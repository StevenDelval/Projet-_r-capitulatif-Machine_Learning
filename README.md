# Les Gens N'ont Plus de Goût
## Description
Les Gens N'ont Plus de Goût est une application web développée dans le cadre du département marketing de notre entreprise spécialisée dans les rééditions d'albums de musique légendaires au format vinyle. Cette application permet de répondre à une question simple : "En se basant sur les caractéristiques musicales d'un morceau, est-ce qu'un tube sorti il y a des années et qui est devenu un classique aurait connu le même succès s'il avait été sorti récemment?".

Pour cela, nous avons étudié le lien entre les caractéristiques musicales des morceaux sortis en 2022 et leur popularité, afin d'appliquer ce modèle à n'importe quel morceau de l'histoire de la musique, en particulier du catalogue de notre entreprise. Nous avons utilisé l'API du service Spotify pour collecter des données et avons entraîné plusieurs modèles de machine learning. Nous avons fixé comme objectif une MAE maximum d'environ 20 pour notre modèle.

## Installation
1. Clonez le dépôt git :
```bash
git clone https://github.com/votrenom/Les-Gens-Nont-Plus-de-Gout.git
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

2. Rendez-vous sur l'URL suivante :
```bash
http://localhost:8000/
```

3. Entrez le titre et l'artiste de la musique que vous souhaitez tester et cliquez sur "Envoyer".

4. Le résultat s'affiche sous forme de pourcentage de popularité estimé si la musique avait été sortie en 2022.


## Déploiement
Nous avons déployé notre application sur Azure en utilisant Docker et Docker Compose. Les fichiers de configuration nécessaires se trouvent dans le dépôt git.

## Auteurs
- Benji, Cédric, Emad, Steven

## Références
- [codepen](https://codepen.io/devparth/pen/dxpKKZ)