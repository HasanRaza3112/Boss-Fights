# MVP Arena Brief

Status: **Approved direction** (per user, 2026-06-25). User will design the environment personally — this brief documents the agreed concept for reference/alignment, not a request for the agent/AI to generate the environment art.

## Concept (Approved)
- Setting: Japanese-style arena
- Location context: Near a lake
- Vegetation: Japanese trees with pink and white leaves (sakura / cherry blossom style)
- Arena shape: Circular
- Arena boundary: No boundary wall — open arena, no visible hard barrier containing the fight space
- Environment ownership: User will design this environment themselves; this document exists so other tools/agents/RAG context stay aligned with the agreed concept, not to hand off art generation

## Design Implications (for awareness, not instruction)
- An open arena with no boundary wall implies either:
  - A natural boundary (cliff edge, lake edge, drop-off) that reads clearly without a literal wall, or
  - An intentionally boundless space where the fight is expected to stay contained by AI behavior/camera framing rather than geometry
  - This distinction is undecided and is the user's call during environment design
- Proximity to a lake may offer reflection/water-surface visual opportunities and ambient sound design (water, wind through sakura trees) — not yet decided
- Circular arena shape supports camera framing for 1v1 boss encounters (consistent radius for lock-on camera systems, common in this genre) — useful to keep in mind during layout, not a hard requirement

## Not Yet Finalized
- Exact arena size/scale
- Time of day / lighting mood
- Weather conditions
- Whether sakura petals are an active particle effect during combat
- Camera-relevant geometry (cover, elevation changes, hazards)
- Audio direction for the arena
- Performance budget for mobile (tree count, water shader cost, particle density)

## Legal/Originality Note
"Japanese arena near a lake with cherry blossom trees" is a broad, common environmental archetype and not tied to any specific Sekiro location. No specific Sekiro arena layout, asset, or level geometry should be referenced or copied during the user's own environment design pass.
