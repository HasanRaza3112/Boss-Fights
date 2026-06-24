# Agent Handoff Context

Use this file to continue work with another agent without losing direction.

## Conversation Summary

The user is a game developer planning a new Unity game project inspired by Sekiro's boss-fight intensity, but the project must be original and legally safe.

The game repo is:
- `F:\Repos\Boss-Fights`
- GitHub remote: `https://github.com/HasanRaza3112/Boss-Fights.git`

The initial pasted JSON research file claimed to list Sekiro bosses and asset resources. It was reviewed and found unreliable:
- It mixed real Sekiro bosses with many invented names.
- It made unsafe claims about downloadable/extracted Sekiro models.
- It should not be treated as source truth.
- It can only be treated as rough inspiration notes.

The design direction was refined by the user:
- Hero name: Akuza
- Akuza identity: samurai
- First boss: human rival
- Visual tone: anime-stylized
- Engine: Unity
- Platforms: PC and mobile
- MVP purpose: portfolio and possible commercial publishing release
- Difficulty: three modes using damage taken and damage given modifiers, with room for posture and timing tuning
- RAG: should work as both a Unity-integrated assistant and a local tool for IDEs, LLMs, and AI agents so they stay aligned and do not hallucinate

## Current Project Truth

Boss-Fights is a boss-only third-person action game. The MVP should prove one polished samurai duel before expanding.

Confirmed:
- Akuza is a samurai.
- Gameplay is 3D.
- UI and supporting art can use 2D assets.
- First boss should be a human rival.
- Style is anime-stylized.
- The game uses Unity.
- PC and mobile are target platforms.
- MVP is both a portfolio piece and a possible publishing release.
- RAG should be part of the project knowledge workflow.

Not yet finalized:
- Final game title.
- Final Akuza visual design.
- Final rival boss name.
- Final arena theme.
- Exact Unity version.
- Asset pipeline.
- Team size.
- Timeline.
- Monetization.
- Store targets.
- Whether revive mechanic exists.
- Whether practice mode ships in MVP.

## Legal Direction

Sekiro is research inspiration only. Do not copy or use:
- Sekiro names
- Character designs
- Boss designs
- Models
- Animations
- Level layouts
- UI
- SFX/music
- Lore
- Extracted assets
- Unclear fan asset packs

Study only:
- Encounter pacing
- Readability
- Posture pressure concepts
- Boss phase structure
- Rematch/gauntlet design patterns

## Documents Added

- `README.md`
- `docs/Akuza_Boss_Rush_GDD.md`
- `docs/RAG_System_Design.md`
- `docs/Commercial_Release_Checklist.md`
- `docs/Agent_Handoff_Context.md`

## Suggested Next Agent Tasks

1. Create `design/characters/Akuza_Character_Brief.md`.
2. Create `design/bosses/Boss_01_Rival_Brief.md`.
3. Create `design/environments/MVP_Arena_Brief.md`.
4. Create combat tuning spreadsheet or Markdown table.
5. Scaffold Unity project folders if the user wants implementation to begin.
6. Build local RAG CLI under `tools/rag`.
7. Build Unity Editor assistant window after local RAG is working.

## Agent Behavior Rules

- Treat approved docs as source of truth.
- If a decision is not documented, say it is undefined.
- Mark new ideas as proposals.
- Do not invent approved project details.
- Keep the MVP small and polished.
- Prioritize commercial-safe original assets.
- Avoid turning the project into an open world or RPG unless the user explicitly changes scope.

