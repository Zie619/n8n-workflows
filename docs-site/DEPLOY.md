# 🚀 Guide de Déploiement Netlify

## Méthode 1 : Déploiement via l'Interface Netlify (Recommandé)

### Étape 1 : Préparation
1. Assurez-vous que tous vos workflows sont dans le dossier `workflows/`
2. Générez les données :
   ```bash
   cd n8n-workflows
   node docs-site/generate-data.js
   ```

### Étape 2 : Connexion GitHub
1. Allez sur [netlify.com](https://netlify.com)
2. Connectez-vous ou créez un compte
3. Cliquez sur "Add new site" → "Import an existing project"
4. Choisissez "GitHub" et autorisez l'accès
5. Sélectionnez le repository `n8n-workflows`

### Étape 3 : Configuration du Build
Netlify détectera automatiquement le fichier `netlify.toml` avec ces paramètres :
- **Build command**: `node docs-site/generate-data.js`
- **Publish directory**: `docs-site`

### Étape 4 : Déploiement
1. Cliquez sur "Deploy site"
2. Attendez quelques secondes
3. Votre site est en ligne ! 🎉

### Étape 5 : Configuration du Domaine (Optionnel)
1. Dans les settings Netlify, allez dans "Domain management"
2. Personnalisez votre sous-domaine : `votre-nom.netlify.app`
3. Ou configurez un domaine personnalisé

## Méthode 2 : Déploiement via Netlify CLI

### Installation de Netlify CLI
```bash
npm install -g netlify-cli
```

### Authentification
```bash
netlify login
```

### Déploiement
```bash
# Déploiement de test
netlify deploy --dir=docs-site

# Déploiement en production
netlify deploy --dir=docs-site --prod
```

## Méthode 3 : Drag & Drop

### Préparation
1. Générez les données :
   ```bash
   node docs-site/generate-data.js
   ```

### Déploiement
1. Allez sur [netlify.com/drop](https://netlify.com/drop)
2. Faites glisser le dossier `docs-site` dans la zone
3. Votre site est déployé instantanément !

⚠️ **Note**: Cette méthode ne permet pas les mises à jour automatiques

## 🔄 Mises à Jour Automatiques

Avec le déploiement GitHub (Méthode 1) :

1. Ajoutez vos workflows dans `workflows/`
2. Commitez et poussez :
   ```bash
   git add workflows/
   git commit -m "Add new workflows"
   git push
   ```
3. Netlify rebuild et redéploie automatiquement ! ✨

## 🎯 URL de votre Site

Après le déploiement, votre site sera accessible à :
```
https://[nom-unique].netlify.app
```

Vous pouvez personnaliser cette URL dans les settings Netlify.

## ⚙️ Configuration Avancée

### Variables d'Environnement
Si nécessaire, ajoutez des variables dans Netlify :
1. Site settings → Build & deploy → Environment
2. Ajoutez vos variables

### Déploiement sur une Branche Spécifique
Dans `netlify.toml`, ajoutez :
```toml
[context.production]
  branch = "main"

[context.develop]
  branch = "develop"
```

### Prévisualisation des Pull Requests
Netlify génère automatiquement des previews pour chaque PR !

## 🐛 Résolution de Problèmes

### Erreur "Command failed"
- Vérifiez que le dossier `workflows/` existe
- Assurez-vous que les fichiers JSON sont valides

### Site vide
- Vérifiez que `data.json` a été généré
- Regardez les logs de build dans Netlify

### Erreur 404
- Vérifiez que le publish directory est bien `docs-site`
- Vérifiez que `index.html` est présent

## 📊 Monitoring

Dans Netlify, vous pouvez :
- Voir les statistiques de visite
- Consulter les logs de build
- Gérer les formulaires et fonctions
- Configurer des webhooks

## 🔒 Sécurité

Le fichier `netlify.toml` inclut déjà :
- Headers de sécurité (XSS, frame protection)
- Cache optimal pour les assets
- Redirections SPA

## 📈 Optimisations

### Performance
- Les CSS/JS sont mis en cache 1 an
- `data.json` est mis en cache 1 heure
- Headers de compression automatiques

### SEO
Pour améliorer le SEO, ajoutez dans `index.html` :
```html
<meta name="description" content="Documentation n8n workflows">
<meta property="og:title" content="n8n Workflows Documentation">
<meta property="og:description" content="...">
```

## ✅ Checklist de Déploiement

- [ ] Workflows présents dans `workflows/`
- [ ] `data.json` généré
- [ ] Repository poussé sur GitHub
- [ ] Site connecté à Netlify
- [ ] Build réussi
- [ ] Site accessible
- [ ] Domaine personnalisé configuré (optionnel)

---

🎉 Félicitations ! Votre documentation est maintenant en ligne et se met à jour automatiquement !
