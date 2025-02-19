# IBM Quantum - Exercice Qiskit

## 🎯 Objectif

Ce projet soumet un circuit quantique simple à IBM Quantum via Qiskit et affiche l'ID du job envoyé.


## 🛠 Installation

## 1️⃣ Prérequis

Créer un compte IBM Quantum : IBM Quantum

Installer Python (3.8+ recommandé)

WSL ou venv recommandé (si nécessaire)

## 2️⃣ Installer les dépendances

Exécute la commande suivante dans un terminal :

pip install qiskit qiskit-ibm-provider python-dotenv

## 3️⃣ Configurer la clé API

IBM Quantum nécessite une authentification via une clé API. Pour la récupérer :

Connecte-toi à IBM Quantum

Va dans Account Settings

Copie ta clé API

Ajoute ensuite cette clé dans un fichier .env à la racine du projet :

IBMQ_API_TOKEN="ta_cle_api_ici"

💡 Ne jamais partager cette clé API ! Assure-toi d'ajouter .env dans .gitignore.

## 🚀 Utilisation

Exécute le script principal :

python main.py

Si tout fonctionne, on obtient un Job ID similaire à :

>>> Job ID: cyttv5478z600082p4m0

## 📂 Structure du projet

/

├── .env            # Contient la clé API (non inclus dans Git)

├── main.py         # Script principal

├── README.md       # Documentation du projet



