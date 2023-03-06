[English version](README-en.md)

# Les Gens N'ont Plus de Goût
## Description
*Les Gens N'ont Plus de Goût* est une Application Web développée dans le cadre de la formation Intelligence Artificielle Dev-IA de Simplon.

### Scénario du projet

Vous travaillez pour une entreprise spécialisée dans la réédition d'albums de musique légendaires au format vinyle. Le département marketing vous demande de répondre à la problématique suivante : "En se basant sur les caractéristiques musicales des morceaux, est-ce qu'un tube sorti dans les années 80 et qui est devenu un classique aurait connu le même succès s'il était sorti récemment ?"

Pour répondre à la question, nous avons étudié le lien entre les caractéristiques musicales de morceaux sortis en 2022 et leur popularité actuelle (selon les informations de Spotify).

Nous avons utilisé la bibliothèque Spotipy afin d'interroger l'API de Spotify, et avons collecté des données pour entraîner deux modèles de Machine Learning : l'un pour la prédiction de genre, et l'autre pour la prédiction de popularité.

Grâce à l'Application Web, les utilisateurs peuvent interroger le modèle sur n'importe quel morceau de l'histoire de la musique.


## Installation
1. Clonez le dépôt git :
```bash
git clone https://github.com/StevenDelval/Projet-_recapitulatif-Machine_Learning
```

2. Créez un environnement virtuel :
```bash
python -m venv venv
```

3. Activez l'environnement virtuel :
```bash
source venv/bin/activate
```

4. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## Utilisation

1. Lancez l'application web :
```bash
python manage.py runserver
```

2. Rendez-vous sur l'URL suivante : http://localhost:8000/


3. Entrez le titre et l'artiste de la musique que vous souhaitez tester et cliquez sur "Envoyer".

4. Le résultat s'affiche sous forme de pourcentage de popularité estimée si la musique était sortie en 2022.

## Déploiement
Nous avons déployé notre application sur Azure en utilisant Docker. Les fichiers de configuration nécessaires se trouvent dans le dépôt git.

## Auteurs
- Benji, Cédric, Emad, Steven

## Références
- [codepen](https://codepen.io/devparth/pen/dxpKKZ)
- [Base de données MusicBrainz](https://musicbrainz.org/doc/MusicBrainz_Database)
- [Wikipedia - Albums sortis en 2022](https://en.wikipedia.org/wiki/List_of_2022_albums_(January%E2%80%93June))
