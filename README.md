# 🤖 AI Learning Game

Un jeu éducatif interactif pour découvrir les concepts fondamentaux de l'intelligence artificielle et de l'apprentissage automatique.

## 🎯 Description détaillée

Ce projet propose une expérience d'apprentissage gamifiée qui couvre les **trois piliers de l'apprentissage automatique** :

### 🔍 Apprentissage Supervisé
- **Concept** : Classification d'images avec des données étiquetées
- **Gameplay** : Identifier correctement des animaux représentés par des emojis
- **Apprentissage** : Comprendre comment un modèle apprend à partir d'exemples étiquetés
- **Exemples réels** : Détection de spam, diagnostic médical, reconnaissance vocale

### 🧩 Apprentissage Non-Supervisé  
- **Concept** : Découverte de patterns cachés dans des données
- **Gameplay** : Regrouper des profils clients selon leurs similarités
- **Apprentissage** : Explorer le clustering et la segmentation automatique
- **Exemples réels** : Segmentation marketing, détection d'anomalies, systèmes de recommandation

### 🎮 Apprentissage par Renforcement
- **Concept** : Apprentissage par essais-erreurs avec un système de récompenses
- **Gameplay** : Naviguer dans un environnement pour maximiser son score
- **Apprentissage** : Comprendre comment un agent apprend une stratégie optimale
- **Exemples réels** : Jeux vidéo (AlphaGo), voitures autonomes, trading algorithmique

## 🚀 Fonctionnalités

- ✅ **Interface intuitive** avec Streamlit
- 🏆 **Système de score** pour gamifier l'apprentissage
- 📊 **Visualisations interactives** des données
- 💡 **Explications pédagogiques** détaillées pour chaque concept
- 🎨 **Design moderne** avec CSS personnalisé
- 📱 **Responsive** : fonctionne sur desktop et mobile

## 📋 Prérequis

- **Python 3.7+** installé sur votre système
- **pip** pour la gestion des paquets Python
- Un navigateur web moderne (Chrome, Firefox, Safari, Edge)

## ⚙️ Installation détaillée

### Option 1 : Installation classique

1. **Clonez le dépôt** :
   ```bash
   git clone https://github.com/votre-username/ai_learning_game.git
   cd ai_learning_game
   ```

2. **Créez un environnement virtuel** (recommandé) :
   ```bash
   # Avec venv
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # OU
   venv\Scripts\activate     # Windows
   
   # Avec conda
   conda create -n ai_game python=3.9
   conda activate ai_game
   ```

3. **Installez les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

### Option 2 : Installation rapide
```bash
pip install streamlit pandas
```

## 🎮 Utilisation

### Lancement local
```bash
streamlit run app.py
```

L'application s'ouvrira automatiquement dans votre navigateur à l'adresse `http://localhost:8501`.

### Navigation dans l'application
1. **Sélectionnez un type d'apprentissage** dans le menu déroulant
2. **Suivez les instructions** spécifiques à chaque module
3. **Consultez les explications** pour approfondir vos connaissances
4. **Suivez votre progression** avec le système de score intégré

## 🌐 Déploiement en ligne

### Streamlit Community Cloud (Recommandé)
1. Forkez ce dépôt sur GitHub
2. Créez un compte sur [share.streamlit.io](https://share.streamlit.io)
3. Connectez votre compte GitHub
4. Sélectionnez votre fork du projet
5. L'application sera automatiquement déployée !

### Autres plateformes
- **[Heroku](https://heroku.com)** : Avec le `Procfile` inclus
- **[Railway](https://railway.app)** : Déploiement automatique depuis GitHub
- **[Replit](https://replit.com)** : Environnement de développement en ligne

## 🧪 Tests et développement

### Tests manuels
- Testez chaque module d'apprentissage
- Vérifiez le système de score
- Testez la responsivité sur différents appareils

### Structure du projet
```
ai_learning_game/
├── app.py              # Application principale Streamlit
├── requirements.txt    # Dépendances Python
├── Procfile           # Configuration Heroku
├── README.md          # Cette documentation
├── LICENSE            # Licence AGPLv3
└── CONTRIBUTING.md    # Guide de contribution
```

## 🤝 Contribution

Les contributions sont les bienvenues ! Consultez [CONTRIBUTING.md](CONTRIBUTING.md) pour :
- Les instructions de développement
- Le processus de soumission de PR
- Les standards de code
- Les options de test et déploiement

## 📚 Ressources pédagogiques

### Pour aller plus loin
- 📖 [Cours de Machine Learning de Stanford](https://www.coursera.org/learn/machine-learning)
- 🎥 [3Blue1Brown - Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)
- 📚 [Hands-On Machine Learning](https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/)
- 🔗 [Scikit-learn Documentation](https://scikit-learn.org/stable/)

## 📄 Licence

Ce projet est sous licence **AGPLv3**. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🆘 Support

- 🐛 **Bugs** : Ouvrez une [issue](https://github.com/votre-username/ai_learning_game/issues)
- 💡 **Suggestions** : Proposez vos idées via les issues
- 📧 **Contact** : [votre-email@exemple.com]

## 🏷️ Version

**Version actuelle** : 1.0.0
**Dernière mise à jour** : Juin 2025


