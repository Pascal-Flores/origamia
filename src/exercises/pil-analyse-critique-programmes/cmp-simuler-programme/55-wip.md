# Reprise des variantes CM1 — simuler un programme

## Gate 0 - Workflow

- Workflow relu : oui
- Date de relecture : 2026-09-03
- Représentation(s) autorisée(s) pour cette série : grille `robot-grid`, programme de déplacement fourni avec les blocs textuels du projet, réponses en langage naturel.
- Représentation(s) interdites : comptage d'objets, états de bacs ou de collections, syntaxe nouvelle, écriture libre du programme.
- Décision : review et réalignement des variantes 209 et 210 sur la forme déjà validée des exercices 55 à 57.

## Attendu

- Compétence : `cmp-simuler-programme`.
- Attendu : `att-simuler-programme-cm1`.
- Variantes concernées : 55, 56, 57, 209 et 210.

## Constat

Les variantes 55, 56 et 57 suivent une même forme : un robot part d'une case et d'une orientation indiquées sur une grille, exécute trois instructions de déplacement, puis l'élève choisit la case colorée atteinte.

Les variantes 209 et 210 s'écartaient de cette forme : elles demandaient de compter des objets après une suite d'actions. Elles ne travaillaient donc pas le même geste de simulation que les autres variantes du même attendu.

## Forme retenue

Les variantes 209 et 210 reprennent exactement la matrice des exercices 55 à 57 :

1. contexte court mettant en scène un robot mobile ;
2. grille `5x4` avec case de départ, orientation et trois cases cibles colorées ;
3. programme de trois instructions : avancer, tourner, avancer ;
4. QCU à trois réponses correspondant aux trois cases colorées ;
5. trois essais ;
6. feedback 1 : suivre les instructions une par une ;
7. feedback 2 : guider le trajet sans donner la case finale ;
8. feedback final : expliciter le déplacement complet et la case atteinte.

## Mises en situation

- 209 conserve `rit-debarrasser-trier-dechets`, adapté à un robot de cantine qui transporte un déchet vers une zone de tri.
- 210 conserve `rit-lire-recette-preparer-ingredients`, adapté à un robot de cuisine qui rejoint une zone où sont préparés des ingrédients.
- Les deux slugs ont été recherchés dans le corpus de `main` et ne sont pas utilisés par un autre exercice.

## Validations utilisateur

- Cadrage : validé par le retour demandant explicitement le même format que les autres variantes
- Variante pilote : forme déjà validée par 55 à 57
- Déclinaison : autorisée pour 209 et 210
- Review finale : à valider par l'utilisateur
- Passage testing : non validé pour 209 et 210
