# Reprise de la série CM2 — paramétrer des instructions

## Gate 0 - Workflow

- Workflow relu : oui
- Date de relecture : 2026-09-03
- Représentation(s) autorisée(s) pour cette série : consigne en langage naturel et programmes Blockly textuels déjà pris en charge par le build (`event:`, `move:`, `end:`), fournis à l'élève comme choix.
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
- La variante autour de la partie de ballon améliorait la vraisemblance des paramètres mais n'était pas le contexte souhaité par l'utilisateur.

## Règle de vraisemblance ajoutée

- Ne pas présenter un programme comme réalisant effectivement une action quotidienne s'il ne peut pas réellement la réaliser.
- Dans ces situations, le programme doit être présenté comme une représentation, une traduction ou un support pédagogique qui décrit la procédure ou les règles.
- Exemples de formulations adaptées : « représenter ces consignes sous forme de programme », « traduire les règles avec des blocs », « écrire un programme qui décrit les étapes ».
- Un programme peut être présenté comme réellement exécuté uniquement lorsque le contexte le justifie : robot, Turtle, appareil programmable, affichage, capteur, etc.

## Forme proposée

- Type : `qcu`.
- `essais: 3`.
- Le contexte fournit trois paramètres explicites liés à une procédure réelle.
- Le programme est présenté comme une représentation de cette procédure, pas comme un outil utilisé pour accomplir le geste quotidien.
- Quatre programmes complets sont proposés.
- Chaque programme contient les mêmes actions dans le même ordre, avec des valeurs de paramètres différentes.
- Un seul programme respecte simultanément les trois informations fournies.
- L'élève doit donc vérifier plusieurs paramètres dans un même programme.
- Les distracteurs changent uniquement les valeurs des paramètres afin de ne pas glisser vers `cmp-ordre-sequence` ou `cmp-identifier-erreurs`.
- Aucun calcul ni savoir extérieur n'est nécessaire.

## Nouveau pilote 22

- Rituel rétabli à la demande de l'utilisateur : `rit-laver-mains-avant-manger`.
- Situation : près du lavabo, une affiche indique la procédure à suivre avant d'aller manger.
- Trois informations de l'affiche sont reprises comme paramètres : `1` dose de savon, `20 secondes` de frottage et `1` feuille d'essuie-mains pour se sécher.
- Statut du programme : en classe, on cherche à représenter cette procédure avec des blocs. Le programme ne lave pas les mains ; il décrit la procédure affichée.
- Quatre propositions contiennent les mêmes étapes ; une seule reprend correctement les trois paramètres.

## Déclinaison prévue après validation

- 23, 24, 187 et 188 devront chacun partir d'une situation où plusieurs paramètres sont naturels dans l'activité.
- Avant chaque choix de rituel : vérifier le slug exact et les doublons sémantiques avec les exercices existants.
- Pour chaque variante, expliciter pourquoi un programme apparaît dans la situation : représentation d'une procédure, exercice de traduction algorithmique ou programme réellement exécutable si le contexte le permet.

## Retours utilisateur pris en compte

- 2026-09-03 : les exercices 22–24, 187 et 188 sont jugés peu intéressants pédagogiquement et plus faciles que les exercices CM1.
- 2026-09-03 : la première refonte du 22 est jugée trop artificielle et peu signifiante.
- 2026-09-03 : précision utilisateur sur le problème de formulation : dans une situation comme le lavage des mains, le programme ne doit pas être présenté comme un programme réellement utilisé pour laver les mains ; il peut en revanche représenter ou montrer la procédure.
- 2026-09-03 : demande explicite de revenir au lavage des mains pour le pilote 22, qui était le contexte d'origine.

## Validations utilisateur

- Diagnostic : issu du retour utilisateur
- Nouvelle forme CM2 : à reviewer
- Contexte lavage des mains : retenu explicitement par l'utilisateur
- Nouveau pilote 22 : à reviewer après réécriture dans ce contexte
- Déclinaison 23-24/187-188 : non validée
- Review finale : non validée
- Passage testing : non validé
