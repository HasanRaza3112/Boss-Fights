# Akuza: Boss Rush MVP - Game Design Document

## 1. High Concept

Akuza is a third-person anime-stylized samurai boss-rush game for PC and mobile, built in Unity. The game is inspired by the intensity and discipline of posture-based sword duels, but it must remain fully original in characters, lore, animation, art, audio, UI, and combat presentation.

The MVP focuses on one playable hero, one human rival boss, one arena, three difficulty modes, and a combat system strong enough to become the foundation for a commercial boss-only action game.

## 2. Product Goals

Primary goals:
- Create a portfolio-quality MVP that clearly shows game development skill.
- Build the project in a way that can grow into a commercial release.
- Keep scope tight enough to finish and polish.
- Make documentation strong enough that other developers, IDE agents, and LLM tools can stay aligned.

Secondary goals:
- Build reusable boss design templates.
- Build a RAG knowledge base that prevents hallucinated design drift.
- Prepare legal-safe research and asset pipelines from day one.

## 3. Design Pillars

1. Boss fights only
   - The game is not about clearing levels of small enemies.
   - Each content unit is a complete duel with phases, tells, counterplay, and mastery.

2. Samurai precision
   - Akuza wins through timing, posture control, and decisive sword strikes.
   - The player should feel like a trained samurai, not a generic action hero.

3. Fair challenge
   - Every boss attack must be readable.
   - Difficulty comes from timing, pattern knowledge, and pressure, not cheap surprise.

4. Anime-stylized impact
   - Strong silhouettes, sharp poses, expressive VFX, and cinematic finishers.
   - Visual style should support readability first and spectacle second.

5. Mobile and PC parity
   - The same core game should work on mobile and PC.
   - Difficulty and controls can be tuned per platform, but the combat fantasy stays the same.

6. Original identity
   - Sekiro can be studied for lessons, not copied.
   - Akuza, the rival, weapons, environment, story, names, animations, and systems must be original.

## 4. Target Platforms

Primary:
- Windows PC
- Android

Secondary after MVP:
- iOS
- Steam Deck or handheld PC

Recommended Unity stack:
- Unity 6 LTS or current stable Unity LTS
- Universal Render Pipeline
- Unity Input System
- Cinemachine
- Addressables later if content grows

## 5. Genre and Camera

Genre:
- Third-person action boss rush

Camera:
- Lock-on third-person combat camera
- Slightly cinematic but still readable
- Wider than a pure cinematic camera on mobile to protect visibility
- Boss should remain visible during lock-on except during intentional cinematic finishers

## 6. Target Audience

Players who enjoy:
- Boss fights
- Samurai fantasy
- Deflect and parry timing
- High-skill combat
- Anime-stylized action
- Short replayable encounters
- Improving rank, time, and mastery

## 7. MVP Scope

Must have:
- One playable hero: Akuza
- One human rival boss
- One polished arena
- Lock-on camera
- Attack, heavy attack, deflect, guard, dodge, sprint, heal, and execute
- Player health and posture
- Boss health and posture
- At least two boss phases
- Three difficulty modes
- PC keyboard/mouse controls
- Controller support
- Mobile touch controls
- Pause menu
- Restart loop
- Results screen
- Basic settings for audio, graphics, input sensitivity, and control layout

Should have:
- Practice mode
- Boss rematch mode
- Timing assist accessibility option
- Haptics on mobile
- Slow-motion execution moment
- Simple lore intro before the duel

Not in MVP:
- Open world
- Large story campaign
- Multiple playable characters
- Multiplayer
- Large enemy roster
- Complex loot
- Extensive RPG builds
- Proprietary Sekiro assets or extracted models

## 8. Player Character: Akuza

Identity:
- Akuza is a samurai.
- He should feel disciplined, controlled, and dangerous.
- His fighting style is built around clean sword technique, posture control, and decisive finishers.

Visual direction:
- Anime-stylized 3D.
- Strong samurai silhouette.
- Signature katana or original blade variant.
- Distinct cloak, sash, shoulder armor, mask, or arm detail.
- Avoid directly copying famous samurai or Sekiro character silhouettes.

Base combat profile:
- Health: medium
- Posture: medium
- Damage: medium
- Mobility: high
- Defense: timing-based
- Skill ceiling: high

Core actions:
- Light attack: quick katana chain
- Heavy attack: slower posture-focused strike
- Deflect: timed input that damages enemy posture
- Guard: held block that costs posture
- Dodge step: short evasive movement
- Sprint: repositioning
- Heal: limited charges
- Execute: cinematic finisher after posture break or phase threshold

Optional special ability:
- Focus Cut: charged samurai strike powered by perfect deflects.

## 9. Weapons

MVP weapon:
- Akuza uses one primary sword.

Recommended weapon:
- Katana-inspired original blade.
- Keep the silhouette familiar enough to read instantly.
- Add one unique visual identity element, such as a broken guard, red cord wrap, black steel edge, or spirit-forged glow.

Future weapon ideas:
- Odachi for slower heavy play.
- Dual short blades for speed mode.
- Spear boss weapons for rival variety.
- Cursed blade cosmetics only if they do not change MVP scope.

Weapon requirements:
- Clear swing arcs.
- Reliable hitbox timing.
- Distinct light and heavy attack animation language.
- Strong deflect clash VFX and SFX.

## 10. First Boss: Human Rival

MVP boss archetype:
- Human rival samurai.

Purpose:
- Teach the player the entire combat loop.
- Test deflect, posture pressure, dodge, heavy attack, and phase changes.
- Provide a portfolio-worthy duel without monster animation complexity.

Temporary name:
- Boss_01_Rival

Original boss name candidates:
- Renga, the Broken Banner
- Lord Kaien of the Red Gate
- Haku Ren, the Moon-Cut Rival
- Jinrai, Last Blade of the Old House

Boss profile:
- Human-sized
- Katana or odachi weapon
- Aggressive but readable
- Two phases
- Duel length: 2-4 minutes for skilled players
- New player attempts: roughly 10-25 depending on difficulty

Phase 1:
- Basic slash combo
- Delayed heavy cut
- Dash slash
- Guard break attempt
- Punishable recovery windows

Phase 2:
- Faster combo chains
- One new perilous thrust or sweep
- Stronger posture recovery
- More delayed timing mixups
- Visible stance, VFX, or armor change

## 11. Difficulty System

The game should ship with three difficulty modes. MVP tuning can focus on damage taken and damage given, but later difficulty should also affect posture, timing windows, and boss aggression.

Mode 1: Disciple
- For players new to precise deflect combat.
- Player takes less damage.
- Player deals slightly more health and posture damage.
- Boss posture recovers slower.
- Deflect timing window is more forgiving.

Mode 2: Samurai
- Intended default experience.
- Balanced player and boss damage.
- Standard posture recovery.
- Standard deflect timing window.

Mode 3: Ronin
- For mastery and replay value.
- Player takes more damage.
- Player deals less damage.
- Boss posture recovers faster.
- Deflect window is tighter.
- Boss can use more aggressive phase 2 patterns.

Initial tuning table:

| Setting | Disciple | Samurai | Ronin |
| --- | --- | --- | --- |
| Player damage taken | 0.75x | 1.0x | 1.35x |
| Player damage dealt | 1.15x | 1.0x | 0.85x |
| Player posture damage taken | 0.8x | 1.0x | 1.25x |
| Boss posture damage taken | 1.2x | 1.0x | 0.85x |
| Perfect deflect window | 180 ms | 140 ms | 110 ms |
| Boss posture recovery | 0.8x | 1.0x | 1.25x |

## 12. Combat System

Health:
- Health determines survival.
- Reaching zero ends the attempt unless a revive mechanic is added later.

Posture:
- Posture represents combat pressure and balance.
- Deflecting, attacking, and countering increases boss posture.
- Blocking, taking hits, and mistiming defense increases player posture.

Player posture break:
- Player is briefly stunned.
- Boss can punish if close.

Boss posture break:
- Boss becomes vulnerable to execution or phase transition.

Attack types:
- Standard attacks can be blocked, deflected, or dodged.
- Heavy attacks deal high posture damage.
- Thrusts require precise counter or dodge.
- Sweeps require jump, spacing, or special counter.
- Grabs cannot be blocked.

## 13. Environment

MVP arena:
- One stylized samurai duel arena.

Recommended concept:
- A moonlit temple courtyard or ruined training ground.
- Strong anime lighting.
- Clear ground plane.
- Wind, cloth banners, leaves, sparks, and sword clash VFX for atmosphere.

Gameplay requirements:
- Circular or oval duel space.
- No geometry that traps camera.
- No props that allow boss cheese.
- Clear boundary treatment.
- Readable contrast between characters and background.
- Mobile performance-friendly layout.

Future environments:
- Burned castle gate.
- Bamboo arena.
- Snow shrine.
- Red bridge at sunset.
- Spirit realm duel stage.

## 14. 2D, 3D, and Art Pipeline

Game format:
- 3D gameplay.
- 2D elements for UI, icons, concept art, portraits, and menus.

3D assets needed for MVP:
- Akuza model
- Rival boss model
- Katana/blade models
- Arena kit
- VFX meshes/particles
- Camera collision helpers
- Hitbox/hurtbox debug tools

2D assets needed for MVP:
- Logo
- Key art
- UI icons
- Health/posture UI
- Difficulty icons
- Button prompts
- Mobile touch controls
- Store capsules/screenshots later

Animation assets needed:
- Akuza idle, locomotion, attacks, heavy attack, deflect, guard, dodge, hit reactions, heal, posture break, execution
- Boss idle, locomotion, attacks, heavy attacks, phase shift, hit reactions, posture break, death/defeat, execution victim animation

Commercial note:
- Prototype placeholders are acceptable during development.
- Public release needs original or clearly licensed assets.

## 15. Backend and Tooling

MVP game backend:
- No live backend required for the first playable MVP.

Local systems:
- Local save data
- Settings save
- Results history
- Difficulty preference
- Optional replay metadata

Future backend options:
- Leaderboards
- Cloud saves
- Analytics
- Crash reporting
- Content update delivery
- Player feedback submission

Recommended MVP services:
- Unity Cloud Diagnostics or equivalent crash reporting
- Basic analytics only if privacy policy is ready
- No account system until needed

## 16. RAG and AI Agent Direction

The RAG system should serve two roles:
- Local research and planning tool for developers using different IDEs, LLMs, and AI agents.
- Unity-integrated assistant that can answer project-specific questions without hallucinating or drifting from the GDD.

The RAG system must prioritize:
- This GDD
- Production checklists
- Combat tuning sheets
- Boss design briefs
- Legal-safe asset references
- Current Unity implementation notes

The RAG system must reject:
- Unsourced invented facts
- Unsafe asset extraction guidance
- Claims that proprietary assets are usable
- Design changes that conflict with approved docs unless clearly marked as proposals

## 17. Release Metrics

MVP success criteria:
- Player can understand controls within 2 minutes.
- First boss feels fair after repeated attempts.
- Skilled player can clear the fight in 2-4 minutes.
- Mobile build maintains stable performance on target devices.
- PC build supports keyboard/mouse and controller.
- Result screen encourages replay.
- Documentation is good enough for another agent or developer to continue.

## 18. Open Decisions

Still needed:
- Final Akuza visual design
- Final rival boss name and backstory
- Final arena theme
- Exact Unity version
- Asset source plan
- Team size and timeline
- Monetization model
- Store targets
- Whether to add revive mechanic
- Whether to include practice mode in MVP

