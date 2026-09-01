# Reprise de la série cmp-repetition-n — exercices 10 à 12, 179 et 180

## Gate 0 - Workflow

- Workflow relu : oui
- Date de relecture : 2026-09-01
- Représentation(s) autorisée(s) pour cette série : programme Turtle Vittascience entièrement développé, sans boucle, présenté à l’élève comme support d’observation ; valeurs par défaut des blocs Turtle.
- Représentation(s) interdites pour cette série : demander à l’élève de paramétrer les blocs ; introduire une boucle dans le programme observé ; utiliser cinq polygones réguliers ou des formes abstraites difficiles à reconnaître.
- Décision : cadrage et variante pilote 10. Les variantes 11, 12, 179 et 180 ne sont pas modifiées avant validation explicite du pilote.

## Attendu

- Compétence : `cmp-repetition-n`
- Attendu : `att-repetition-n-cm1`
- Geste travaillé : déterminer combien de fois un motif d’instructions est répété dans un programme.
- Série concernée : 10, 11, 12, 179, 180.

## Forme invariante proposée

- Type : `free`.
- Support : interface Turtle montrant un programme entièrement développé, sans boucle.
- Le programme produit une forme immédiatement reconnaissable et nommée dans le contexte.
- Un même groupe d’instructions apparaît plusieurs fois à l’identique.
- Consigne identique : « Combien de fois ce morceau est-il répété ? Écris uniquement le nombre. »
- Réponse attendue : un entier.
- `essais: 2`.
- Feedback essai 1 : aide à repérer les limites du motif sans donner le nombre.
- Feedback final : indique le nombre de répétitions et montre le motif répété.
- Les blocs Turtle utilisent leurs valeurs par défaut ; l’élève n’a rien à paramétrer.

## Pilote 10 proposé

- Cible visuelle : un escalier simplifié de trois marches.
- Mise en situation : `rit-dessiner-pictogramme-escalier` — dessiner un pictogramme simple d’escalier pour signaler l’accès à l’étage.
- Motif : `avancer 50` → `tourner à gauche de 90°` → `avancer 50` → `tourner à droite de 90°`.
- Répétitions : 3.
- Programme développé : 12 blocs.
- Valeurs : uniquement `50` et `90°`, valeurs par défaut Vittascience.

## Pistes pour les quatre variantes suivantes

Les formes devront rester reconnaissables et différentes, tout en conservant exactement la même interaction pédagogique : observer un programme développé et compter le motif répété. Exemples à valider après le pilote : frise de créneaux, rangée de ronds, peigne, motif de marches inversées. Les formes définitives ne sont pas encore rédigées.

## Validations utilisateur

- Cadrage : à revoir
- Variante pilote 10 : à revoir
- Déclinaison 11-12/179-180 : non validée
- Review finale : non validée
- Passage testing : non validé
