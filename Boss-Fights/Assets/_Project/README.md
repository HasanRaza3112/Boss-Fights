# Unity Project Scaffold — Boss-Fights

This is the initial Unity folder scaffold for the project. No actual Unity project (ProjectSettings binary data, Library, etc.) has been generated yet — this provides the **Assets/ folder structure** so future content has a defined home and stays organized as the team/agent count grows.

## Setup Instructions
1. Create a new Unity project (3D, URP recommended for anime-stylized look — not yet finalized, confirm Unity version with the user first; see "Not Yet Finalized" in Agent_Handoff_Context.md).
2. Copy the contents of this `Assets/_Project` folder into your new Unity project's `Assets/` folder, OR open this repo root as the Unity project root if you generate the project here.
3. `.gitkeep` files mark intentionally empty folders so they survive Git (Git does not track empty directories).

## Folder Structure

```
Assets/_Project/
├── Characters/Akuza/        — player character models, animations, materials, prefabs
├── Bosses/Itsuke/           — Boss 01 models, animations, materials, prefabs
├── Environments/MVP_Arena/  — arena models, materials, prefabs (user is designing this themselves)
├── Scripts/
│   ├── Combat/              — damage, posture, hit detection, parry/dodge logic
│   ├── Player/              — Akuza control scripts
│   ├── AI/                  — boss behavior/state machines
│   ├── Camera/              — lock-on / combat camera systems
│   ├── UI/                  — HUD, health/posture bars, menus
│   └── Core/                — game state, scene management, shared systems
├── UI/2D/                   — 2D UI art assets
├── Audio/SFX, Audio/Music   — sound
├── VFX/                     — particle/effect assets
└── Scenes/                  — Unity scene files
```

## Naming Convention
- Folders use the established names from approved docs: `Akuza`, `Itsuke`, `MVP_Arena`. Do not rename these without updating the corresponding design docs in `/design`.
- `_Project` prefix keeps custom content sorted above any imported third-party asset folders in the Unity Project window.

## Status
This is structural scaffolding only — no gameplay code, models, or scenes exist yet. Treat folder presence as organizational groundwork, not as confirmation that any asset within has been created.
