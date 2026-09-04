# Reprise des variantes 6e — simuler un programme

## Gate 0 - Workflow

- Workflow relu : oui
- Date de relecture : 2026-09-03
- Représentation(s) autorisée(s) pour cette série : mission explicite, même programme fourni en blocs textuels (`event:`, `move:`, `say:`, `end:`), quatre états initiaux en langage naturel ou sur grille.
- Représentation(s) interdites : programme réduit à une opération isolée, syntaxe de variable inventée, situation quotidienne artificiellement transformée en programme, tâche qui ne teste qu'une valeur sans état initial complet.
- Décision : review et harmonisation de 185–186 autorisées à la demande explicite de l'utilisateur.

## Attendu

- Compétence : `cmp-simuler-programme`.
- Attendu : `att-simuler-programme-6e`.
- Variantes de référence : 61, 62, 63.
- Variantes reprises : 185, 186.

## Forme de référence

Les variantes 61–63 utilisent la même mécanique :

1. une mission définie par un état final précis ;
2. un même programme exécuté dans quatre états initiaux différents ;
3. un véritable robot, appareil ou dispositif programmable ;
4. l'élève simule séparément chaque test ;
5. il sélectionne tous les états initiaux qui conduisent à la réussite (`type: qcm`) ;
6. deux tests réussissent et deux échouent ;
7. trois essais avec deux feedbacks progressifs puis un feedback final.

Dans 62–63, le programme modifie seulement une partie de l'état du dispositif : au moins une information reste inchangée et doit donc être correcte dès le départ. Ce mécanisme oblige l'élève à tenir compte de l'état initial complet.

## Problème des versions précédentes de 185–186

Les exercices respectaient formellement « quatre états initiaux + même programme », mais les situations `niveau sonore` et `activité au parc` étaient des situations ordinaires transformées artificiellement en simulations. Elles ne ressemblaient donc pas réellement aux variantes 61–63, qui portent sur des systèmes programmables concrets.

## Nouvelle reprise de 185–186

- 185 : `rit-feu-pieton-programmable`. Le programme force le feu voitures au rouge et le feu piétons au vert, mais ne modifie pas le signal sonore. La mission exige les trois états corrects. Réussites : tests 1 et 4.
- 186 : `rit-barriere-parking-programmable`. Le programme ajoute une place libre, ouvre la barrière et allume le voyant `SORTIE`. La mission impose exactement 5 places libres avec la sortie ouverte. Réussites : tests 1 et 4.
- Les deux situations sont de nouveaux rituels ajoutés au référentiel afin de ne pas réutiliser une mise en situation existante.

## Review

Verdict : **OK**.

- Même structure que 62–63 : mission finale explicite, programme unique, quatre états initiaux, deux réussites.
- Les programmes correspondent à des dispositifs réellement programmables.
- 185 vérifie la compréhension d'un état que le programme ne modifie pas, comme 63.
- 186 combine une évolution numérique avec deux états forcés par le programme, comme 62.
- Les solutions et feedbacks ont été vérifiés manuellement.
- Les exercices restent en `wip`.
- Aucun build ni import SQLite n'est revendiqué.

## Validations utilisateur

- Cadrage : validé par la demande d'alignement sur les autres variantes
- Variante pilote : 61–63 servent de références établies
- Déclinaison : autorisée pour 185–186
- Review finale : à valider par l'utilisateur
- Passage testing : non validé pour 185–186
