# Site de Documentation n8n Workflows

Ce site web génère automatiquement une documentation complète de tous vos workflows n8n.

## 🚀 Déploiement sur Netlify

### Option 1 : Déploiement automatique via GitHub

1. Connectez votre repository GitHub à Netlify
2. Netlify détectera automatiquement le fichier `netlify.toml`
3. Le site sera déployé automatiquement à chaque push

### Option 2 : Déploiement manuel

1. Générez le fichier de données :
   ```bash
   node docs-site/generate-data.js
   ```

2. Déployez le dossier `docs-site` sur Netlify :
   ```bash
   netlify deploy --dir=docs-site --prod
   ```

## 📁 Structure du Site

```
docs-site/
├── index.html          # Page principale
├── styles.css          # Styles CSS
├── app.js             # Application JavaScript
├── generate-data.js   # Script de génération des données
├── data.json          # Données des workflows (généré)
└── README.md          # Ce fichier
```

## 🔧 Fonctionnalités

### Vue d'ensemble
- Statistiques globales du projet
- Nombre total de workflows, nodes, et connexions
- Structure du projet
- Types de nodes communs

### Workflows
- Liste complète de tous les workflows
- Recherche et filtrage
- Détails de chaque workflow :
  - Nombre de nodes et connexions
  - Tags et métadonnées
  - Liste des nodes utilisés
  - Dates de création et modification

### Catalogue de Nodes
- Liste de tous les types de nodes utilisés
- Nombre d'utilisations par type
- Workflows utilisant chaque type de node

### Statistiques
- Statistiques détaillées
- Top 10 des nodes les plus utilisés
- Distribution des workflows par complexité
- Workflows par tag

## 🎨 Personnalisation

### Changer les Couleurs

Modifiez les variables CSS dans `styles.css` :

```css
:root {
    --primary: #ea4b71;
    --primary-dark: #d63e5f;
    --secondary: #ff6d5a;
    --background: #0f172a;
    /* ... autres couleurs */
}
```

### Modifier le Contenu

Éditez `index.html` pour modifier :
- Le titre et la description
- Le contenu de la vue d'ensemble
- Les sections affichées

### Ajouter des Fonctionnalités

Modifiez `app.js` pour :
- Ajouter de nouvelles statistiques
- Créer de nouveaux filtres
- Personnaliser l'affichage

## 🔄 Mise à Jour

Lorsque vous ajoutez de nouveaux workflows :

1. Placez vos fichiers JSON dans `workflows/`
2. Régénérez les données :
   ```bash
   node docs-site/generate-data.js
   ```
3. Commitez et poussez les changements

Si déployé sur Netlify avec GitHub, la mise à jour sera automatique.

## 🌐 Accès au Site

Une fois déployé, votre site sera accessible à :
- `https://[votre-site].netlify.app`

## 📝 Notes Importantes

- Le fichier `data.json` doit être régénéré après chaque modification des workflows
- Les workflows ne contiennent pas de credentials (stockés séparément dans n8n)
- Le site est entièrement statique et ne nécessite pas de serveur backend

## 🐛 Dépannage

### Le site ne charge pas les workflows

1. Vérifiez que `data.json` existe et contient des données
2. Régénérez le fichier : `node docs-site/generate-data.js`
3. Vérifiez la console du navigateur pour les erreurs

### Erreur lors de la génération de data.json

1. Vérifiez que le dossier `workflows/` existe
2. Vérifiez que les fichiers JSON sont valides
3. Assurez-vous que Node.js est installé

### Le design ne s'affiche pas correctement

1. Vérifiez que tous les fichiers (HTML, CSS, JS) sont présents
2. Videz le cache du navigateur
3. Vérifiez la console pour les erreurs de chargement

## 📧 Support

Pour toute question ou problème, consultez la documentation ou ouvrez une issue sur GitHub.

---

Créé avec ❤️ pour la documentation automatique des workflows n8n
