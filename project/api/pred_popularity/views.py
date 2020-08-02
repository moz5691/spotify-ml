from flask import request
from flask_restx import Resource, Api, fields, Namespace

from project.api.pred_popularity.crud import predict_popularity

pred_popularity_namespace = Namespace(
    "pred_popularity", description="Data Input for Popularity Prediction")

pred_popularity = pred_popularity_namespace.model(
    'Pred_Popularity', {
        'acousticness':
        fields.Float(required=True, description="Float, Min:0, Max:1"),
        'danceability':
        fields.Float(required=True, description="Float, Min:0, Max:1"),
        'energy':
        fields.Float(required=True, description="Float, Min:0, Max:1"),
        'instrumentalness':
        fields.Float(required=True, description="Float, Min:0, Max:1"),
        'liveness':
        fields.Float(required=True, description="Float, Min:0, Max:1"),
        'loudness':
        fields.Float(required=True,
                     description="Float, Min:-52, Max:3.8, unit dB"),
        'speechiness':
        fields.Float(required=True, description="Float, Min:0, Max:1"),
        'genre':
        fields.String(
            required=True,
            description=
            "String, [Alternative,Anime,Blues,Childrens,Classical,Comedy,Country,Dance,Electronic,Folk,Hip-Hop,Indie,Jazz,Movie,Opera,Pop,R&B,Rap,Reggae,Reggaeton,Rock,Ska,Soul,Soundtrack,World]"
        ),
    })


class PredPopularity(Resource):
    @pred_popularity_namespace.expect(pred_popularity, validate=True)
    @pred_popularity_namespace.response(201, "New entry was added!")
    def post(self):
        """Create a new entry for predicton"""
        post_data = request.get_json()
        acousticness = post_data.get("acousticness")
        danceability = post_data.get("danceability")
        energy = post_data.get("energy")
        instrumentalness = post_data.get("instrumentalness")
        liveness = post_data.get("liveness")
        loudness = post_data.get("loudness")
        speechiness = post_data.get("speechiness")
        genre = post_data.get("genre")
        response_object = {}

        response = predict_popularity(acousticness=acousticness,
                                      danceability=danceability,
                                      energy=energy,
                                      instrumentalness=instrumentalness,
                                      liveness=liveness,
                                      loudness=loudness,
                                      speechiness=speechiness,
                                      genre=genre)

        print('response--->', response)
        response_object = {'probability': response[0], 'class': response[1]}
        return response_object, 201


pred_popularity_namespace.add_resource(PredPopularity, '')