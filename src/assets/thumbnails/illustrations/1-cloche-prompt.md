# Illustration seule — Cloche simplifiée

Outil : imagegen intégré. Génération à partir du prompt ci-dessous, dont les couleurs et la direction visuelle sont issues de la charte graphique et de la demande de simplification de l’utilisateur.

Sortie : `1-cloche.png`, illustration transparente. Le fond exact #81cc71 et le disque blanc sont ajoutés séparément par `compose_thumbnail.py`, sans changement de géométrie.

Couleurs demandées : jaune #ffee4d et ocre #9a6f03. Aucun détail décoratif.

## Prompt

Use case: illustration-story. Generate ONLY one isolated very simple school bell illustration for an Origamia educational thumbnail. Genuine transparent PNG alpha background.
STRICTLY TWO COLORS ONLY: bright yellow #ffee4d (RGB 255,238,77) for the bell body and upper loop, and ochre #9a6f03 (RGB 154,111,3) for the inside of the bottom opening and the small clapper. No third color, no orange, no cream, no black, no white. Flat solid fills without gradients, highlights, reflections, grain or texture.
Minimal clear friendly 2D silhouette: one compact rounded top loop with a transparent hole, a simple rounded bell body flaring slightly at the bottom, and one small visible round clapper. Front view, nearly upright, no dramatic perspective. At most a thin ochre edge only where needed for legibility. Rounded uncomplicated forms, cheerful children's educational illustration. All parts belong to the bell itself.
Absolutely NO decorative patterns, triangles, folded-paper facets, geometric ornament, sound marks, rays, stars, dots, reflections, shine, additional objects, face, letters, text, badge or circle. Do not embellish. The user explicitly asks for fewer colors and no irrelevant details. Bell centered, complete, with transparent margin. No background color and no white disk: these are added separately by code. Simple enough to remain immediately readable at 96 pixels tall.
