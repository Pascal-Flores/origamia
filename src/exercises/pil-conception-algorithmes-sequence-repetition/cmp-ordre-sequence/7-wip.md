# Reprise de la série cmp-ordre-sequence - exercices 7 à 9, 177 et 178

## Gate 0 - Workflow

- Workflow relu : oui
- Date de relecture : 2026-09-01
- Représentation(s) autorisée(s) pour cette série : interface Turtle Vittascience avec blocs fournis ; projet solution Vittascience et solution Python conservés comme aides de fabrication.
- Représentation(s) interdite(s) pour cette série : paramétrage demandé à l'élève ; valeurs hors valeurs par défaut lorsqu'elles obligent l'élève à modifier un bloc ; pseudo-code inventé à la place de l'interface.
- Décision : review autorisée sur les deux variantes supplémentaires 177 et 178 ; les exercices historiques 7 à 9 servent de gabarit de forme.

## Attendu

- Compétence : `cmp-ordre-sequence`
- Attendu : `att-ordre-sequence-6e`
- Geste : construire un programme Turtle en ordonnant exactement 8 blocs fournis et déjà paramétrés.

## Forme invariante

- Type : `interface`.
- Canvas élève vide en mode exercice.
- Les blocs utiles sont fournis dans la toolbox ; l'élève les assemble uniquement.
- Les paramètres sont déjà corrects.
- Exactement 8 instructions dans la solution.
- La figure cible doit être immédiatement reconnaissable et nommée dans l'énoncé.
- Les variantes doivent produire des figures réellement différentes.

## Retours utilisateur

- 2026-09-01 : les blocs doivent utiliser leurs valeurs par défaut ; aucune compétence de paramétrage ne doit être mobilisée.
- 2026-09-01 : le canvas de l'exercice est vide et seuls les blocs nécessaires doivent être disponibles dans la toolbox.
- 2026-09-01 : les figures doivent être reconnaissables ; l'ancienne variante 177 n'était pas assez explicite.
- 2026-09-01 : lorsqu'un projet Vittascience est fourni, il doit reprendre la structure réelle des exports/projets existants du dépôt et les types/champs officiels des blocs Vittascience ; ne pas inventer le format.
- 2026-09-01 : l'appellation « trèfle à quatre feuilles » ne correspond pas assez précisément au tracé de 177 ; utiliser une référence exacte ou expliciter précisément l'analogie.

## Correction de 177

- Nouvelle cible : une rosace à quatre cercles.
- Description exacte : quatre cercles identiques partent du même point ; après chaque cercle complet, Turtle tourne de 90° avant de tracer le suivant.
- 8 blocs : quatre `cercle rayon 50` et quatre `tourner à droite de 90°`.
- Toutes les valeurs sont les valeurs par défaut des blocs Turtle Vittascience.
- Projet `177/vittascience.py` fourni avec un workspace Blockly cohérent et le code Python correspondant.

## Validations utilisateur

- Cadrage : à revoir
- Variante pilote : à revoir
- Déclinaison : à revoir
- Review finale : non valide
- Passage testing : non valide
