from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.movie import Movie, movies_list

class MoviesListResource(Resource):
    def get(self):
        data = []
        for movie in movies_list:
            data.append(movie.data)
        return {'data':data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()
        newMovie = Movie(title=data['title'],
                            year=data['year'],
                            description=data['description'])
        movies_list.append(newMovie)
        return newMovie.data, HTTPStatus.CREATED

class MovieSingleResource(Resource):
    def get(self, movie_id):
        movie = next((movie for movie in movies_list if movie.id == movie_id ), None)
        if movie is None:
            return {'message': 'movie not found'}, HTTPStatus.NOT_FOUND
        return movie.data, HTTPStatus.OK

    def put(self, movie_id):
        data = request.get_json()
        movie = next((movie for movie in movies_list if movie.id == movie_id), None)
        if movie is None:
            return {'message': 'movie not found'}, HTTPStatus.NOT_FOUND
        movie.title = data['title']
        movie.year = data['year']
        movie.description = data['description']
        return movie.data, HTTPStatus.OK
