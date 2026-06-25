# Boss 01 — Itsuke (Rival Brief)

Status: **Approved direction** (per user, 2026-06-25). Visual execution details beyond what's listed are open — described traits are locked, rendered interpretation is proposal until signed off.

## Identity
- Name: Itsuke
- Role: Boss 01 — first major encounter, human rival
- Archetype: Samurai / spear-wielding duelist
- Narrative function: Akuza's first true test — establishes the game's combat language and stakes

## Physical Description (Approved)
- Height: 7.5 ft (228 cm) — notably taller than Akuza (6 ft), should read as physically dominant/looming in-frame
- Build: Muscular, imposing physique — bigger and heavier-presence than Akuza
- Skin tone: Dark
- Hair: Long, grey
- Face: Wears a mask (style/design not yet finalized — could be lacquered samurai mask, cloth wrap, demonic oni-style mask, etc. — proposal pending visual reference)
- Weapon: Spear (yari-style), with **both-side attacking zone** — i.e. both ends of the spear are usable as attack points, giving Itsuke a wider/dual-ended threat range than a standard polearm. This is a core moveset-defining trait, not just visual flavor — gameplay implication: his attack telegraphs and punish windows should differ on each end (e.g. blade-tip thrusts vs. butt-end sweeps/strikes), giving the player two distinct spacing problems to read.

## Anime-Stylized Direction
- Stylization level: Matches Akuza's anime-stylized approach — same art style language across both characters for visual consistency
- Silhouette: Should be instantly distinguishable from Akuza at a glance even in motion-blurred combat — height difference, mask, and spear silhouette (long polearm vs. short katana) all help with this
- Color identity: Dark skin + grey hair + mask suggests a deeper, more muted/shadowed palette than Akuza's pale "ghost" look — creates visual contrast between hero and first rival (proposal — color accent TBD)

## Gameplay Implication Notes (for later combat tuning, not final)
- Dual-ended spear suggests Itsuke should have attack patterns from both close range (spear-tip thrusts) and slightly wider sweep range (butt-end strikes), making spacing/positioning a key skill test for the player in this first fight
- As the first boss, his moveset should teach core mechanics (likely parry/dodge timing, posture pressure) without overwhelming the player — exact difficulty curve deferred to Combat Tuning Table (not yet authored)

## Not Yet Finalized
- Mask design specifics (full-face vs. half-mask, material, decoration)
- Armor design / how much armor vs. cloth
- Exact spear length and blade shape on both ends
- Color accent choice
- Specific attack patterns / phase structure
- Stance/idle silhouette
- Voice/sound direction
- Whether Itsuke has a backstory/dialogue beat in MVP or is purely a silent duel

## Legal/Originality Note
This design is original and not based on any specific Sekiro character. A tall masked spear-wielding rival is a broad archetype; the dual-ended spear concept and 7.5 ft height/proportions help keep the silhouette clearly distinct from existing properties once visual references are generated.

---

## 3D Generation Prompts

### Step 1 — 2D Character Reference Prompt (use in an image model first)

```
Full body character reference sheet, front view and back view, anime-stylized
samurai warrior boss character named Itsuke. Extremely tall and imposing male
figure, approximately 7.5 feet tall, heavily muscular and dominant physique,
noticeably larger and more imposing than an average warrior. Dark skin tone.
Long grey hair, flowing or partially tied. Wearing a full face or half-face
samurai mask, intimidating design, with dark, heavy samurai armor — muted dark
color palette, battle-worn. Wielding a long spear (yari) designed so BOTH ends
are usable as weapons — a sharp blade tip on one end and a secondary striking
point/blade or weighted butt-end on the other end, clearly visible dual-ended
weapon silhouette. Neutral combat-ready stance, weapon held diagonally to show
both ends. Clean, sharp anime art style, strong silhouette readability, cel-shaded
lighting, dramatic rim light on a plain neutral grey background. No other
characters, no text, no logos. Orthographic-style turnaround for 3D modeling
reference.
```

### Step 2 — Image-to-3D / Text-to-3D Prompt (Meshy, Tripo, Luma, etc.)

```
Generate a 3D game character model: anime-stylized male samurai boss character,
7.5 feet tall, heavily muscular and imposing build, dark skin tone, long grey
hair, wearing a samurai face mask and dark battle-worn armor. Wielding a long
dual-ended spear with a usable attack point on both ends (blade tip and a
secondary striking end). Style: stylized anime game boss character, clean
topology suitable for rigging, cel-shaded / toon-compatible textures, T-pose,
game-ready proportions, PBR-friendly materials, optimized for Unity real-time
rendering on PC and mobile, scaled noticeably larger than a standard human
character rig.
```

### Notes for the artist/generator pass
- Model Itsuke and Akuza at correct relative scale (7.5 ft vs 6 ft) early — this height gap is a deliberate intimidation/readability choice for the first fight.
- The dual-ended spear is a gameplay-defining prop — make sure both ends are visually distinct enough that the player can read which end is about to attack mid-animation.
- Mask should not obscure readability of attack tells (head turn, wind-up) needed for boss-fight combat clarity.
