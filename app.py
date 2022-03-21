from flask import Flask
from flask_restful import Api
from resources.movie import MoviesListResource, MovieSingleResource


app = Flask(__name__)
api = Api(app)


api.add_resource(MoviesListResource, '/movies')
api.add_resource(MovieSingleResource, '/movies/<int:movie_id>')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
