# Templates a dupliquer (version simple)

But: dupliquer un des fichiers template du dossier, remplir, puis convertir en JSON.

## Frontmatter minimal (identique partout)

```yaml
nom: Nom visible par l'élève
description: Courte description pédagogique visible dans les outils de suivi.
type:
competence:
attendu:
statut: wip
essais: 2
media:
link:
```

## Choisir un template

- exercice-qcu-qcm-dd.md
- exercice-free.md
- exercice-ddu.md
- exercice-texte-a-trous.md
- exercice-interface.md

## Regle pratique

1. Dupliquer un template.
2. Remplir le frontmatter + sections.
3. Separer toujours la situation dans `# Contexte` et l'action demandee dans `# Consigne`.
4. Garder la numerotation des reponses/solutions en chiffres.
5. Pour `exercice-texte-a-trous.md`, utiliser `[[1]]`, `[[2]]`, etc. pour marquer les trous dans l'ordre.
6. Dans un texte a trous, les etiquettes doivent etre du texte simple, directement inserable dans la phrase, pas des blocs ou du code.
7. `nom` doit etre court et lisible par l'eleve, sans mention technique de variante.
8. `description` doit resumer le geste travaille pour le suivi pedagogique.
9. `essais` indique le nombre maximal de tentatives.
10. Si `essais` vaut 2 ou plus, ajouter `# Feedback essai 1`, puis `# Feedback essai 2`, etc. jusqu'a l'avant-dernier essai.
11. `# Feedback` est le feedback final apres echec complet. `# Feedback final` est aussi accepte.

Le format reste volontairement court pour faciliter l'ecriture.
