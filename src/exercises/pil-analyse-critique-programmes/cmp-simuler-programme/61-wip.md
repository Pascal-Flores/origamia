# Reprise des variantes 6e — simuler un programme

## Gate 0 - Workflow

- Workflow relu : oui
- Date de relecture : 2026-09-03
- Représentation(s) autorisée(s) pour cette série : mission explicite, même programme fourni en blocs textuels (`event:`, `move:`, `say:`, `end:`), quatre états initiaux en langage naturel.
- Représentation(s) interdites : programme réduit à une opération isolée, syntaxe de variable inventée, tâche qui ne teste qu'une valeur sans état initial complet.
- Décision : review et harmonisation autorisées à la demande explicite de l'utilisateur.

## Attendu

- Compétence : `cmp-simuler-programme`.
- Attendu : `att-simuler-programme-6e`.
- Variantes de référence : 61, 62, 63.
- Variantes reprises : 213, 214.

## Forme de référence

Les variantes 61–63 utilisent la même mécanique :

1. une mission définie par un état final précis ;
2. un même programme exécuté dans quatre états initiaux différents ;
3. l'élève simule séparément chaque test ;
4. il sélectionne tous les états initiaux qui conduisent à la réussite (`type: qcm`) ;
5. deux tests réussissent et deux échouent ;
6. trois essais avec deux feedbacks progressifs puis un feedback final.

## Reprise de 213–214

- 213 conserve la crème solaire mais devient une **simulation** : le programme ajoute deux zones couvertes et referme le tube ; la mission impose un nombre final de zones couvertes et un tube fermé.
- 214 conserve le contexte du parc mais devient une **simulation de planning** : le programme consomme trois minutes et marque l'activité comme terminée ; la réussite dépend aussi d'une information initiale que le programme ne modifie pas.
- Les deux exercices reprennent quatre états initiaux complets et deux réussites.

## Validations utilisateur

- Cadrage : validé par la demande d'alignement sur les autres variantes
- Variante pilote : 61 déjà existante et sert de référence
- Déclinaison : autorisée pour 213–214
- Review finale : à valider par l'utilisateur
- Passage testing : non validé pour 213–214
