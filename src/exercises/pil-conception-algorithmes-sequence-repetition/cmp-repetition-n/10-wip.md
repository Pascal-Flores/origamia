# Reprise de la série cmp-repetition-n — exercices 10 à 12, 179 et 180

## Gate 0 - Workflow

- Workflow relu : oui
- Date de relecture : 2026-09-02
- Représentation(s) autorisée(s) pour cette série : programme Turtle Vittascience entièrement développé, sans boucle, présenté à l’élève comme support d’observation ; paramètres déjà fixés dans les blocs.
- Représentation(s) interdites pour cette série : demander à l’élève de paramétrer les blocs ; introduire une boucle dans le programme observé ; utiliser cinq polygones réguliers ou des formes abstraites difficiles à reconnaître.
- Décision : déclinaison autorisée après validation explicite du pilote 10 par l’utilisateur.

## Attendu

- Compétence : `cmp-repetition-n`
- Attendu : `att-repetition-n-cm1`
- Geste travaillé : déterminer combien de fois un motif d’instructions est répété dans un programme.
- Série concernée : 10, 11, 12, 179, 180.

## Forme invariante

- Type : `free`.
- Support : interface Turtle montrant un programme entièrement développé, sans boucle.
- Le programme produit une forme immédiatement reconnaissable et nommée dans le contexte.
- Un même groupe d’instructions apparaît plusieurs fois à l’identique.
- Consigne identique : « Combien de fois ce morceau est-il répété ? Écris uniquement le nombre. »
- Réponse attendue : un entier.
- `essais: 2`.
- Feedback essai 1 : aide à repérer les limites du motif sans donner le nombre.
- Feedback final : indique le nombre de répétitions et montre le motif répété.
- Les paramètres Turtle sont déjà fixés ; l’élève n’a rien à modifier. Ils peuvent varier entre variantes puisque la tâche consiste uniquement à observer le programme.
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

- Cible : échelle clairement reconnaissable avec deux montants verticaux qui dépassent au-dessus et au-dessous des barreaux.
- Situation : `rit-dessiner-pictogramme-echelle`.
- Motif observé : `avancer 80` → `reculer 80`.
- Répétitions : 6.
- Le programme trace d’abord séparément les deux montants, de `y = -110` à `y = 110`, aux abscisses `x = 0` et `x = 80`.
- Les six barreaux sont placés aux hauteurs `-80`, `-48`, `-16`, `16`, `48` et `80`.
- Entre deux barreaux, Turtle lève le stylo, se replace au montant gauche puis rebaisse le stylo : aucun segment parasite n’est tracé pendant le repositionnement.
- Programme : 38 blocs au total.
- `vittascience.py` utilise uniquement des structures déjà présentes dans les projets fonctionnels de la série : `turtle_direction`, `turtle_goto` et `turtle_pen`. Aucun nouveau format de bloc n’est inventé.

## Retours utilisateur pris en compte

- Les anciens triangle/carré/hexagone/pentagone/octogone étaient trop répétitifs.
- Les formes doivent être immédiatement reconnaissables.
- Les projets `.py` Vittascience doivent reprendre la structure réelle d’un export importable et les types/champs officiels des blocs.
- Les mises en situation peuvent être inventées si cela évite de plaquer un rituel sans rapport avec le dessin.
- 2026-09-02 : utilisateur autorise explicitement la déclinaison des variantes 11, 12, 179 et 180 à partir du pilote 10.
- 2026-09-02 : utilisateur modifie les nombres de répétitions et certains paramètres de tracé afin d’éviter une série trop homogène ; conserver ces modifications.
- 2026-09-02 : les premières générations de `180/vittascience.py` échouent dans Vittascience avec `textToDom was unable to parse` ; ne plus fabriquer ce projet à partir d'un XML écrit à la main sans reprendre les structures de blocs validées dans les projets fonctionnels du dépôt.
- 2026-09-02 : la variante « six perles » est refusée car trop proche des hublots ; conserver l’échelle comme cible visuelle.
- 2026-09-02 : le premier rendu de l’échelle ressemblait à une colonne de rectangles empilés. Correction demandée : tracer les montants séparément, déplacer Turtle stylo levé entre les barreaux et faire dépasser les montants en haut et en bas afin que la silhouette soit immédiatement identifiable comme une échelle.

## Validations utilisateur

- Cadrage : validé pour la déclinaison
- Variante pilote 10 : validée
- Déclinaison 11-12/179-180 : à reviewer
- Variante 180 : à revalider après nouveau projet Turtle
- Review finale : non validée
- Passage testing : non validé
