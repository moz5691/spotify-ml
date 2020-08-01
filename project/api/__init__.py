from flask_restx import Api

from project.api.ping import ping_namespace
from project.api.pred_danceability.views import pred_danceability_namespace
from project.api.pred_popularity.views import pred_popularity_namespace

api = Api(version='1.0', title='Data project #3 API', doc='/doc/')

api.add_namespace(ping_namespace, path="/api/v1/ping")
api.add_namespace(pred_popularity_namespace, path="/api/v1/popularity")
api.add_namespace(pred_danceability_namespace, path="/api/v1/danceability")