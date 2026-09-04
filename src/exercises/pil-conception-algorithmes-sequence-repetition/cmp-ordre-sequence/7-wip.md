# Reprise de la série cmp-ordre-sequence - exercices 7 à 9, 149 et 150

## Gate 0 - Workflow

- Workflow relu : oui
- Date de relecture : 2026-09-01
- Représentation(s) autorisée(s) pour cette série : interface Turtle Vittascience avec blocs fournis ; projet solution Vittascience et solution Python conservés comme aides de fabrication.
- Représentation(s) interdite(s) pour cette série : paramétrage demandé à l'élève ; valeurs hors valeurs par défaut lorsqu'elles obligent l'élève à modifier un bloc ; pseudo-code inventé à la place de l'interface.
- Décision : review autorisée sur les deux variantes supplémentaires 149 et 150 ; les exercices historiques 7 à 9 servent de gabarit de forme.

## Attendu

- Compétence : `cmp-ordre-sequence`
- Attendu : `att-ordre-sequence-6e`
- Geste : construire un programme Turtle en ordonnant des blocs fournis et déjà paramétrés pour obtenir une figure cible.

## Forme invariante

- Type : `interface`.
- Canvas élève vide en mode exercice.
- Les blocs utiles sont fournis dans la toolbox ; l'élève les assemble uniquement.
- Les paramètres sont déjà corrects et utilisent les valeurs par défaut des blocs Vittascience.
- Le nombre de blocs peut dépasser 8 si cela permet d'obtenir une figure nettement plus reconnaissable ; le nombre d'instructions ne doit pas être réduit au détriment de la lisibilité de la cible.
- La figure cible doit être immédiatement reconnaissable et nommée dans l'énoncé.
- Les variantes doivent produire des figures réellement différentes.
- La mise en situation doit expliquer naturellement pourquoi cette figure est tracée ; ne pas plaquer un rituel sans rapport avec le dessin.
- Si aucun rituel existant n'est pertinent, une mise en situation spécifique peut être créée pour l'exercice, à condition qu'elle reste concrète et n'introduise aucune compétence externe nécessaire à la réussite.

## Retours utilisateur

- 2026-09-01 : les blocs doivent utiliser leurs valeurs par défaut ; aucune compétence de paramétrage ne doit être mobilisée.
- 2026-09-01 : le canvas de l'exercice est vide et seuls les blocs nécessaires doivent être disponibles dans la toolbox.
- 2026-09-01 : les figures doivent être reconnaissables ; l'ancienne variante 149 n'était pas assez explicite.
- 2026-09-01 : lorsqu'un projet Vittascience est fourni, il doit reprendre la structure réelle des exports/projets existants du dépôt et les types/champs officiels des blocs Vittascience ; ne pas inventer le format.
- 2026-09-01 : l'appellation « trèfle à quatre feuilles » ne correspond pas assez précisément au tracé de 149 ; utiliser une référence exacte ou expliciter précisément l'analogie.
- 2026-09-01 : pour 149, conserver la rosace et adapter la mise en situation ; une situation pertinente peut être inventée si nécessaire.
- 2026-09-01 : 149 validé ; passage à la variante 150.
- 2026-09-01 : les mises en situation peuvent être inventées si cela permet une meilleure cohérence avec la figure, sans introduire de compétence parasite.
- 2026-09-01 : la première proposition de 150 ne ressemble pas suffisamment à une clé ; il est possible d'utiliser davantage d'instructions pour obtenir une forme clairement reconnaissable.

## Correction de 149 - validée

- Cible : une rosace à quatre cercles.
- Mise en situation : `rit-decorer-affiche-rosace` — la classe prépare une affiche d'exposition et souhaite la décorer avec un motif géométrique.
- Description exacte : quatre cercles identiques partent du même point ; après chaque cercle complet, Turtle tourne de 90° avant de tracer le suivant.
- 8 blocs : quatre `cercle rayon 50` et quatre `tourner à droite de 90°`.
- Toutes les valeurs sont les valeurs par défaut des blocs Turtle Vittascience.
- Projet `149/vittascience.py` fourni avec un workspace Blockly cohérent et le code Python correspondant.

## Proposition révisée de 150

- Cible : un drapeau de départ rectangulaire fixé en haut d'un mât.
- Mise en situation : `rit-preparer-parcours-sport` — préparation d'un petit parcours sportif avec un drapeau pour matérialiser le départ sur le plan.
- Description exacte : un mât vertical de trois segments, puis un rectangle horizontal de deux segments de large et un segment de haut.
- 12 blocs : `gauche 90`, trois `avancer 50`, `droite 90`, deux `avancer 50`, `droite 90`, `avancer 50`, `droite 90`, deux `avancer 50`.
- Toutes les valeurs sont les valeurs par défaut des blocs Turtle Vittascience.
- Figure immédiatement identifiable comme un drapeau et très différente de la rosace 149.
- Projet `150/vittascience.py` fourni avec le workspace Blockly et le code Python correspondant.

## Validations utilisateur

- Cadrage : à revoir
- Variante 149 : validée
- Variante 150 : à revoir
- Déclinaison : à revoir
- Review finale : non valide
- Passage testing : non valide
