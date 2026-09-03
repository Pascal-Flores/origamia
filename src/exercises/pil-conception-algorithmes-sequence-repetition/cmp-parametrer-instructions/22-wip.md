# Reprise de la série CM2 — paramétrer des instructions

## Gate 0 - Workflow

- Workflow relu : oui
- Date de relecture : 2026-09-03
- Représentation(s) autorisée(s) pour cette série : consigne en langage naturel et programmes Blockly textuels déjà pris en charge par le build (`event:`, `move:`, `end:`), fournis à l'élève comme choix.
- Représentation(s) interdites pour cette série : saisie libre de blocs, calcul nécessaire pour retrouver un paramètre, information implicite à connaître, syntaxe inventée, valeurs artificiellement ajoutées à un rituel uniquement pour fabriquer des paramètres.
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
- La première refonte du 22, fondée sur trois instructions isolées à classer et sur des durées de lavage des mains, augmentait bien le nombre de paramètres mais restait artificielle : la situation avait été construite pour justifier les paramètres au lieu de partir de paramètres naturellement présents dans le rituel.

## Nouvelle forme proposée

- Type : `qcu`.
- `essais: 3`.
- Le contexte décrit une situation dans laquelle trois paramètres existent naturellement et sont explicitement décidés avant l'exécution.
- Quatre programmes complets sont proposés.
- Chaque programme contient les trois mêmes instructions, avec des valeurs de paramètres différentes.
- Un seul programme respecte simultanément les trois contraintes.
- L'élève doit donc vérifier plusieurs paramètres dans un même programme, et non répondre à trois micro-questions indépendantes.
- Les distracteurs changent uniquement les valeurs des paramètres ; les actions et leur ordre restent identiques afin de ne pas glisser vers `cmp-ordre-sequence` ou `cmp-identifier-erreurs`.
- Aucun calcul n'est nécessaire.
- Les cinq variantes conserveront cette structure ; seuls la situation et les paramètres changeront.

## Nouveau pilote 22

- Ancien rituel `rit-laver-mains-avant-manger` abandonné pour cette série : les durées ajoutées au lavage des mains rendaient l'énoncé artificiel.
- Nouveau rituel : `rit-organiser-partie-ballon`.
- Vérification d'usage : le slug n'apparaît dans aucun exercice existant lors de la recherche ; il est seulement présent dans le référentiel des rituels.
- Situation : pendant une récréation, le groupe se met d'accord sur les règles pratiques de la partie avant de commencer.
- Paramètres naturellement présents : `2` équipes, `4` joueurs par équipe, `10` minutes de jeu.
- Quatre programmes proposent les mêmes trois actions : former les équipes, répartir les joueurs, lancer la partie pour une durée donnée.
- Un seul reprend correctement les trois valeurs.

## Déclinaison prévue après validation

- 23, 24, 187 et 188 devront chacun partir d'une situation où plusieurs paramètres sont déjà naturels dans l'activité, pas d'une liste de valeurs fabriquée pour l'exercice.
- Avant chaque choix de rituel : vérifier le slug exact et les doublons sémantiques avec les exercices existants.
- Les situations de recette, de réglage ou de matériel ne seront conservées que si les trois paramètres ont une fonction crédible dans la situation.

## Retours utilisateur pris en compte

- 2026-09-03 : les exercices 22–24, 187 et 188 sont jugés peu intéressants pédagogiquement et plus faciles que les exercices CM1. Demande : soit les rendre réellement CM2, soit les basculer en CM1 avec une refonte pédagogique.
- 2026-09-03 : la première refonte du 22 est jugée trop artificielle et peu signifiante. Le problème vient notamment du fait que la situation est formulée comme une « fiche de réglages » et que des paramètres peu naturels sont ajoutés au lavage des mains.
- Décision de conception : conserver le niveau CM2, mais faire porter la difficulté sur la vérification simultanée de trois paramètres naturellement présents dans une situation concrète.

## Validations utilisateur

- Diagnostic : issu du retour utilisateur
- Nouvelle forme CM2 : à reviewer
- Nouveau pilote 22 : à reviewer après seconde refonte
- Déclinaison 23-24/187-188 : non validée
- Review finale : non validée
- Passage testing : non validé
