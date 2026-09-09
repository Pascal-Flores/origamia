# Origamia

Exercices et outils pour le référentiel de compétences.

Pour faire un retour, remplir librement le champ `review` de l'exercice dans [src/exercises](src/exercises/), initialement vide (`review: ""`). Pour plusieurs lignes :

```yaml
review: |
  Préciser que deux réponses sont attendues.
```

Pour afficher les exercices qui ont un retour :

```bash
python3 origamia reviews
```

La commande affiche leur numéro, leur nom, le chemin du fichier et le texte de `review`, triés par numéro. Les champs vides sont ignorés, y compris ceux qui ne contiennent que des espaces ou des lignes vides. Elle lit directement les sources, sans lancer de build.
