# RAG and AI Agent System Design

## 1. Purpose

The Boss-Fights RAG system is a project memory and guardrail system. It should help developers, IDE tools, LLMs, and AI agents answer project questions using approved project documents instead of guessing.

The system must support:
- Local use across IDEs and agent tools
- Unity-integrated assistant access
- Search over design, production, legal, combat, and asset notes
- Clear source citations
- Hallucination reduction

## 2. Core Rule

The RAG system is not allowed to invent project truth.

If a question is not answered by indexed project sources, the assistant should say:
- The answer is not defined yet.
- Which document should be updated.
- What decision is needed from the developer.

## 3. Authoritative Source Priority

Highest priority:
- `docs/Akuza_Boss_Rush_GDD.md`
- `docs/Commercial_Release_Checklist.md`
- Approved boss design briefs
- Approved combat tuning sheets
- Approved technical architecture notes

Medium priority:
- Meeting notes
- Prototype test notes
- Asset shortlist documents
- Legal review notes
- Unity implementation notes

Low priority:
- External research summaries
- Wiki-derived factual notes
- Video analysis notes
- Inspiration boards

Never authoritative:
- Raw AI chat output
- Unsourced JSON research
- Fan asset packs with unclear license
- Extracted proprietary game assets
- Decompiled or pirated content

## 4. Recommended Architecture

Local tool:
- Python CLI
- ChromaDB or LanceDB for local vector storage
- Markdown and JSON ingestion
- Simple source citation output
- Runs without internet after documents are indexed

Unity-integrated assistant:
- Unity Editor window
- Sends queries to a local RAG server
- Shows answer, citations, and confidence
- Can open referenced local files
- Should not edit game files automatically in MVP

Optional backend:
- FastAPI local service
- PostgreSQL with pgvector for team or cloud usage
- REST endpoints for query, ingest, list sources, and health check

## 5. Suggested Folder Structure

```text
Boss-Fights/
  docs/
    Akuza_Boss_Rush_GDD.md
    RAG_System_Design.md
    Commercial_Release_Checklist.md
    Agent_Handoff_Context.md
  research/
    external_sources/
    summaries/
    legal_notes/
  design/
    bosses/
    combat/
    characters/
    environments/
  tools/
    rag/
      ingest.py
      query.py
      server.py
      config.yaml
```

## 6. Document Metadata Schema

Each indexed document or chunk should track:

```json
{
  "title": "",
  "path": "",
  "source_url": "",
  "source_type": "gdd | checklist | design_brief | research | legal | implementation_note",
  "authority": "approved | draft | external | unsafe",
  "topic": "",
  "tags": [],
  "license_status": "original | licensed | research_only | unclear | unsafe",
  "created_at": "",
  "updated_at": ""
}
```

## 7. Chunking Rules

- Chunk Markdown by heading where possible.
- Target 500-900 tokens per chunk.
- Keep tables with their surrounding explanation.
- Keep legal warnings attached to the source they refer to.
- Keep boss moves together when they belong to the same phase.

## 8. Query Behavior

The assistant should:
- Cite source file names.
- Prefer approved project docs.
- Separate confirmed facts from proposals.
- Say when something is undefined.
- Ask for a decision when a missing answer blocks work.

The assistant should not:
- Pretend a boss, weapon, or mechanic is approved when it is only a suggestion.
- Copy external copyrighted content into design docs.
- Recommend proprietary asset extraction.
- Replace project direction based on general LLM knowledge.

## 9. Example Queries

- "What is the current MVP scope?"
- "What is Akuza's confirmed character identity?"
- "What difficulty modes are approved?"
- "What assets are needed for the first boss?"
- "Is backend required for the MVP?"
- "What should the Unity assistant say if the answer is missing?"
- "Which sources are unsafe for commercial use?"

## 10. Unity Editor Assistant MVP

Editor window features:
- Search box
- Answer panel
- Citations list
- Open source document button
- "Undefined decision" warning
- Copy answer button

Useful future features:
- Generate boss brief from approved template
- Validate a boss design against the GDD
- List missing assets for a selected milestone
- Compare current implementation notes against design docs
- Create tasks for unresolved decisions

## 11. Anti-Hallucination Prompt Contract

Every agent using this repo should follow this contract:

```text
Use the indexed Boss-Fights docs as the source of truth.
If the docs do not define an answer, say it is undefined.
Do not invent approved project decisions.
Mark suggestions as proposals.
Do not use copied Sekiro assets, names, lore, animations, UI, audio, or extracted files.
Prefer the GDD, release checklist, and approved design briefs over external references.
```

## 12. First Implementation Plan

Milestone 1:
- Create Markdown docs.
- Create local ingestion script.
- Index docs folder.
- Support terminal query with citations.

Milestone 2:
- Add Unity Editor window.
- Query local RAG server.
- Display answers and citations inside Unity.

Milestone 3:
- Add design validation prompts.
- Add source authority filtering.
- Add unsafe source detection.

