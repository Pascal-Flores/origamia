# Reprise de la série CM2 — paramétrer des instructions

## Gate 0 - Workflow

- Workflow relu : oui
- Date de relecture : 2026-09-03
- Représentation(s) autorisée(s) pour cette série : consigne en langage naturel et instructions Blockly textuelles déjà prises en charge par le build (`move:`), fournies à l'élève comme éléments déjà écrits puis rendues visuellement sous forme de blocs Blockly.
- Représentation(s) interdites pour cette série : saisie libre de blocs, calcul nécessaire pour retrouver un paramètre, information implicite à connaître, syntaxe inventée, valeurs artificiellement ajoutées à un rituel uniquement pour fabriquer des paramètres, mise en situation où un programme est présenté comme exécutant réellement un geste ordinaire alors qu'il sert seulement à représenter une procédure.
- Décision : reprendre le cadrage CM2 et réécrire d'abord l'exercice 22 comme pilote. Les exercices 23, 24, 187 et 188 ne seront déclinés qu'après validation explicite du nouveau pilote 22.

## Attendu

- Compétence : `cmp-parametrer-instructions`.
- Attendu : `att-parametrer-instructions-cm2`.
- Intitulé du référentiel : « Vérifier si un paramètre proposé dans un programme respecte la consigne. »
- Indicateur acquis : gérer correctement 2 à 3 paramètres et respecter les contraintes données.
- Exercices concernés à terme : 22, 23, 24, 187 et 188.

## Diagnostic des exercices précédents

- Les anciennes variantes CM2 reposaient sur un QCU vrai/faux à un seul paramètre.
- Le plus souvent, l'élève comparait directement deux valeurs déjà visibles dans l'énoncé.
- Cette tâche était plus simple que les variantes CM1, où l'élève doit identifier la bonne information parmi plusieurs données puis renseigner un paramètre manquant.
- La première refonte du 22 augmentait bien le nombre de paramètres mais introduisait des valeurs peu naturelles et formulait mal le rôle du programme.
- La variante avec quatre programmes complets obligeait l'élève à choisir quelle proposition représentait correctement toute la procédure. Cette forme chevauche trop la compétence de comparaison/association de représentations.

## Règle de vraisemblance

- Ne pas présenter un programme comme réalisant effectivement une action quotidienne s'il ne peut pas réellement la réaliser.
- Dans ces situations, le programme doit être présenté comme une représentation, une traduction ou un support pédagogique qui décrit la procédure ou les règles.
- Un programme peut être présenté comme réellement exécuté uniquement lorsque le contexte le justifie : robot, Turtle, appareil programmable, affichage, capteur, etc.

## Règle de formulation liée au rendu Blockly

- Le DSL textuel (`move:`, parenthèses autour des valeurs, etc.) est une représentation interne destinée au build.
- L'élève voit les éléments sous forme de blocs Blockly et ne voit donc pas nécessairement les parenthèses ni la syntaxe source.
- Les consignes et feedbacks ne doivent jamais demander de « regarder le nombre entre parenthèses » ou se référer à un signe de ponctuation du DSL.
- Employer à la place des formulations visibles dans le rendu final : « la valeur indiquée dans le bloc », « le paramètre du bloc », « la durée indiquée », « la quantité indiquée ».

## Forme proposée après le dernier retour

- Type : `qcm`.
- `essais: 3`.
- Le contexte fournit trois paramètres explicites liés à une procédure réelle.
- Trois instructions **indépendantes** sont proposées, avec trois actions différentes et déjà correctes.
- Chaque instruction contient un seul paramètre déjà renseigné.
- L'élève sélectionne toutes les instructions dont le paramètre respecte la consigne.
- La tâche porte exclusivement sur la valeur du paramètre : il n'y a pas à comparer deux programmes complets, à juger l'ordre des actions ni à choisir entre plusieurs représentations globales d'une même procédure.
- Les actions des instructions reprennent directement celles de la consigne afin que l'association action ↔ information soit évidente et ne constitue pas une difficulté autonome.
- Sur les trois paramètres, au moins un est incorrect et au moins un est correct.
- Aucun calcul ni savoir extérieur n'est nécessaire.

## Nouveau pilote 22

- Rituel : `rit-laver-mains-avant-manger`.
- Situation : près du lavabo, une affiche indique `1` dose de savon, `20 secondes` de frottage et `1` feuille d'essuie-mains.
- Statut du programme : un élève a commencé à traduire quelques étapes de l'affiche en instructions de programme. Les actions sont déjà correctes ; seuls les paramètres doivent être vérifiés.
- Trois instructions indépendantes :
  - `PRENDRE (1) dose de savon` : correcte ;
  - `FROTTER pendant (15) secondes` : incorrecte ;
  - `PRENDRE (1) feuille d'essuie-mains` : correcte.
- Consigne attendue côté élève : sélectionner toutes les instructions dont le paramètre correspond à l'affiche, sans référence aux parenthèses ou à la syntaxe textuelle utilisée par le build.

## Déclinaison prévue après validation

- 23, 24, 187 et 188 devront conserver exactement cette forme : trois instructions indépendantes, chacune portant un paramètre à vérifier.
- Chaque situation devra rendre les paramètres naturels et crédibles.
- Avant chaque choix de rituel : vérifier le slug exact et les doublons sémantiques avec les exercices existants.
- Pour chaque variante, expliciter pourquoi les instructions apparaissent sous forme de programme sans prétendre qu'un programme exécute réellement le geste quotidien.
- Tous les textes destinés à l'élève doivent être rédigés en fonction du rendu Blockly final, jamais en fonction de la syntaxe DSL source.

## Retours utilisateur pris en compte

- 2026-09-03 : les exercices 22–24, 187 et 188 sont jugés peu intéressants pédagogiquement et plus faciles que les exercices CM1.
- 2026-09-03 : la première refonte du 22 est jugée trop artificielle et peu signifiante.
- 2026-09-03 : dans une situation comme le lavage des mains, le programme ne doit pas être présenté comme un programme réellement utilisé pour laver les mains ; il peut en revanche représenter ou montrer la procédure.
- 2026-09-03 : demande explicite de revenir au lavage des mains pour le pilote 22.
- 2026-09-03 : les programmes complets sont jugés trop proches d'une tâche de comparaison de représentations ; préférence pour des instructions uniques afin de cibler directement la vérification des paramètres.
- 2026-09-03 : les blocs étant rendus sous forme de blocs Blockly, ne pas parler aux élèves de « parenthèses » présentes uniquement dans la syntaxe source.

## Validations utilisateur

- Diagnostic : issu du retour utilisateur
- Contexte lavage des mains : retenu explicitement par l'utilisateur
- Forme « instructions indépendantes » : direction explicitement demandée par l'utilisateur
- Nouveau pilote 22 : à reviewer après correction des formulations liées au rendu Blockly
- Déclinaison 23-24/187-188 : non validée
- Review finale : non validée
- Passage testing : non validé
