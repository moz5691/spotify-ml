### ML import here.
import os
from pathlib import Path
import joblib

MODEL_PATH = os.path.join(Path(__file__).parent.parent, 'models')


def predict_danceability(acousticness, popularity, duration_ms, energy,
                         instrumentalness):

    ## implement here.
    fixed = 12345

    return float(fixed)
