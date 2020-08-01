# popularity
# acousticness
# danceability
# duration_ms
# energy
# instrumentalness

from flask import request
from flask_restx import Resource, Api, fields, Namespace

from project.api.pred_danceability.crud import (predict_danceability)

pred_danceability_namespace = Namespace("pred_danceability")

pred_danceability = pred_danceability_namespace.model(
    'Pred_Danceability', {
        'acousticness': fields.Float(),
        'popularlity': fields.Float(),
        'duration_ms': fields.Float(),
        'energy': fields.Float(),
        'instrumentalness': fields.Float(),
    })


class PredDanceability(Resource):
    @pred_danceability_namespace.expect(pred_danceability, validate=True)
    @pred_danceability_namespace.response(201, "New entry was added!")
    def post(self):
        """Create a new entry for predicton"""
        post_data = request.get_json()
        acousticness = post_data.get("acousticness")
        popularity = post_data.get("popularity")
        duration_ms = post_data.get("duration_ms")
        energy = post_data.get("energy")
        instrumentalness = post_data.get("instrumentalness")
        response_object = {}

        response = predict_danceability(acousticness=acousticness,
                                        popularity=popularity,
                                        duration_ms=duration_ms,
                                        energy=energy,
                                        instrumentalness=instrumentalness)
        response_object = {'danceability': response}
        return response_object, 201


pred_danceability_namespace.add_resource(PredDanceability, '')