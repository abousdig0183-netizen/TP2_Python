
## TP2 — Encapsulation

`TP2_Python/README.md`:

```markdown
# TP2 – Encapsulation en Python

## Objectif
Comprendre le principe d'encapsulation et protéger les données d'une classe.

## Notions abordées
- Attributs publics, protégés et privés
- Encapsulation
- Getters et Properties
- Validation des données
- Méthodes d'accès et de modification
- Historique des opérations
- Héritage avec CompteEpargne

## Classe principale
`CompteBancaire`

## Fichier principal
`compte_bancaire.py`

## Exemple
```python
compte = CompteBancaire("Ali", 1000)
compte.deposer(200)
compte.retirer(150)
print(compte.solde)
