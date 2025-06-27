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
