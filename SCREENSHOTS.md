# 📸 Documentation Visuelle - AI Learning Game

Cette documentation présente les interfaces utilisateur de l'application AI Learning Game avec des descriptions détaillées.

## 🏠 Page d'Accueil

### Interface Principale
```
┌─────────────────────────────────────────────────────────────┐
│  🤖 AI Learning Game                                        │
│  Découvrez l'apprentissage automatique de manière          │
│  interactive !                                             │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│           🏆 Score Total: 25    Questions: 3               │
└─────────────────────────────────────────────────────────────┘

📚 Choisissez votre domaine d'apprentissage :
┌─────────────────────────────────────────────────────────────┐
│ 🔍 Apprentissage supervisé                        ▼        │
└─────────────────────────────────────────────────────────────┘
```

**Description :**
- En-tête coloré avec dégradé bleu-violet
- Compteur de score persistant au centre
- Menu déroulant avec emojis pour la sélection

---

## 🔍 Module Apprentissage Supervisé

### Interface de Classification
```
## 🔍 Apprentissage Supervisé - Classification d'Images

ℹ️ Qu'est-ce que l'apprentissage supervisé ? [Développer ▼]

### 🎯 Défi : Identifiez correctement l'animal !

┌─────────────────────────────────────────────────────────────┐
│                        🐱                                   │
│                                                            │
│               Quel animal voyez-vous ?                     │
└─────────────────────────────────────────────────────────────┘

🤔 Votre réponse : [Chat            ▼]

         ┌─────────────────────────┐
         │  ✅ Valider ma réponse  │
         └─────────────────────────┘

         ┌─────────────────────────┐
         │    🔄 Nouvel animal     │
         └─────────────────────────┘
```

**Éléments interactifs :**
- Zone d'affichage centrée avec fond gris clair
- Menu déroulant avec 6 choix d'animaux
- Boutons centrés et stylisés
- Feedback coloré selon la réponse (vert/rouge)

---

## 🧩 Module Apprentissage Non-Supervisé

### Interface de Clustering
```
## 🧩 Apprentissage Non-Supervisé - Clustering de Données

ℹ️ Qu'est-ce que l'apprentissage non-supervisé ? [Développer ▼]

### 🎯 Défi : Regroupez les données par similarité !

📊 Données clients (Âge vs Revenu) :

┌─────────────────────────────────────────────────────────────┐
│ Client   │ Âge │ Revenu (€) │                              │
│ Client 1 │ 22  │ 25000      │                              │
│ Client 2 │ 25  │ 30000      │                              │
│ ...      │ ... │ ...        │                              │
└─────────────────────────────────────────────────────────────┘

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

### 🤔 Votre analyse :
┌─────────────────────────────────────────────────────────────┐
│ Comment regrouperiez-vous ces clients ?                    │
│ (ex: Jeunes/Seniors, Revenus faibles/élevés)              │
│                                                            │
│ [Zone de texte libre]                                     │
└─────────────────────────────────────────────────────────────┘
```

**Fonctionnalités :**
- Tableau de données interactif avec Pandas
- Graphique ASCII pour la visualisation
- Zone de texte libre pour l'analyse
- Feedback intelligent sur le regroupement

---

## 🎮 Module Apprentissage par Renforcement

### Interface Agent Explorateur
```
## 🎮 Apprentissage par Renforcement - Agent Explorateur

ℹ️ Qu'est-ce que l'apprentissage par renforcement ? [Développer ▼]

📋 RÈGLES DU JEU - À LIRE AVANT DE COMMENCER [Développé ▲]

🎯 Objectif :
Maximisez votre score en naviguant intelligemment !

🗺️ L'environnement :
- Ligne de 5 cases (positions 1 à 5)
- Chaque case = élément différent avec récompense
- Votre position = robot 🤖

🏆 Système de récompenses :
- 🕳️ Piège : -10 points
- 🐍 Serpent : -5 points  
- 💰 Trésor : +15 points
- 💎 Diamant : +25 points

### 🎮 Votre environnement actuel :

Position 1  Position 2  Position 3  Position 4  Position 5
┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
│   🕳️    │ │   💰    │ │   🤖    │ │   🐍    │ │   💎    │
└─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘
                        VOUS ÊTES ICI

🏆 Score Épisode: 15  👣 Pas: 3  💰 Trésors: 1  📍 Position: 3

### 🎯 Choisissez votre prochaine action :

🤖 Vous êtes actuellement en Position 3 sur l'élément 🤖

┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│ Destination:    │ │ Action:         │ │ Destination:    │
│ Position 2 (💰) │ │ Rester immobile │ │ Position 4 (🐍) │
│                 │ │ Conséquence:    │ │                 │
│ ⬅️ Aller à      │ │ -1 point        │ │ ➡️ Aller à      │
│    Gauche       │ │ 🛑 Rester sur   │ │    Droite       │
│                 │ │    Place        │ │                 │
└─────────────────┘ └─────────────────┘ └─────────────────┘
```

**Améliorations apportées :**
- Règles complètes et détaillées dans un expandeur
- Numérotation claire des positions
- Indication visuelle de votre position actuelle
- Aperçu des destinations avant de cliquer
- Conseils stratégiques séparés (exploration vs exploitation)
- Feedback détaillé après chaque action

---

## 📖 Glossaire Intégré

### Interface du Glossaire
```
## 📚 Glossaire - Termes Importants de l'IA

🔍 Recherche rapide : [Tapez un terme...    ]

### 🤖 Apprentissage Automatique (Machine Learning)
Domaine de l'IA qui permet aux ordinateurs d'apprendre...

### 🎯 Apprentissage Supervisé
Type d'apprentissage utilisant des données étiquetées...

### 🧩 Clustering (Regroupement)
Technique d'apprentissage non-supervisé qui groupe...

[... autres termes ...]
```

**Fonctionnalités :**
- Recherche interactive des termes
- Définitions claires avec exemples
- Organisation par catégories
- Liens vers les modules correspondants

---

## 📱 Responsive Design

### Adaptation Mobile
```
📱 Vue Mobile (largeur < 768px)
┌─────────────────────┐
│   🤖 AI Learning    │
│       Game          │
│                     │
│ 🏆 Score: 25        │     ← Condensé sur une ligne
│                     │
│ [Menu déroulant]    │     ← Pleine largeur
│                     │
│ ┌─────────────────┐ │
│ │     🐱          │ │     ← Zone réduite
│ └─────────────────┘ │
│                     │
│ [Bouton pleine     ] │     ← Boutons empilés
│ [largeur          ] │
└─────────────────────┘

🖥️ Vue Desktop (largeur > 768px)
┌─────────────────────────────────────────────────────────────┐
│           🤖 AI Learning Game                               │
│                                                            │
│        🏆 Score: 25      Questions: 3                     │ ← Centré avec métriques
│                                                            │
│    [Menu]              [Zone de jeu]              [Info]   │ ← 3 colonnes
└─────────────────────────────────────────────────────────────┘
```

## 💾 Persistance des Données

### Gestion des Sessions
- **Score total** : Conservé pendant toute la session
- **Progression** : Nombre de questions répondues
- **États des jeux** : Position de l'agent, données actuelles
- **Préférences** : Module sélectionné

### Réinitialisation
- Boutons "Nouvel épisode" / "Nouvelles données"
- Conservation du score global
- Reset des états spécifiques aux modules

---

Cette documentation visuelle aide à comprendre l'interface utilisateur et les interactions possibles dans chaque module de l'application AI Learning Game.
