# Illustration seule — Cloche

Outil : imagegen intégré. Entrée : première proposition de cloche, désormais conservée dans `../drafts/1-cloche-source.png`.

Sortie : `1-cloche.png`, illustration sur fond transparent. Le fond vert et le cercle blanc sont ajoutés séparément par `compose_thumbnail.py`.

## Prompt

Use case: background-extraction. Extract ONLY the golden yellow bell illustration from the supplied thumbnail as a standalone PNG with a genuinely transparent alpha background. Preserve the bell's recognizable shape, little top loop, warm brown outline, yellow body, orange rim and clapper, and friendly flat educational style. Remove the green background AND the entire white circle completely. The hole in the top loop must also be transparent. There must be ONLY the bell itself and transparency, no circle, no badge, no white rectangle, no shadow, no text, no checkerboard baked into pixels. Keep crisp clean antialiased edges and simplified flat color fills. Center the complete uncut bell on a square transparent canvas, taking up about 80% of its height. This file will be composited by code onto a fixed reusable thumbnail template, so DO NOT generate any background or circle.
