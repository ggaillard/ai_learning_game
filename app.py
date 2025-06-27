# ai_learning_game - Un jeu éducatif sur l'apprentissage automatique
# Copyright (C) 2025  AI Learning Game Contributors
#
# Ce programme est distribué sous licence éducative libre et non commerciale
# Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
# avec des dispositions supplémentaires pour l'usage pédagogique.
#
# Vous êtes libre de partager, adapter et enseigner avec ce matériel
# pour des usages non commerciaux en respectant l'attribution et le partage
# dans les mêmes conditions.
#
# Voir LICENSE_EDUCATIONAL pour les détails complets de la licence.
# Source : https://github.com/[votre-repo]/ai_learning_game

try:
    import streamlit as st
    import random
except ModuleNotFoundError:
    print("Le module 'streamlit' n'est pas installé. Veuillez l'installer avec 'pip install streamlit'.")
    exit()

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

def show_detailed_feedback_supervised(correct, user_answer, correct_answer, score_gained):
    """Feedback didactique détaillé pour l'apprentissage supervisé"""
    if correct:
        st.success(f"🎉 **CORRECT !** Vous avez identifié un {correct_answer}")
        st.info(f"""
        **🧠 Analyse didactique :**
        - **Processus mental** : Vous avez comparé les caractéristiques visuelles de l'emoji avec vos connaissances
        - **En IA** : Un modèle ferait de même en analysant les pixels, formes et patterns
        - **Apprentissage** : Chaque bonne réponse renforce les connexions neuronales
        - **Points gagnés** : +{score_gained} (récompense positive = renforcement)
        """)
        with st.expander("🔬 Zoom sur l'algorithme"):
            st.markdown("""
            1. **Extraction de caractéristiques** : L'emoji a des patterns uniques
            2. **Comparaison** : Votre cerveau compare avec sa base de données
            3. **Classification** : Attribution à la classe la plus probable
            4. **Confiance** : Degré de certitude dans la prédiction
            """)
    else:
        st.error(f"❌ **INCORRECT !** C'était un {correct_answer}, pas un {user_answer}")
        st.warning(f"""
        **🔍 Analyse de l'erreur :**
        - **Confusion possible** : Similarités visuelles entre {user_answer} et {correct_answer}
        - **En IA** : C'est ce qu'on appelle une "fausse classification"
        - **Apprentissage** : L'erreur aide à ajuster les poids du modèle
        - **Pénalité** : {score_gained} points (signal d'erreur pour l'apprentissage)
        """)
        with st.expander("🎯 Comment s'améliorer ?"):
            st.markdown(f"""
            - **Observez mieux** : Quelles sont les caractéristiques uniques du {correct_answer} ?
            - **Mémorisation** : Associez l'emoji à ses traits distinctifs
            - **En IA** : Plus de données d'entraînement améliorent la précision
            """)

def show_detailed_feedback_unsupervised(user_groups, data):
    """Feedback didactique détaillé pour l'apprentissage non-supervisé"""
    st.success("🧩 **Analyse de votre regroupement :**")
    
    # Analyse automatique des groupes optimaux
    ages = data['ages']
    revenus = data['revenus']
    
    optimal_groups = []
    if max(ages) - min(ages) > 30:
        optimal_groups.append("👶 **Jeunes** (20-35 ans)")
        optimal_groups.append("👨 **Expérimentés** (35-55 ans)")
        optimal_groups.append("👴 **Seniors** (55+ ans)")
    
    st.info(f"""
    **🔍 Votre approche vs Algorithme :**
    
    **Votre regroupement :** {user_groups}
    
    **Groupes optimaux détectés :**
    {chr(10).join([f"- {group}" for group in optimal_groups])}
    
    **🧠 Apprentissage didactique :**
    - **Similarité** : Vous cherchez des patterns comme l'âge ou le revenu similaires
    - **Distance** : En IA, on calcule la "distance" mathématique entre les points
    - **Centroïdes** : Chaque groupe a un "centre" représentatif
    - **Itération** : L'algorithme ajuste les groupes jusqu'à convergence
    """)
    
    with st.expander("🔬 Algorithmes de clustering"):
        st.markdown(f"""
        **K-Means (le plus populaire) :**
        1. **Initialisation** : Choix de {len(optimal_groups)} centres aléatoirement
        2. **Attribution** : Chaque client va au centre le plus proche
        3. **Recalcul** : Les centres se déplacent au milieu de leur groupe
        4. **Répétition** : Jusqu'à stabilisation des groupes
        
        **Critères de qualité :**
        - **Cohésion interne** : Clients similaires dans un même groupe
        - **Séparation externe** : Groupes bien distincts les uns des autres
        """)

def show_detailed_feedback_reinforcement(action, reward, position, episode_score, steps):
    """Feedback didactique détaillé pour l'apprentissage par renforcement"""
    environment_names = {0: "🕳️ Piège", 1: "💰 Trésor", 2: "🤖 Neutre", 3: "🐍 Serpent", 4: "💎 Diamant"}
    current_zone = environment_names.get(position, "Zone inconnue")
    
    if reward > 20:
        st.success(f"🎉 **RÉCOMPENSE MAXIMALE !** {current_zone}")
        st.info(f"""
        **🏆 Excellence stratégique :**
        - **Action** : {action} vers position {position+1}
        - **Récompense** : +{reward} points (signal très positif)
        - **Apprentissage** : Cette action sera **fortement renforcée**
        - **Stratégie** : Mémorisez cette séquence gagnante !
        """)
        
    elif reward > 0:
        st.success(f"✅ **BONNE ACTION !** {current_zone}")
        st.info(f"""
        **📈 Progrès positif :**
        - **Récompense** : +{reward} points
        - **Signal** : Votre choix était judicieux
        - **Renforcement** : Cette action a plus de chances d'être répétée
        """)
        
    elif reward == 0:
        st.warning(f"😐 **ACTION NEUTRE** {current_zone}")
        st.info("""
        **🤔 Pas d'apprentissage :**
        - **Récompense** : 0 point (signal neutre)
        - **Effet** : Aucun renforcement positif ou négatif
        - **Conseil** : Explorez d'autres actions pour apprendre
        """)
        
    else:
        st.error(f"❌ **PUNITION !** {current_zone}")
        st.warning(f"""
        **⚠️ Signal négatif :**
        - **Pénalité** : {reward} points
        - **Apprentissage** : Cette action sera **découragée**
        - **Stratégie** : Évitez cette zone à l'avenir
        - **Adaptation** : L'agent apprend de ses erreurs
        """)
    
    # Analyse stratégique globale
    with st.expander("🎯 Analyse stratégique avancée"):
        performance = episode_score / max(steps, 1)
        st.markdown(f"""
        **📊 Performance actuelle :**
        - **Score/Action** : {performance:.1f} points par action
        - **Efficacité** : {'🟢 Excellente' if performance > 5 else '🟡 Moyenne' if performance > 0 else '🔴 À améliorer'}
        
        **🧠 Concepts clés :**
        - **Exploration vs Exploitation** : Faut-il découvrir ou répéter les bonnes actions ?
        - **Fonction de valeur** : Chaque position a une "valeur" espérée
        - **Politique optimale** : La meilleure stratégie à long terme
        - **Discount factor** : Les récompenses futures valent-elles moins ?
        """)

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
                score_gained = 10
                st.session_state.score_total += score_gained
                show_detailed_feedback_supervised(True, label_utilisateur, label_correct, score_gained)
                st.balloons()
            else:
                score_gained = -2
                st.session_state.score_total = max(0, st.session_state.score_total + score_gained)
                show_detailed_feedback_supervised(False, label_utilisateur, label_correct, score_gained)
            
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
            show_detailed_feedback_unsupervised(groupes, data)
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
    
    # Règles du jeu détaillées
    with st.expander("📋 RÈGLES DU JEU - À LIRE AVANT DE COMMENCER", expanded=True):
        st.markdown("""
        ### 🎯 **Objectif :**
        Maximisez votre score en naviguant intelligemment dans l'environnement !
        
        ### 🗺️ **L'environnement :**
        - Vous évoluez sur une **ligne de 5 cases** (positions 1 à 5)
        - Chaque case contient un **élément différent** avec sa récompense
        - Votre position actuelle est marquée par le robot 🤖
        
        ### 🎮 **Actions possibles :**
        - **⬅️ Aller à Gauche** : Se déplace d'une case vers la gauche (si possible)
        - **➡️ Aller à Droite** : Se déplace d'une case vers la droite (si possible)  
        - **🛑 Rester sur Place** : Ne bouge pas (pénalité de -1 point)
        
        ### 🏆 **Système de récompenses :**
        - 🕳️ **Piège** : **-10 points** (Attention, très pénalisant !)
        - 🐍 **Serpent** : **-5 points** (Évitez-le si possible)
        - 🤖 **Zone neutre** : **0 point** (Pas de récompense)
        - 💰 **Trésor** : **+15 points** (Bonne trouvaille !)
        - 💎 **Diamant** : **+25 points** (Jackpot ! La meilleure récompense)
        
        ### 🧠 **Stratégie :**
        - **Explorez** d'abord pour découvrir l'environnement
        - **Retenez** où sont les bonnes et mauvaises cases
        - **Optimisez** vos déplacements pour maximiser les gains
        - **Attention** : rester immobile coûte des points !
        """)
    
    # Affichage de l'environnement
    environment = ["🕳️", "💰", "🤖", "🐍", "💎"]  # Piège, Trésor, Agent, Serpent, Diamant
    env_display = environment.copy()
    env_display[st.session_state.agent_position] = "🤖"
    
    st.markdown("### 🎮 **Votre environnement actuel :**")
    
    # Affichage des numéros de positions
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.markdown(f"<div style='text-align: center; font-weight: bold; color: #666;'>Position {i+1}</div>", unsafe_allow_html=True)
    
    # Affichage de l'environnement avec votre position
    cols = st.columns(5)
    for i, (col, item) in enumerate(zip(cols, env_display)):
        with col:
            if i == st.session_state.agent_position:
                st.markdown(f"<div style='text-align: center; background-color: #90EE90; padding: 1.5rem; border-radius: 15px; font-size: 3rem; border: 3px solid #4CAF50;'>{item}</div>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center; color: #4CAF50; font-weight: bold; margin-top: 0.5rem;'>VOUS ÊTES ICI</p>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='text-align: center; padding: 1.5rem; border-radius: 15px; font-size: 3rem; background-color: #f0f2f6;'>{environment[i]}</div>", unsafe_allow_html=True)
    
    # Légende avec explications
    st.markdown("### 🔍 **Légende des éléments :**")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - 🕳️ **Piège** : -10 points
        - � **Serpent** : -5 points  
        - 🤖 **Vous** : Position actuelle
        """)
    with col2:
        st.markdown("""
        - 💰 **Trésor** : +15 points
        - 💎 **Diamant** : +25 points
        """)
    
    st.markdown("---")
    
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
    st.markdown("### 🎯 **Choisissez votre prochaine action :**")
    
    # Indication de l'état actuel
    current_pos = st.session_state.agent_position + 1
    st.info(f"🤖 Vous êtes actuellement en **Position {current_pos}** sur l'élément **{environment[st.session_state.agent_position]}**")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        can_go_left = st.session_state.agent_position > 0
        next_left_pos = st.session_state.agent_position - 1 if can_go_left else None
        next_left_element = environment[next_left_pos] if next_left_pos is not None else None
        
        if can_go_left:
            st.markdown(f"**Destination :** Position {next_left_pos + 1} ({next_left_element})")
        else:
            st.markdown("**Impossible** : Vous êtes au bord gauche")
            
        if st.button("⬅️ Aller à Gauche", disabled=not can_go_left, use_container_width=True):
            st.session_state.agent_position = max(0, st.session_state.agent_position - 1)
            reward = calculate_reward(st.session_state.agent_position, environment)
            st.session_state.episode_score += reward
            st.session_state.steps_taken += 1
            if reward > 0:
                st.session_state.treasure_found += 1
            show_detailed_feedback_reinforcement("Gauche", reward, st.session_state.agent_position, 
                                                st.session_state.episode_score, st.session_state.steps_taken)
            st.rerun()
    
    with col2:
        st.markdown("**Action :** Rester immobile")
        st.markdown("**Conséquence :** -1 point (pénalité)")
        
        if st.button("🛑 Rester sur Place", use_container_width=True):
            # Petite pénalité pour l'inaction
            st.session_state.episode_score -= 1
            st.session_state.steps_taken += 1
            show_detailed_feedback_reinforcement("Rester", -1, st.session_state.agent_position, 
                                                st.session_state.episode_score, st.session_state.steps_taken)
            st.rerun()
    
    with col3:
        can_go_right = st.session_state.agent_position < 4
        next_right_pos = st.session_state.agent_position + 1 if can_go_right else None
        next_right_element = environment[next_right_pos] if next_right_pos is not None else None
        
        if can_go_right:
            st.markdown(f"**Destination :** Position {next_right_pos + 1} ({next_right_element})")
        else:
            st.markdown("**Impossible** : Vous êtes au bord droit")
            
        if st.button("➡️ Aller à Droite", disabled=not can_go_right, use_container_width=True):
            st.session_state.agent_position = min(4, st.session_state.agent_position + 1)
            reward = calculate_reward(st.session_state.agent_position, environment)
            st.session_state.episode_score += reward
            st.session_state.steps_taken += 1
            if reward > 0:
                st.session_state.treasure_found += 1
            show_detailed_feedback_reinforcement("Droite", reward, st.session_state.agent_position, 
                                                st.session_state.episode_score, st.session_state.steps_taken)
            st.rerun()
    
    st.markdown("---")
    
    # Conseils stratégiques
    st.markdown("### 💡 **Conseils pour une stratégie optimale :**")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **🎯 Phase d'exploration :**
        - Testez toutes les positions au moins une fois
        - Notez mentalement les récompenses de chaque case
        - N'ayez pas peur des pénalités au début !
        """)
    with col2:
        st.markdown("""
        **🏆 Phase d'exploitation :**
        - Privilégiez les cases avec des récompenses positives
        - Évitez les pièges et serpents quand vous les connaissez
        - Minimisez les déplacements inutiles
        """)
    
    # Bouton reset avec explication
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🔄 Nouvel Épisode", use_container_width=True):
            st.session_state.agent_position = 2
            st.session_state.episode_score = 0
            st.session_state.steps_taken = 0
            st.session_state.treasure_found = 0
            st.success("🎯 Nouvel épisode commencé ! Vous repartez de la position centrale.")
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

# Section Glossaire
st.markdown("---")
st.markdown("## 📚 Glossaire des Termes d'IA")

with st.expander("🔍 Apprentissage Supervisé - Termes Clés"):
    st.markdown("""
    **🎯 Classification** : Prédire à quelle catégorie appartient un élément
    
    **🏷️ Étiquettes (Labels)** : Les bonnes réponses utilisées pour entraîner le modèle
    
    **📊 Données d'entraînement** : Exemples avec leurs réponses correctes pour apprendre
    
    **🧠 Modèle** : L'algorithme qui apprend à faire des prédictions
    
    **⚖️ Fonction de perte** : Mesure l'erreur entre prédiction et réalité
    
    **🎯 Précision** : Pourcentage de bonnes prédictions sur le total
    
    **🔄 Surapprentissage** : Quand le modèle mémorise au lieu de comprendre
    
    **✅ Validation** : Test sur de nouvelles données pour vérifier les performances
    
    **🎲 Validation croisée** : Technique pour tester la robustesse du modèle
    """)

with st.expander("🧩 Apprentissage Non-Supervisé - Termes Clés"):
    st.markdown("""
    **🗂️ Clustering** : Regrouper automatiquement des données similaires
    
    **📍 Centroïde** : Point central représentatif d'un groupe
    
    **📏 Distance euclidienne** : Mesure mathématique de proximité entre deux points
    
    **🎯 K-Means** : Algorithme populaire qui divise en K groupes
    
    **🔄 Convergence** : Quand l'algorithme trouve une solution stable
    
    **📊 Inertie** : Mesure de la compacité des groupes formés
    
    **🌳 Clustering hiérarchique** : Crée un arbre de regroupements
    
    **📈 DBSCAN** : Trouve des groupes de densité variable
    
    **🔍 Analyse exploratoire** : Découvrir des patterns cachés dans les données
    
    **📋 Segmentation** : Division des données en sous-groupes homogènes
    """)

with st.expander("🎮 Apprentissage par Renforcement - Termes Clés"):
    st.markdown("""
    **🤖 Agent** : L'entité qui prend des décisions et apprend
    
    **🌍 Environnement** : Le monde dans lequel l'agent évolue
    
    **⚡ Action** : Ce que l'agent peut décider de faire
    
    **🎁 Récompense** : Signal positif ou négatif reçu après une action
    
    **📋 État** : Situation actuelle de l'agent dans l'environnement
    
    **🎯 Politique** : Stratégie que suit l'agent pour choisir ses actions
    
    **💰 Fonction de valeur** : Estimation de la "valeur" d'un état ou action
    
    **🔍 Exploration** : Essayer de nouvelles actions pour apprendre
    
    **⚡ Exploitation** : Utiliser les meilleures actions connues
    
    **📉 Discount factor** : Importance accordée aux récompenses futures
    
    **🎲 Epsilon-greedy** : Stratégie mixant exploration et exploitation
    
    **🔄 Q-Learning** : Algorithme populaire d'apprentissage par renforcement
    """)

with st.expander("🧠 Intelligence Artificielle - Concepts Généraux"):
    st.markdown("""
    **🤖 Intelligence Artificielle (IA)** : Capacité d'une machine à imiter l'intelligence humaine
    
    **📖 Machine Learning (ML)** : Sous-domaine de l'IA qui apprend à partir de données
    
    **🧠 Deep Learning** : ML utilisant des réseaux de neurones profonds
    
    **🌐 Réseau de neurones** : Modèle inspiré du cerveau humain
    
    **⚖️ Algorithme** : Suite d'instructions pour résoudre un problème
    
    **📊 Big Data** : Très grandes quantités de données difficiles à traiter
    
    **🔮 Prédiction** : Estimation d'un résultat futur basée sur des données
    
    **🎯 Optimisation** : Recherche de la meilleure solution possible
    
    **📈 Gradient descent** : Méthode pour minimiser les erreurs du modèle
    
    **🔄 Itération** : Répétition d'un processus pour améliorer les résultats
    
    **📋 Dataset** : Ensemble de données utilisées pour l'entraînement
    
    **🎭 Biais** : Tendance systématique à favoriser certains résultats
    
    **🎲 Variance** : Sensibilité du modèle aux variations des données
    """)

st.markdown("---")
st.markdown("*🎓 Plus vous jouez, plus vous maîtrisez ces concepts !*")