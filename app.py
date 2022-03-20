from flask import Flask
from flask_restful import Api
from resources.movie import MoviesListResource


app = Flask(__name__)
api = Api(app)


api.add_resource(MoviesListResource, '/movies')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
