#!/usr/bin/env python3
"""
Boss-Fights Local RAG CLI
--------------------------
A zero-dependency local retrieval tool over the project's approved docs/design
files. Purpose: let IDEs, local LLMs, and AI agents query "what is actually
approved/true about this project" instead of hallucinating or relying on
stale chat memory.

This is intentionally simple (keyword + TF-IDF-lite scoring, no external
services, no API keys) so it runs anywhere Python 3 runs, with zero setup
cost. It is a *retrieval* tool, not a generator — it returns the most relevant
source chunks and lets the calling agent/LLM reason over them.

Usage:
    python tools/rag/rag_cli.py index
    python tools/rag/rag_cli.py query "is there a revive mechanic"
    python tools/rag/rag_cli.py query "akuza height" --top 3

Design notes:
- Indexes all .md files under docs/ and design/ (configurable via SOURCE_DIRS).
- Chunks by markdown headers (## sections) so results map to a meaningful
  unit, not arbitrary line windows.
- Stores an index cache as JSON in tools/rag/.index_cache.json for speed;
  rebuild with `index` whenever docs change.
- No network calls. No third-party packages required (stdlib only).
"""

import argparse
import json
import math
import os
import re
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SOURCE_DIRS = ["docs", "design", "README.md"]
CACHE_PATH = Path(__file__).resolve().parent / ".index_cache.json"

STOPWORDS = {
    "the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
    "and", "or", "but", "if", "then", "of", "to", "in", "on", "for", "with",
    "as", "by", "at", "this", "that", "it", "its", "not", "no", "yet",
    "has", "have", "had", "will", "should", "can", "could", "would", "do",
    "does", "did", "from", "into", "about", "per", "user", "agent",
}


def tokenize(text: str):
    text = text.lower()
    tokens = re.findall(r"[a-z0-9]+", text)
    return [t for t in tokens if t not in STOPWORDS and len(t) > 1]


def find_markdown_files():
    files = []
    for entry in SOURCE_DIRS:
        path = REPO_ROOT / entry
        if path.is_file() and path.suffix == ".md":
            files.append(path)
        elif path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
    return files


def chunk_markdown(path: Path):
    """Split a markdown file into chunks by ## (or #) headers."""
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    chunks = []
    current_header = path.stem
    current_lines = []

    def flush():
        if current_lines:
            body = "\n".join(current_lines).strip()
            if body:
                chunks.append({
                    "file": str(path.relative_to(REPO_ROOT)),
                    "header": current_header,
                    "text": body,
                })

    for line in lines:
        if re.match(r"^#{1,3}\s+", line):
            flush()
            current_header = re.sub(r"^#{1,3}\s+", "", line).strip()
            current_lines = [line]
        else:
            current_lines.append(line)
    flush()
    return chunks


def build_index():
    all_chunks = []
    for f in find_markdown_files():
        all_chunks.extend(chunk_markdown(f))

    df = Counter()
    chunk_tokens = []
    for c in all_chunks:
        toks = tokenize(c["text"] + " " + c["header"])
        chunk_tokens.append(toks)
        for t in set(toks):
            df[t] += 1

    n_docs = max(len(all_chunks), 1)
    for c, toks in zip(all_chunks, chunk_tokens):
        tf = Counter(toks)
        c["term_freqs"] = tf
        c["length"] = max(len(toks), 1)

    index = {
        "n_docs": n_docs,
        "doc_freqs": df,
        "chunks": [
            {
                "file": c["file"],
                "header": c["header"],
                "text": c["text"],
                "term_freqs": dict(c["term_freqs"]),
                "length": c["length"],
            }
            for c in all_chunks
        ],
    }
    CACHE_PATH.write_text(json.dumps(index), encoding="utf-8")
    return index


def load_index(rebuild=False):
    if rebuild or not CACHE_PATH.exists():
        return build_index()
    try:
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except Exception:
        return build_index()


def score_query(query: str, index: dict, top_k: int = 5):
    q_tokens = tokenize(query)
    if not q_tokens:
        return []
    n_docs = index["n_docs"]
    doc_freqs = index["doc_freqs"]
    results = []
    for chunk in index["chunks"]:
        tf = chunk["term_freqs"]
        length = chunk["length"]
        score = 0.0
        for qt in q_tokens:
            f = tf.get(qt, 0)
            if f == 0:
                continue
            df = doc_freqs.get(qt, 1)
            idf = math.log((n_docs + 1) / df) + 1
            score += (f / length) * idf
        if score > 0:
            results.append((score, chunk))
    results.sort(key=lambda x: x[0], reverse=True)
    return results[:top_k]


def cmd_index(args):
    index = build_index()
    print(f"Indexed {len(index['chunks'])} chunks from "
          f"{len(find_markdown_files())} markdown files.")
    print(f"Cache written to {CACHE_PATH}")


def cmd_query(args):
    index = load_index()
    results = score_query(args.query, index, top_k=args.top)
    if not results:
        print("No relevant results found. The project docs may not cover "
              "this topic — treat it as UNDEFINED rather than guessing.")
        return
    for i, (score, chunk) in enumerate(results, 1):
        print(f"\n--- Result {i} (score={score:.3f}) ---")
        print(f"Source: {chunk['file']}  |  Section: {chunk['header']}")
        print(chunk["text"][:800])
        if len(chunk["text"]) > 800:
            print("... [truncated]")


def main():
    parser = argparse.ArgumentParser(
        description="Boss-Fights local RAG CLI — query approved project docs."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_index = sub.add_parser("index", help="(Re)build the local search index.")
    p_index.set_defaults(func=cmd_index)

    p_query = sub.add_parser("query", help="Query the indexed project docs.")
    p_query.add_argument("query", type=str, help="Natural language question.")
    p_query.add_argument("--top", type=int, default=5, help="Number of results.")
    p_query.set_defaults(func=cmd_query)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
