try:
    import streamlit as st
    import random
except ModuleNotFoundError:
    print("Le module 'streamlit' n'est pas installé. Veuillez l'installer avec 'pip install streamlit'.")
    exit()

# Configuration de l'application
st.title("Jeu éducatif sur l'apprentissage automatique")
st.write("Découvrez les trois types d'apprentissage : supervisé, non-supervisé et par renforcement !")

# Sélection du type d'apprentissage
type_apprentissage = st.selectbox("Choisissez un type d'apprentissage :", [
    "Apprentissage supervisé",
    "Apprentissage non-supervisé",
    "Apprentissage par renforcement"
])

if type_apprentissage == "Apprentissage supervisé":
    st.subheader("Apprentissage supervisé - Jeu de classification")
    st.write("Identifiez si l'image correspond au bon label !")
    images = {"Chat": "🐱", "Chien": "🐶", "Oiseau": "🐦"}
    label_correct, image = random.choice(list(images.items()))
    st.write(f"Image : {image}")
    label_utilisateur = st.selectbox("Quel est le bon label ?", list(images.keys()))
    if st.button("Valider"):
        if label_utilisateur == label_correct:
            st.success("Bonne réponse !")
        else:
            st.error(f"Mauvaise réponse. C'était {label_correct}.")
    st.write("### Explication :")
    st.write("L'apprentissage supervisé consiste à entraîner un modèle avec des données labellisées. Ici, vous avez identifié un élément à partir d'exemples connus.")

elif type_apprentissage == "Apprentissage non-supervisé":
    st.subheader("Apprentissage non-supervisé - Regroupement de données")
    st.write("Regroupez les éléments selon leur similarité !")
    donnees = [random.randint(1, 10) for _ in range(6)]
    st.write(f"Données à analyser : {donnees}")
    groupes = st.text_input("Proposez un regroupement (ex: 1-5, 6-10)")
    if st.button("Valider"):
        st.info("Il n'y a pas de réponse unique, l'important est d'identifier les similarités !")
    st.write("### Explication :")
    st.write("L'apprentissage non-supervisé consiste à identifier des motifs cachés dans les données sans labels. Ici, vous avez regroupé des nombres selon leurs ressemblances.")

elif type_apprentissage == "Apprentissage par renforcement":
    st.subheader("Apprentissage par renforcement - Jeu de récompenses")
    st.write("Aidez l'agent à maximiser sa récompense !")
    actions = ["Gauche", "Droite", "Sauter"]
    action_choisie = st.selectbox("Choisissez une action :", actions)
    recompense = random.choice([-10, 0, 10])
    if st.button("Exécuter l'action"):
        st.write(f"Vous avez choisi : {action_choisie}")
        if recompense > 0:
            st.success("Bonne action ! Vous avez gagné des points.")
        elif recompense == 0:
            st.warning("Action neutre, aucun effet.")
        else:
            st.error("Mauvaise action, perte de points !")
    st.write("### Explication :")
    st.write("L'apprentissage par renforcement consiste à apprendre par essais et erreurs en recevant des récompenses. Ici, vous avez testé différentes actions et observé leurs effets.")
