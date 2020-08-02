import os
import json
import numpy as np
from pathlib import Path
import joblib
from tensorflow.keras.models import load_model
### retreive model and weight

MODEL_PATH = os.path.join(Path(__file__).parent.parent, 'models')

# h1 = joblib.load(f'{MODEL_PATH}/placeholder.txt')

# print(os.path.join(APP_DATA, 'placeholder.txt'))
# with open(f'{MODEL_PATH}/placeholder.txt', 'r') as f:
#     all_lines = f.readlines()
#     print(all_lines)

model = load_model(f'{MODEL_PATH}/ann_pop_model.h5')
scaler = joblib.load(f'{MODEL_PATH}/ann_pop_scaler.pkl')

genre_conversion = {
    'Alternative': 7,
    'Anime': 8,
    'Blues': 9,
    'Childrens': 10,
    'Classical': 11,
    'Comedy': 12,
    'Country': 13,
    'Dance': 14,
    'Electronic': 15,
    'Folk': 16,
    'Hip-Hop': 17,
    'Indie': 18,
    'Jazz': 19,
    'Movie': 20,
    'Opera': 21,
    'Pop': 22,
    'R&B': 23,
    'Rap': 24,
    'Reggae': 25,
    'Reggaeton': 26,
    'Rock': 27,
    'Ska': 28,
    'Soul': 29,
    'Soundtrack': 30,
    'World': 31
}


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


def predict_popularity(acousticness, danceability, energy, instrumentalness,
                       liveness, loudness, speechiness, genre):

    X_test = np.array([[
        acousticness, danceability, energy, instrumentalness, liveness,
        loudness, speechiness, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0
    ]])

    index = int(genre_conversion[genre])

    if (index > 6 and index < 32):
        # choose genre here
        X_test[0][index] = 1
    else:
        # if not in range, choose 'Pop' as genre
        X_test[0][22] = 1

    print(acousticness, danceability, energy, instrumentalness, liveness,
          loudness, speechiness, genre)

    print('X_test --> ', X_test)

    X_scaled = scaler.transform(X_test)
    predict = model.predict(X_scaled)
    arg_max = np.argmax(predict)
    print('arg_max -->', arg_max)

    return (predict[0].tolist(), int(arg_max))
