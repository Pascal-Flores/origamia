# Reprise des variantes CM2 — vérifier et corriger la forme

## Gate 0 - Workflow

- Workflow relu : oui
- Date de relecture : 2026-09-04
- Représentation(s) autorisée(s) pour cette série : langage naturel, étapes numérotées, pseudo-code du projet et blocs textuels Blockly pris en charge par le build.
- Représentation(s) interdites : syntaxe inventée, correction libre, changement de représentation présenté comme correction correcte.
- Décision : déclinaison et review de 229–230 autorisées à la demande explicite de l'utilisateur, à partir des variantes 85–87 déjà en `testing`.

## Attendu

- Compétence : `cmp-verifier-forme-representation`.
- Attendu : `att-verifier-forme-representation-cm2`.
- Variantes de référence : 85, 86 et 87.
- Variantes reprises : 229 et 230.

## Forme de référence

Chaque variante comporte :

1. une situation concrète qui précise le résultat ou les informations attendues ;
2. une courte séquence homogène dans une représentation donnée ;
3. une instruction mal formée ou insuffisamment précise ;
4. une consigne demandant de repérer/corriger cette instruction sans changer de représentation ;
5. quatre réponses : une correction complète et homogène, une correction toujours incomplète, une modification qui change le sens ou la mauvaise ligne, et une proposition dans une autre représentation ;
6. `type: qcu`, `essais: 2`, un feedback d'aide puis un feedback final expliquant l'information manquante et la conservation de la forme.

## Reprise de 229–230

- 229 conserve `rit-relire-corriger`, non réutilisé exactement dans `main`. La séquence de relecture est contextualisée par ce qu'il faut vérifier et comporte une ligne trop vague à compléter.
- 230 conserve `rit-preparer-plan-travail`, non réutilisé exactement dans `main`. Le plan précise les tâches à placer dans `Maintenant` et `Ensuite`, puis un bloc `COMMENCER` incomplet doit être corrigé.
- Les anciennes versions à trois réponses et au contexte très réduit sont remplacées par des séquences plus complètes et quatre réponses comme dans 85–87.

## Review

Verdict : **OK**.

- 229 reprend la matrice de 87 : une procédure complète en pseudo-code, une action trop vague, quatre corrections de natures différentes et une seule réponse qui complète l'information tout en gardant la représentation.
- 230 reprend la matrice de 85 : une séquence complète en blocs, un bloc incomplet, quatre propositions dont une seule conserve à la fois la forme et le paramètre attendu.
- Les distracteurs ne se limitent plus au préfixe visuel : ils testent aussi l'information manquante et le sens de la correction.
- Les deux exercices restent en `wip`.
- Aucun build ni import SQLite n'est revendiqué.

## Validations utilisateur

- Cadrage : validé par la demande de reprise
- Variante pilote : forme 85–87 déjà validée
- Déclinaison : autorisée pour 229–230
- Review finale : à valider par l'utilisateur
- Passage testing : non validé
