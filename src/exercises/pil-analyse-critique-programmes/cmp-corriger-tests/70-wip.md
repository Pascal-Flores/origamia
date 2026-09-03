# Reprise des variantes 6e — corriger un programme

## Gate 0 - Workflow

- Workflow relu : oui
- Date de relecture : 2026-09-03
- Représentation(s) autorisée(s) pour cette série : programme fautif complet en blocs textuels pris en charge par le projet, texte à trous avec fragments de correction en langage naturel.
- Représentation(s) interdites : texte qui se contente de nommer une erreur, correction portant sur une syntaxe de boucle sans lien clair avec le résultat final, formulation télégraphique.
- Décision : review et harmonisation de 219 et 220 autorisées à la demande explicite de l'utilisateur.

## Attendu

- Compétence : `cmp-corriger-tests`.
- Attendu : `att-corriger-tests-6e`.
- Variantes de référence : 70, 71, 72.
- Variantes reprises : 219 et 220.

## Forme de référence

Les variantes 70–72 utilisent toutes :

1. une mission comportant plusieurs critères ;
2. un dispositif réellement programmable ;
3. un programme dont deux éléments produisent un résultat incorrect tandis qu'au moins un élément est déjà correct ;
4. un texte à trois trous : première correction, seconde correction, résultat obtenu après correction ;
5. six étiquettes environ, avec trois réponses correctes et des distracteurs ;
6. `type: ddt`, `essais: 3`, puis deux feedbacks progressifs et un feedback final explicatif.

## Reprise réalisée

### 219

- Situation : `rit-sechauffer-avant-activite`.
- Un minuteur programmable doit utiliser une durée de `5 minutes`, afficher `PRÊT` et allumer un voyant bleu.
- Dans le programme fautif, la durée et le message sont incorrects tandis que le voyant est déjà correct.
- Le texte à trous demande la durée corrigée, le message corrigé et le résultat global obtenu.
- L'ancienne version centrée sur une boucle de répétition a été supprimée pour éviter un glissement vers la compétence sur les répétitions.

### 220

- Situation : `rit-ouvrir-appli-fermer-correctement`, rituel existant qui n'est utilisé par aucun autre exercice du corpus vérifié.
- Un script de tablette doit ouvrir l'application `Dessin` pendant `10 secondes`, la fermer puis afficher `DÉMONSTRATION TERMINÉE`.
- Dans le programme fautif, l'application ouverte et le message final sont incorrects ; la durée et la fermeture sont déjà correctes.
- Le texte à trous demande l'application corrigée, le message corrigé et le résultat global obtenu.
- L'ancienne version ne comportait que deux instructions inversées et une seule correction réelle ; elle était nettement plus simple que les autres variantes 6e.

## Review

Verdict : **OK**.

- 219 et 220 suivent désormais la même structure que 70–72 : mission multicritère, deux corrections indépendantes, éléments déjà corrects, puis résultat global.
- Les deux exercices sont en `type: ddt` avec `essais: 3`.
- Chaque exercice propose six étiquettes, dont trois constituent la solution `1, 2, 3`.
- Les feedbacks distinguent d'abord les critères déjà corrects des deux éléments à modifier, puis explicitent le résultat final.
- Les dispositifs décrits sont réellement programmables ou scriptables.
- 219 et 220 restent en `wip`.
- Aucun build ni import SQLite n'est revendiqué.

## Validations utilisateur

- Cadrage : validé par les demandes successives de reprise
- Variante pilote : 70 sert de référence existante
- Déclinaison : réalisée pour 219–220
- Review finale : à valider par l'utilisateur
- Passage testing : non validé
