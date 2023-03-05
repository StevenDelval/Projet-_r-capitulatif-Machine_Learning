[Version française](README.md)

# People are out of taste
## Description
*People are out of taste* is a Web Application developed as part of the Artificial Intelligence Dev-IA training course at Simplon.

### Project script

You work for a company specializing in the reissue of legendary music albums in vinyl format. The marketing department missioned you with the following project: based on songs' musical characteristics, would a hit released in the 80s that became a classic have had the same success if it were recently released?

To answer the question, we studied the link between the musical features of songs released in 2022 and their current popularity, according to Spotify data.

We used the Spotipy library to query Spotify's API, and collected data in order to train several Machine Learning models: one for Genre Prediction, and the other for Popularity Prediction.

Through our Web Application, users can query the model on any piece of music history.

## Installation
1. Clone the git repository:
```bash
git clone https://github.com/StevenDelval/Projet-_recapitulatif-Machine_Learning
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Launch the Web Application:
```bash
python manage.py runserver
```

2. Go to the following URL: http://localhost:8000/

3. Enter the title and artist of the music you want to test and click on "Envoyer".

The result is displayed with our estimated popularity score.

## Deployment
We deployed our application as a Docker container to Microsoft Azure.
The required configuration files are in the git repository.

## Authors
- Benji, Cedric, Emad, Steven

## References
- [codepen](https://codepen.io/devparth/pen/dxpKKZ)
- [MusicBrainz Database](https://musicbrainz.org/doc/MusicBrainz_Database)
- [Wikipedia - Albums released in 2022](https://en.wikipedia.org/wiki/List_of_2022_albums_(January%E2%80%93June))
