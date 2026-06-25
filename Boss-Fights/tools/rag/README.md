# Boss-Fights Local RAG Tool

A zero-dependency, local-only retrieval tool over this project's approved
docs (`/docs`, `/design`, `README.md`). Its purpose is to give IDEs, local
LLMs, and AI coding agents a fast way to check "what is actually true/approved
about this project" instead of relying on memory, a stale chat thread, or
guesswork — directly addressing the project's stated goal of agents staying
aligned and not hallucinating.

## Why this exists
As more docs, code, and agents get added to this project, there needs to be
one place that any tool — Unity Editor assistant, VS Code/Cursor, a chat
agent, a CI script — can query to get grounded answers from the actual
project source-of-truth files, with citations back to the originating doc.

## Requirements
- Python 3.8+
- No third-party packages (standard library only — `argparse`, `json`,
  `math`, `re`, `collections`, `pathlib`)

## Usage

Build/refresh the index (run this whenever docs change):
```bash
python tools/rag/rag_cli.py index
```

Query it:
```bash
python tools/rag/rag_cli.py query "is there a revive mechanic"
python tools/rag/rag_cli.py query "akuza height and weapon" --top 3
python tools/rag/rag_cli.py query "itsuke spear attack zones"
```

Each result includes:
- The score (relative relevance, not a probability)
- The source file and section header it came from
- The actual text of that section

If nothing relevant is found, the tool says so explicitly rather than
returning a weak match — callers (human or agent) should treat "no result"
as **undefined in project docs**, not as license to invent an answer.

## How it works (plain terms)
- Splits every markdown file in `docs/` and `design/` into chunks by header
  (`#`, `##`, `###`)
- Scores chunks against a query using TF-IDF (term frequency / inverse
  document frequency) — a standard, simple keyword-relevance method
- No embeddings, no vector database, no API key, no network call — this
  keeps it usable offline and inside Unity's own process later if needed
- An index cache (`tools/rag/.index_cache.json`) is built once and reused;
  rebuild it after editing any doc

## Integration paths (future work, not yet built)
- **CLI / IDE agents**: call this script directly as a subprocess and feed
  results into the agent's context before it answers project questions.
- **Unity Editor assistant window**: planned next step (see
  `Agent_Handoff_Context.md`, task 7) — will likely port this same chunking/
  scoring logic into C# so it can run inside the Unity Editor without
  shelling out to Python, or call this script via `Process.Start` as an
  interim approach.

## Maintenance
Re-run `index` after any change to files under `docs/` or `design/`. The
cache is local-only (`.index_cache.json`) and is safe to delete — it will
regenerate automatically on the next query if missing.

## Status
This is a first working version focused on correctness and zero setup
friction. Not yet built: semantic/embedding-based search, automatic
re-indexing on file save, and the Unity Editor integration window.
