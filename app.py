# ai_learning_game - Un jeu éducatif sur l'apprentissage automatique
# Copyright (C) 2025  <Votre Nom ou Organisation>
#
# Ce programme est libre : vous pouvez le redistribuer et/ou le modifier
# selon les termes de la Licence Publique Générale Affero GNU publiée par
# la Free Software Foundation, soit la version 3 de la licence, soit
# (à votre choix) toute version ultérieure.
#
# Ce programme est distribué dans l'espoir qu'il sera utile,
# mais SANS AUCUNE GARANTIE ; sans même la garantie implicite de
# QUALITÉ MARCHANDE ou D'ADÉQUATION À UN BUT PARTICULIER. Voir la
# Licence Publique Générale Affero GNU pour plus de détails.
#
# Vous devriez avoir reçu une copie de la Licence Publique Générale Affero GNU
# avec ce programme. Si ce n'est pas le cas, voir <https://www.gnu.org/licenses/>.

try:
    import streamlit as st
    import random
except ModuleNotFoundError:
    print("Le module 'streamlit' n'est pas installé. Veuillez l'installer avec 'pip install streamlit'.")
    exit()

# Configuration de l'application
st.set_page_config(page_title="AI Learning Game", page_icon="🤖", layout="wide")

# En-tête avec style
st.markdown("""
<div style='text-align: center; padding: 2rem; background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); border-radius: 10px; margin-bottom: 2rem;'>
    <h1 style='color: white; font-size: 3rem; margin-bottom: 0.5rem;'>🤖 AI Learning Game</h1>
    <p style='color: white; font-size: 1.2rem; margin: 0;'>Découvrez l'apprentissage automatique de manière interactive !</p>
</div>
""", unsafe_allow_html=True)

# Initialisation du score dans la session
if 'score_total' not in st.session_state:
    st.session_state.score_total = 0
if 'questions_repondues' not in st.session_state:
    st.session_state.questions_repondues = 0

# Affichage du score
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.metric("🏆 Score Total", st.session_state.score_total, f"Questions: {st.session_state.questions_repondues}")

st.markdown("---")

# Sélection du type d'apprentissage
st.markdown("### 📚 Choisissez votre domaine d'apprentissage :")
type_apprentissage = st.selectbox("", [
    "🔍 Apprentissage supervisé",
    "🧩 Apprentissage non-supervisé", 
    "🎮 Apprentissage par renforcement"
], format_func=lambda x: x)

if type_apprentissage == "🔍 Apprentissage supervisé":
    st.markdown("## 🔍 Apprentissage Supervisé - Classification d'Images")
    
    # Zone d'information
    with st.expander("ℹ️ Qu'est-ce que l'apprentissage supervisé ?", expanded=False):
        st.markdown("""
        **L'apprentissage supervisé** utilise des données étiquetées pour entraîner un modèle.
        
        **Exemples concrets :**
        - 📧 Détection de spam dans les emails
        - 🏥 Diagnostic médical à partir d'images
        - 🚗 Reconnaissance de panneaux de signalisation
        - 💬 Analyse de sentiment dans les commentaires
        """)
    
    st.markdown("### 🎯 Défi : Identifiez correctement l'animal !")
    
    # Génération d'un nouvel animal à chaque rafraîchissement
    if 'current_animal' not in st.session_state:
        images = {"Chat": "🐱", "Chien": "🐶", "Oiseau": "🐦", "Poisson": "🐠", "Lapin": "🐰", "Panda": "🐼"}
        st.session_state.current_animal = random.choice(list(images.items()))
    
    label_correct, image = st.session_state.current_animal
    
    # Affichage stylé de l'image
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.markdown(f"""
        <div style='text-align: center; padding: 2rem; background-color: #f0f2f6; border-radius: 15px; margin: 1rem 0;'>
            <div style='font-size: 5rem; margin-bottom: 1rem;'>{image}</div>
            <p style='font-size: 1.2rem; color: #333;'>Quel animal voyez-vous ?</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Choix de l'utilisateur
    images_all = {"Chat": "🐱", "Chien": "🐶", "Oiseau": "🐦", "Poisson": "🐠", "Lapin": "🐰", "Panda": "🐼"}
    label_utilisateur = st.selectbox("🤔 Votre réponse :", list(images_all.keys()))
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("✅ Valider ma réponse", use_container_width=True):
            st.session_state.questions_repondues += 1
            if label_utilisateur == label_correct:
                st.session_state.score_total += 10
                st.success("🎉 Excellent ! Bonne réponse !")
                st.balloons()
            else:
                st.error(f"❌ Oups ! C'était un {label_correct}. Essayez encore !")
                st.session_state.score_total = max(0, st.session_state.score_total - 2)
            
            # Générer un nouvel animal
            st.session_state.current_animal = random.choice(list(images_all.items()))
    
    # Bouton pour une nouvelle question
    if st.button("🔄 Nouvel animal", use_container_width=True):
        st.session_state.current_animal = random.choice(list(images_all.items()))
        st.rerun()
    
    # Explication détaillée
    st.markdown("---")
    st.markdown("### 📖 Comment ça marche ?")
    st.markdown("""
    1. **Données d'entraînement** : Le modèle apprend avec des milliers d'images étiquetées
    2. **Extraction de caractéristiques** : Il identifie les patterns (formes, couleurs, textures)
    3. **Prédiction** : Sur une nouvelle image, il prédit la classe la plus probable
    4. **Évaluation** : On mesure la précision sur des données de test
    """)

elif type_apprentissage == "🧩 Apprentissage non-supervisé":
    st.markdown("## 🧩 Apprentissage Non-Supervisé - Clustering de Données")
    
    # Zone d'information
    with st.expander("ℹ️ Qu'est-ce que l'apprentissage non-supervisé ?", expanded=False):
        st.markdown("""
        **L'apprentissage non-supervisé** découvre des structures cachées dans les données sans étiquettes.
        
        **Exemples concrets :**
        - 🛒 Segmentation de clients pour le marketing
        - 🧬 Analyse de séquences génétiques
        - 📊 Détection d'anomalies dans les transactions
        - 🎵 Systèmes de recommandation musicale
        """)
    
    st.markdown("### 🎯 Défi : Regroupez les données par similarité !")
    
    # Génération de données plus réalistes
    if 'current_data' not in st.session_state:
        # Simuler des données de clients avec âge et revenu
        st.session_state.current_data = {
            'ages': [22, 25, 35, 38, 45, 48, 52, 55, 62, 65],
            'revenus': [25000, 30000, 45000, 50000, 65000, 70000, 75000, 80000, 85000, 90000]
        }
    
    data = st.session_state.current_data
    
    # Visualisation des données
    st.markdown("**📊 Données clients (Âge vs Revenu) :**")
    
    # Affichage en tableau
    import pandas as pd
    df = pd.DataFrame({
        'Client': [f'Client {i+1}' for i in range(len(data['ages']))],
        'Âge': data['ages'],
        'Revenu (€)': data['revenus']
    })
    st.dataframe(df, use_container_width=True)
    
    # Simulation d'un graphique simple avec du texte
    st.markdown("""
    ```
    Revenu (€)
    90000 |                    •  •  •
    80000 |               •  •
    70000 |          •  •
    60000 |     •  •
    50000 |•  •
    40000 |
    30000 |
    20000 +----+----+----+----+----+----+
          20   30   40   50   60   70  Âge
    ```
    """)
    
    st.markdown("### 🤔 Votre analyse :")
    groupes = st.text_area(
        "Comment regrouperiez-vous ces clients ? (ex: Jeunes/Seniors, Revenus faibles/élevés)",
        placeholder="Exemple: Groupe 1: Clients 1-4 (jeunes, revenus modestes)\nGroupe 2: Clients 5-10 (seniors, revenus élevés)"
    )
    
    if st.button("🔍 Analyser mon regroupement"):
        if groupes:
            st.success("🎯 Excellente analyse ! Voici l'interprétation de l'algorithme :")
            st.info("""
            **Groupes détectés automatiquement :**
            - 🟢 **Groupe 1** : Jeunes professionnels (20-35 ans, revenus 25-50K€)
            - 🔵 **Groupe 2** : Cadres expérimentés (35-55 ans, revenus 50-80K€)  
            - 🟡 **Groupe 3** : Seniors aisés (55+ ans, revenus 80K€+)
            """)
        else:
            st.warning("Veuillez proposer un regroupement !")
    
    if st.button("🔄 Nouvelles données", use_container_width=True):
        # Générer de nouvelles données
        ages = sorted([random.randint(20, 70) for _ in range(10)])
        revenus = sorted([random.randint(20000, 100000) for _ in range(10)])
        st.session_state.current_data = {'ages': ages, 'revenus': revenus}
        st.rerun()
    
    # Explication détaillée
    st.markdown("---")
    st.markdown("### 📖 Algorithmes de clustering populaires :")
    st.markdown("""
    - **K-means** : Divise en K groupes selon la distance euclidienne
    - **Clustering hiérarchique** : Crée un arbre de regroupements
    - **DBSCAN** : Détecte les groupes de densité variable
    - **Gaussian Mixture** : Modélise les groupes comme des distributions gaussiennes
    """)

elif type_apprentissage == "🎮 Apprentissage par renforcement":
    st.markdown("## 🎮 Apprentissage par Renforcement - Agent Explorateur")
    
    # Zone d'information
    with st.expander("ℹ️ Qu'est-ce que l'apprentissage par renforcement ?", expanded=False):
        st.markdown("""
        **L'apprentissage par renforcement** apprend par interaction avec l'environnement via récompenses/punitions.
        
        **Exemples concrets :**
        - 🎮 IA de jeux vidéo (AlphaGo, OpenAI Five)
        - 🚗 Voitures autonomes
        - 💰 Trading algorithmique
        - 🤖 Robotique et navigation
        """)
    
    # Initialisation de l'environnement
    if 'agent_position' not in st.session_state:
        st.session_state.agent_position = 2  # Position centrale
        st.session_state.episode_score = 0
        st.session_state.steps_taken = 0
        st.session_state.treasure_found = 0
    
    st.markdown("### 🗺️ Environnement : Chasse au Trésor")
    
    # Affichage de l'environnement
    environment = ["🕳️", "💰", "🤖", "🐍", "💎"]  # Piège, Trésor, Agent, Serpent, Diamant
    env_display = environment.copy()
    env_display[st.session_state.agent_position] = "🤖"
    
    st.markdown("**Position actuelle :**")
    cols = st.columns(5)
    for i, (col, item) in enumerate(zip(cols, env_display)):
        with col:
            if i == st.session_state.agent_position:
                st.markdown(f"<div style='text-align: center; background-color: #90EE90; padding: 1rem; border-radius: 10px; font-size: 2rem;'>{item}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='text-align: center; padding: 1rem; border-radius: 10px; font-size: 2rem;'>{environment[i]}</div>", unsafe_allow_html=True)
    
    # Légende
    st.markdown("""
    **Légende :** 🕳️ Piège (-10 pts) | 💰 Trésor (+15 pts) | 🤖 Vous | 🐍 Serpent (-5 pts) | 💎 Diamant (+25 pts)
    """)
    
    # Statistiques
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🏆 Score Épisode", st.session_state.episode_score)
    with col2:
        st.metric("👣 Pas", st.session_state.steps_taken)
    with col3:
        st.metric("💰 Trésors", st.session_state.treasure_found)
    with col4:
        st.metric("📍 Position", st.session_state.agent_position + 1)
    
    # Actions possibles
    st.markdown("### 🎯 Choisissez votre action :")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("⬅️ Aller à Gauche", disabled=st.session_state.agent_position == 0):
            st.session_state.agent_position = max(0, st.session_state.agent_position - 1)
            reward = calculate_reward(st.session_state.agent_position, environment)
            st.session_state.episode_score += reward
            st.session_state.steps_taken += 1
            if reward > 0:
                st.session_state.treasure_found += 1
            show_reward_feedback(reward)
            st.rerun()
    
    with col2:
        if st.button("🛑 Rester sur Place"):
            # Petite pénalité pour l'inaction
            st.session_state.episode_score -= 1
            st.session_state.steps_taken += 1
            st.warning("Vous restez sur place (-1 pt)")
            st.rerun()
    
    with col3:
        if st.button("➡️ Aller à Droite", disabled=st.session_state.agent_position == 4):
            st.session_state.agent_position = min(4, st.session_state.agent_position + 1)
            reward = calculate_reward(st.session_state.agent_position, environment)
            st.session_state.episode_score += reward
            st.session_state.steps_taken += 1
            if reward > 0:
                st.session_state.treasure_found += 1
            show_reward_feedback(reward)
            st.rerun()
    
    # Bouton reset
    if st.button("🔄 Nouvel Épisode"):
        st.session_state.agent_position = 2
        st.session_state.episode_score = 0
        st.session_state.steps_taken = 0
        st.session_state.treasure_found = 0
        st.rerun()
    
    # Explication détaillée
    st.markdown("---")
    st.markdown("### 📖 Concepts clés :")
    st.markdown("""
    - **Agent** : L'entité qui prend des décisions (vous)
    - **Environnement** : Le monde dans lequel l'agent évolue
    - **Actions** : Les choix possibles (gauche, droite, rester)
    - **Récompenses** : Les signaux de feedback (+/- points)
    - **Politique** : La stratégie apprise pour maximiser les récompenses
    """)

# Fonctions utilitaires pour l'apprentissage par renforcement
def calculate_reward(position, environment):
    """Calcule la récompense basée sur la position actuelle"""
    rewards = {
        "🕳️": -10,  # Piège
        "💰": 15,   # Trésor
        "🤖": 0,    # Position neutre
        "🐍": -5,   # Serpent
        "💎": 25    # Diamant
    }
    return rewards.get(environment[position], 0)

def show_reward_feedback(reward):
    """Affiche le feedback basé sur la récompense"""
    if reward > 20:
        st.success(f"🎉 FANTASTIQUE ! Vous avez trouvé un diamant ! (+{reward} pts)")
        st.balloons()
    elif reward > 10:
        st.success(f"💰 Excellent ! Trésor découvert ! (+{reward} pts)")
    elif reward > 0:
        st.info(f"✨ Pas mal ! (+{reward} pts)")
    elif reward == 0:
        st.warning("😐 Zone neutre (0 pt)")
    elif reward > -10:
        st.warning(f"🐍 Aïe ! Vous avez rencontré un serpent ! ({reward} pts)")
    else:
        st.error(f"🕳️ OUPS ! Vous êtes tombé dans un piège ! ({reward} pts)")
