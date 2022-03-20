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