# Reprise de la série CM2 — paramétrer des instructions

## Gate 0 - Workflow

- Workflow relu : oui
- Date de relecture : 2026-09-03
- Représentation(s) autorisée(s) pour cette série : consigne en langage naturel et instructions Blockly textuelles déjà prises en charge par le build (`move:`), fournies à l'élève comme éléments déjà écrits puis rendues visuellement sous forme de blocs Blockly.
- Représentation(s) interdites pour cette série : saisie libre de blocs, calcul nécessaire pour retrouver un paramètre, information implicite à connaître, syntaxe inventée, valeurs artificiellement ajoutées à un rituel uniquement pour fabriquer des paramètres, mise en situation où un programme est présenté comme exécutant réellement un geste ordinaire alors qu'il sert seulement à représenter une procédure.
- Décision : déclinaison autorisée après validation explicite du pilote 22. Réécrire 23, 24, 159 et 160 selon la même forme didactique.

## Attendu

- Compétence : `cmp-parametrer-instructions`.
- Attendu : `att-parametrer-instructions-cm2`.
- Intitulé du référentiel : « Vérifier si un paramètre proposé dans un programme respecte la consigne. »
- Indicateur acquis : gérer correctement 2 à 3 paramètres et respecter les contraintes données.
- Exercices concernés : 22, 23, 24, 159 et 160.

## Diagnostic des exercices précédents

- Les anciennes variantes CM2 reposaient sur un QCU vrai/faux à un seul paramètre.
- Le plus souvent, l'élève comparait directement deux valeurs déjà visibles dans l'énoncé.
- Cette tâche était plus simple que les variantes CM1, où l'élève doit identifier la bonne information parmi plusieurs données puis renseigner un paramètre manquant.
- La variante avec quatre programmes complets obligeait l'élève à choisir quelle proposition représentait correctement toute la procédure. Cette forme chevauchait trop la compétence de comparaison/association de représentations.

## Règle de vraisemblance

- Ne pas présenter un programme comme réalisant effectivement une action quotidienne s'il ne peut pas réellement la réaliser.
- Dans ces situations, les blocs sont présentés comme une représentation, une traduction ou un support pédagogique qui décrit une procédure, une fiche ou un planning.
- Un programme peut être présenté comme réellement exécuté uniquement lorsque le contexte le justifie : robot, Turtle, appareil programmable, affichage, capteur, etc.

## Règle de formulation liée au rendu Blockly

- Le DSL textuel (`move:`, parenthèses autour des valeurs, etc.) est une représentation interne destinée au build.
- L'élève voit les éléments sous forme de blocs Blockly et ne voit donc pas nécessairement les parenthèses ni la syntaxe source.
- Les consignes et feedbacks ne doivent jamais demander de « regarder le nombre entre parenthèses » ou se référer à un signe de ponctuation du DSL.
- Employer des formulations compatibles avec le rendu final : « la valeur indiquée dans le bloc », « le paramètre du bloc », « la durée indiquée », « la quantité indiquée ».

## Forme validée

- Type : `qcm`.
- `essais: 3`.
- Le contexte fournit trois paramètres explicites et naturels dans la situation.
- Trois instructions indépendantes sont proposées, avec trois actions différentes et déjà correctes.
- Chaque instruction contient un seul paramètre déjà renseigné.
- L'élève sélectionne toutes les instructions dont le paramètre respecte la consigne.
- La tâche porte exclusivement sur la valeur du paramètre : pas de comparaison de programmes complets, pas d'ordre à juger et pas de conversion entre représentations.
- Les actions des blocs reprennent directement les informations du contexte afin que l'association action ↔ information ne constitue pas une difficulté autonome.
- Deux blocs sont corrects et un bloc est incorrect ; la position du bloc incorrect varie entre les variantes.
- Aucun calcul ni savoir extérieur n'est nécessaire.

## Pilote 22 validé

- Rituel : `rit-laver-mains-avant-manger`.
- Situation : une affiche indique `1` dose de savon, `20 secondes` de frottage et `1` feuille d'essuie-mains.
- Statut des blocs : un élève a commencé à traduire certaines étapes de l'affiche en instructions de programme ; les actions sont déjà correctes, seuls les paramètres sont à vérifier.
- Trois instructions indépendantes ; solution : blocs 1 et 3.
- Le texte élève ne fait aucune référence aux parenthèses du DSL.

## Déclinaison autorisée

### 23 — salade de fruits

- Rituel conservé : `rit-preparer-salade-fruits`.
- Vérification d'usage : le slug apparaît dans l'exercice 23 existant et dans le référentiel, sans autre exercice trouvé lors de la recherche.
- Fiche recette : `2` pommes, `1` poire, `3` clémentines.
- Trois blocs indépendants de type `AJOUTER` ; le bloc sur les pommes porte une mauvaise quantité.
- Solution prévue : 2, 3.

### 24 — chasse au trésor

- Nouveau rituel : `rit-organiser-chasse-tresor`.
- Vérification d'usage : aucun autre exercice trouvé avec ce slug lors de la recherche ; seule la ligne du référentiel est retournée.
- Fiche d'organisation : `6` indices, `2` équipes, durée `20 minutes`.
- Trois blocs indépendants ; le bloc sur la durée porte une mauvaise valeur.
- Solution prévue : 1, 2.

### 159 — carnet de lecture

- Nouveau rituel : `rit-tenir-carnet-lecture`.
- Vérification d'usage : aucun autre exercice trouvé avec ce slug lors de la recherche ; seule la ligne du référentiel est retournée.
- Fiche de suivi : page `48`, avis `4/5`, `2` mots nouveaux.
- Trois blocs indépendants ; le bloc sur l'avis porte une mauvaise valeur.
- Solution prévue : 1, 3.

### 160 — devoirs avec pause

- Nouveau rituel : `rit-faire-devoirs-avec-pause`.
- Vérification d'usage : aucun autre exercice trouvé avec ce slug lors de la recherche ; seule la ligne du référentiel est retournée.
- Planning : mathématiques `20 minutes`, pause `5 minutes`, lecture `15 minutes`.
- Trois blocs indépendants ; le bloc sur les mathématiques porte une mauvaise durée.
- Solution prévue : 2, 3.

## Retours utilisateur pris en compte

- 2026-09-03 : les exercices 22–24, 159 et 160 sont jugés peu intéressants pédagogiquement et plus faciles que les exercices CM1.
- 2026-09-03 : dans une situation comme le lavage des mains, le programme ne doit pas être présenté comme un programme réellement utilisé pour accomplir le geste ; il peut représenter ou montrer la procédure.
- 2026-09-03 : les programmes complets sont jugés trop proches d'une tâche de comparaison de représentations ; préférence pour des instructions uniques afin de cibler directement la vérification des paramètres.
- 2026-09-03 : les blocs étant rendus sous forme de blocs Blockly, ne pas parler aux élèves de « parenthèses » présentes uniquement dans la syntaxe source.
- 2026-09-03 : validation explicite du pilote 22 (« oui là c'est bon ») et autorisation de produire les autres exercices.

## Validations utilisateur

- Diagnostic : validé par les retours utilisateur
- Contexte lavage des mains : validé
- Forme « instructions indépendantes » : validée
- Variante pilote 22 : validée
- Déclinaison 23-24/159-160 : autorisée, à reviewer après rédaction
- Review finale : non validée
- Passage testing : non validé
