
# Mon Application ChatGPT avec Streamlit

Ce projet est une application de chat simple utilisant Streamlit et le modèle ChatOpenAI de LangChain pour créer un chat interactif avec ChatGPT.

## Prérequis

Avant de commencer, assurez-vous d'avoir Python installé sur votre machine. Ce projet a été testé avec Python 3.8 et supérieur. Vous aurez également besoin de pip pour installer les dépendances.

## Installation

Suivez ces étapes pour configurer l'environnement de développement et exécuter l'application.

### 1. Cloner le dépôt

Clonez ce dépôt sur votre machine locale en utilisant la commande suivante :

```bash
git clone https://github.com/Nelly-98/Create-ChatGPT.git
cd Create-ChatGPT
```

### 2. Créer un environnement virtuel

Il est recommandé de créer un environnement virtuel pour isoler les dépendances du projet. Utilisez la commande suivante pour créer un environnement virtuel :

```bash
python -m venv .venv
```

Activez l'environnement virtuel avec :

- Sur Windows :

```bash
.venv\Scripts\activate
```

- Sur macOS et Linux :

```bash
source .venv/bin/activate
```

### 3. Installer les dépendances

Installez les dépendances nécessaires en utilisant `pip` :

```bash
pip install -r requirements.txt
```

### 4. Configuration des variables d'environnement

Dans le fichier `.env` à la racine du projet, ajoutez votre clé API OpenAI :

```plaintext
OPENAI_API_KEY=votre_clé_api
```

Remplacez `votre_clé_api` par votre clé API OpenAI.

## Lancement de l'application

Pour lancer l'application, exécutez la commande suivante dans le terminal :

```bash
streamlit run main.py
```

Streamlit ouvrira automatiquement l'application dans votre navigateur par défaut. 

## Utilisation

Une fois l'application lancée, vous pouvez interagir avec ChatGPT en saisissant des messages dans le champ de texte et en observant les réponses générées.

