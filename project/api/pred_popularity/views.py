# popularity
# acousticness
# danceability
# duration_ms
# energy
# instrumentalness

from project.api.pred_popularity.crud import (predict_popularity)

from flask import request
from flask_restx import Resource, Api, fields, Namespace

pred_popularity_namespace = Namespace("pred_popularity")

pred_popularity = pred_popularity_namespace.model(
    'Pred_Popularity', {
        'acousticness': fields.Float(),
        'danceability': fields.Float(),
        'duration_ms': fields.Float(),
        'energy': fields.Float(),
        'instrumentalness': fields.Float(),
    })


class PredPopularity(Resource):
    @pred_popularity_namespace.expect(pred_popularity, validate=True)
    @pred_popularity_namespace.response(201, "New entry was added!")
    def post(self):
        """Create a new entry for predicton"""
        post_data = request.get_json()
        acousticness = post_data.get("acousticness")
        danceability = post_data.get("danceability")
        duration_ms = post_data.get("duration_ms")
        energy = post_data.get("energy")
        instrumentalness = post_data.get("instrumentalness")
        response_object = {}

        response = predict_popularity(acousticness, danceability, duration_ms,
                                      energy, instrumentalness)
        response_object = {'pouplarity': response}
        return response_object, 201


pred_popularity_namespace.add_resource(PredPopularity, '')