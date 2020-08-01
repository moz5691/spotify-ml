import os
from pathlib import Path
import joblib

MODEL_PATH = os.path.join(Path(__file__).parent.parent, 'models')

# h1 = joblib.load(f'{MODEL_PATH}/placeholder.txt')

# print(os.path.join(APP_DATA, 'placeholder.txt'))
# with open(f'{MODEL_PATH}/placeholder.txt', 'r') as f:
#     all_lines = f.readlines()
#     print(all_lines)


def predict_popularity(acousticness, danceability, duration_ms, energy,
                       instrumentalness):

    ## implement here.
    fixed = 123
    print(acousticness, danceability, duration_ms, energy, instrumentalness)

    return float(fixed)
