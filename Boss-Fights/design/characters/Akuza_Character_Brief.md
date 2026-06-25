# Akuza — Character Brief

Status: **Approved direction** (per user, 2026-06-25). Visual execution (final outfit detailing, face, hair styling specifics) is still open for iteration — treat described traits as locked, rendered interpretation as proposal until the user signs off on generated art.

## Identity
- Name: Akuza
- Role: Player character / protagonist
- Archetype: Samurai
- Narrative function: Lone duelist, the player's avatar through the boss-rush

## Physical Description (Approved)
- Height: 6 ft (180 cm) — tall but human-scaled, not exaggerated
- Build: Muscular, athletic warrior physique — strength read, not bulky/tank
- Skin tone: Fair
- Hair: Long, white, loose or tied back (style not yet finalized)
- Weapon: Katana, single-handed primary grip
- Outfit: "Ghost" themed outfit — interpreted as pale/white-and-grey samurai garb with a tattered, spectral, or faded aesthetic (final pattern/armor detailing not yet finalized — this is a proposal-level interpretation of "ghost outfit" pending visual reference approval)

## Anime-Stylized Direction
- Stylization level: Anime-stylized, not photorealistic — sharper jaw/face planes, clean silhouette readability at a distance (important for boss-fight camera readability), exaggerated but controlled proportions
- Color identity: White hair + fair skin + pale "ghost" outfit suggests a desaturated, monochrome-leaning palette with a single accent color reserved for: blood, a sash, hilt wrapping, or an ability-effect glow (color TBD — proposal)

## Not Yet Finalized
- Exact armor plate layout / how much armor vs. cloth
- Facial design specifics (face shape, eyes, scars, age)
- Hair style (flowing vs. tied topknot vs. half-tied)
- Color accent choice
- Katana sheath/scabbard design and how it's worn
- Idle/combat stance silhouette
- Rig requirements (humanoid Mecanim-compatible assumed default, not yet confirmed)

## Legal/Originality Note
This design is original. It is not based on any specific Sekiro character, model, or silhouette. "Samurai with katana" is a broad archetype, not a copyrightable design — final outfit and proportions should remain distinct from any specific game character once visual references are generated.

---

## 3D Generation Prompts

### Recommended workflow
Most AI 3D generators (Meshy, Tripo3D, Luma Genie, etc.) produce far better results from a clean 2D reference image first, then convert that to 3D, rather than going text-to-3D directly. Two prompt sets are given below for this reason.

### Step 1 — 2D Character Reference Prompt (use in an image model, e.g. Midjourney/SDXL/DALL·E)

```
Full body character reference sheet, front view and back view, anime-stylized samurai
warrior named Akuza. Tall muscular male figure, approximately 6 feet tall, athletic
warrior build (not bulky). Fair skin. Long white hair, flowing past shoulders.
Wearing a pale, weathered "ghost-like" samurai outfit — faded white and grey hakama
and haori with tattered, wind-worn edges, subtle torn fabric details, minimal armor
plating, giving a spectral/haunting silhouette. Holding a single katana in both
hands, sheathed scabbard worn at the hip. Neutral T-pose or relaxed combat-ready
stance. Clean, sharp anime art style with strong silhouette readability, cel-shaded
lighting, dramatic but clean rim light separating the figure from a plain neutral
grey background. Highly detailed face with sharp anime facial structure, calm
intense expression. No other characters, no text, no logos. Orthographic-style
turnaround for use as 3D modeling reference.
```

### Step 2 — Image-to-3D / Text-to-3D Prompt (Meshy, Tripo, Luma, etc.)

```
Generate a 3D game character model: anime-stylized male samurai, 6 feet tall,
muscular athletic build, fair skin tone, long white hair. Wearing a pale white
and grey "ghost" themed samurai outfit with tattered cloth edges and minimal
armor, spectral/haunted aesthetic. Holding a katana in a two-handed grip.
Style: stylized anime game character, clean topology suitable for rigging,
cel-shaded / toon-compatible textures, T-pose, game-ready proportions,
PBR-friendly materials, optimized for Unity real-time rendering on PC and mobile.
```

### Notes for the artist/generator pass
- Keep poly count mobile-friendly if a single shared model targets both PC and mobile — consider a high-detail PC variant and a simplified mobile LOD later.
- Generate the T-pose version first for rigging; pose/action renders are a separate downstream pass.
- Flag any generated result back against this brief before treating it as approved — generation is a proposal step, not automatic canon.
