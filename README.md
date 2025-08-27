# Démo GitHub Pages + Python

Ce repo contient :
- Une page HTML statique (hébergée via GitHub Pages)
- Des scripts Python qui génèrent un fichier `data.json`
- Du JavaScript qui charge et affiche ce JSON

## 🚀 Déploiement GitHub Pages
1. Aller dans `Settings > Pages`
2. Sélectionner la branche `main` et le dossier `/root`
3. Ton site sera accessible à :  
   `https://<ton-nom-utilisateur>.github.io/<nom-du-repo>/`

## 🐍 Génération des données
Pour mettre à jour les données :
```bash
cd python
python generate_data.py