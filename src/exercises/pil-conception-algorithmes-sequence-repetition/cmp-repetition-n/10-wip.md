# Reprise de la série cmp-repetition-n — exercices 10 à 12, 179 et 180

## Gate 0 - Workflow

- Workflow relu : oui
- Date de relecture : 2026-09-02
- Représentation(s) autorisée(s) pour cette série : programme Turtle entièrement développé, sans boucle, présenté à l’élève comme support d’observation. Pour la variante 180, le support est du code Python Turtle brut, sans projet Vittascience.
- Représentation(s) interdites pour cette série : demander à l’élève de paramétrer les instructions ; introduire une boucle dans le programme observé ; utiliser des formes abstraites difficiles à reconnaître ; générer un projet Vittascience pour la variante 180.
- Décision : déclinaison autorisée après validation explicite du pilote 10 par l’utilisateur ; réécriture de 180 autorisée après abandon explicite de l’échelle.

## Attendu

- Compétence : `cmp-repetition-n`
- Attendu : `att-repetition-n-cm1`
- Geste travaillé : déterminer combien de fois un motif d’instructions est répété dans un programme.
- Série concernée : 10, 11, 12, 179, 180.

## Forme invariante

- Type : `free`.
- Support : programme Turtle entièrement développé, sans boucle.
- Le programme produit une forme immédiatement reconnaissable et nommée dans le contexte.
- Un même groupe d’instructions apparaît plusieurs fois à l’identique.
- Des instructions peuvent apparaître avant ou après le motif répété : l’élève doit aussi repérer les limites du motif.
- Consigne identique : « Combien de fois ce morceau est-il répété ? Écris uniquement le nombre. »
- Réponse attendue : un entier.
- `essais: 2`.
- Feedback essai 1 : aide à repérer les limites du motif sans donner le nombre.
- Feedback final : indique le nombre de répétitions et montre le motif répété.
- Les paramètres Turtle sont déjà fixés ; l’élève n’a rien à modifier.
- Les variantes changent de dessin et de motif, mais pas de geste cognitif ni de format de réponse.
- Une mise en situation spécifique peut être inventée quand aucun rituel existant ne correspond au tracé, à condition qu’elle reste concrète et n’ajoute aucune compétence parasite.

## Variante 10 — validée comme pilote

- Cible : escalier simplifié de trois marches.
- Situation : `rit-dessiner-pictogramme-escalier`.
- Motif : `avancer 50` → `gauche 90°` → `avancer 50` → `droite 90°`.
- Répétitions : 3.
- Programme : 12 blocs.

## Variante 11

- Cible : ligne pointillée.
- Situation : `rit-tracer-ligne-pointillee-affiche`.
- Motif : `avancer 10` → `lever le stylo` → `avancer 10` → `baisser le stylo`.
- Répétitions : 4.

## Variante 12

- Cible : peigne simplifié.
- Situation : `rit-dessiner-pictogramme-peigne`.
- Motif : `avancer 10` → `droite 90°` → `avancer 50` → `reculer 50` → `gauche 90°`.
- Répétitions : 5.

## Variante 179

- Cible : hublots ronds alignés.
- Situation : `rit-dessiner-hublots-sous-marin`.
- Motif : `cercle 20` → `lever le stylo` → `avancer 50` → `baisser le stylo`.
- Répétitions : 3.

## Variante 180

- Cible : serpent stylisé / ligne ondulée continue.
- Situation : atelier de dessin, sans compétence externe requise.
- Support : code Python Turtle brut affiché directement dans l’exercice ; aucun projet Vittascience.
- Instructions hors motif : `forward(20)` avant le motif et `forward(20)` après le motif.
- Motif : `circle(25, 180)` → `circle(-25, 180)`.
- Répétitions : 4.
- Programme : 10 instructions Turtle après l’import, suffisamment court pour être parcouru mentalement par un élève de CM1.
- Le motif produit une ondulation complète ; quatre répétitions forment le corps du serpent.

## Retours utilisateur pris en compte

- Les anciens triangle/carré/hexagone/pentagone/octogone étaient trop répétitifs.
- Les formes doivent être immédiatement reconnaissables.
- Les mises en situation peuvent être inventées si cela évite de plaquer un rituel sans rapport avec le dessin.
- 2026-09-02 : utilisateur autorise explicitement la déclinaison des variantes 11, 12, 179 et 180 à partir du pilote 10.
- 2026-09-02 : utilisateur modifie les nombres de répétitions et certains paramètres de tracé afin d’éviter une série trop homogène ; conserver ces modifications.
- 2026-09-02 : la variante « six perles » est refusée car trop proche des hublots.
- 2026-09-02 : plusieurs tentatives d’échelle sont refusées : soit le rendu ressemble à des rectangles, soit le programme devient trop long et difficile à se représenter mentalement.
- 2026-09-02 : utilisateur précise que des instructions peuvent être placées avant/après le motif répété ; l’élève peut avoir à distinguer ce qui appartient au motif de ce qui reste hors répétition.
- 2026-09-02 : utilisateur demande d’abandonner les projets Vittascience pour 180 et de fournir uniquement le code Python.
- 2026-09-02 : variante « vague / serpent » validée comme nouvelle direction pour 180 ; motif `circle(25, 180)` → `circle(-25, 180)` répété quatre fois.

## Validations utilisateur

- Cadrage : validé pour la déclinaison
- Variante pilote 10 : validée
- Déclinaison 11-12/179-180 : à reviewer
- Variante 180 : à revalider après réécriture en serpent ondulé
- Review finale : non validée
- Passage testing : non validé
