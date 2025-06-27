# Guide de contribution

Merci de votre intérêt pour contribuer à ce projet !

## Comment contribuer
- Forkez le dépôt et créez une branche pour votre fonctionnalité ou correction.
- Faites vos modifications et soumettez une Pull Request.
- Décrivez clairement vos changements dans la PR.

## Bonnes pratiques
- Respectez la licence AGPLv3.
- Ajoutez des tests si possible.
- Documentez votre code.

## Code de conduite
Merci de rester respectueux et constructif dans vos échanges.

## Tester l'application localement

Pour tester l'application localement :

1. Installez les dépendances nécessaires :
   ```bash
   pip install -r requirements.txt
   pip install streamlit
   ```
2. Lancez l'application avec Streamlit :
   ```bash
   streamlit run app.py
   ```
3. Ouvrez votre navigateur à l'adresse indiquée (généralement http://localhost:8501).

Vous pouvez maintenant interagir avec l'application et tester toutes ses fonctionnalités.

## Tester en ligne (déploiement cloud)

Plusieurs options sont disponibles pour déployer et tester l'application en ligne gratuitement :

### Option 1 : Streamlit Community Cloud (Recommandé)
1. Créez un compte sur [share.streamlit.io](https://share.streamlit.io)
2. Connectez votre compte GitHub
3. Sélectionnez votre dépôt `ai_learning_game`
4. L'application sera automatiquement déployée et accessible via une URL publique

### Option 2 : Heroku
1. Créez un compte sur [heroku.com](https://heroku.com)
2. Installez Heroku CLI
3. Créez un fichier `Procfile` avec : `web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
4. Déployez avec :
   ```bash
   heroku create votre-app-name
   git push heroku main
   ```

### Option 3 : Railway
1. Créez un compte sur [railway.app](https://railway.app)
2. Connectez votre dépôt GitHub
3. L'application sera automatiquement déployée

### Option 4 : Replit
1. Créez un compte sur [replit.com](https://replit.com)
2. Importez votre projet depuis GitHub
3. Lancez avec `streamlit run app.py`

**Note :** Streamlit Community Cloud est l'option la plus simple pour les applications Streamlit.

## Tests approfondis

### Tests fonctionnels
1. **Test de l'apprentissage supervisé** :
   - Vérifiez que les emojis s'affichent correctement
   - Testez la validation des réponses (bonnes/mauvaises)
   - Vérifiez que le score se met à jour
   - Testez le bouton "Nouvel animal"

2. **Test de l'apprentissage non-supervisé** :
   - Vérifiez la génération de données clients
   - Testez l'affichage du tableau de données
   - Vérifiez la visualisation ASCII du graphique
   - Testez le bouton "Nouvelles données"

3. **Test de l'apprentissage par renforcement** :
   - Vérifiez l'affichage de l'environnement 5x1
   - Testez tous les boutons de mouvement
   - Vérifiez le calcul des récompenses
   - Testez les limites de déplacement (positions 0 et 4)
   - Vérifiez la remise à zéro de l'épisode

### Tests d'interface
- **Responsive design** : Testez sur mobile, tablette, desktop
- **Navigation** : Vérifiez le menu déroulant
- **Performance** : Testez avec plusieurs utilisateurs simultanés
- **Compatibilité** : Testez sur Chrome, Firefox, Safari, Edge

### Tests de déploiement
1. **Test local** :
   ```bash
   streamlit run app.py
   # Vérifiez l'ouverture sur http://localhost:8501
   ```

2. **Test Streamlit Cloud** :
   - Vérifiez le déploiement automatique
   - Testez l'URL publique générée
   - Vérifiez les logs de déploiement

3. **Test Heroku** :
   ```bash
   # Vérifiez que le Procfile est correct
   cat Procfile
   # Devrait afficher : web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```

### Debugging courant
- **Erreur "Module not found"** : Vérifiez requirements.txt
- **Port déjà utilisé** : Utilisez `streamlit run app.py --server.port 8502`
- **Problème de permissions** : Vérifiez les droits d'exécution
- **Erreur de syntaxe** : Vérifiez la version Python (3.7+)
