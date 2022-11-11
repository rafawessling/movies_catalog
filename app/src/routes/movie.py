from typing import List
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.src.schemas.movie import MovieSchema
from app.src.controllers.movie import (
    register_movie,
    find_movie_by_title,
    find_movie_by_genre,
    find_movie_by_metascore,
    find_all_movies,
    delete_movie_by_id
)

router = APIRouter(tags=['Movies'], prefix='/movies')

@router.post('/register', summary='Register a movie')
async def post_movie(movie: MovieSchema):
    add_movie = await register_movie(movie)
    return JSONResponse(status_code=200, content=add_movie)

@router.get('/search/{title}', summary='Search movie by name')
async def get_movie(title: str):
    movies = await find_movie_by_title(title)
    return JSONResponse(status_code=200, content=movies)

@router.get('/search/genre/{genre}', summary='Search movie by genre')
async def get_movie_genre(genre: str):
    movies = await find_movie_by_genre(genre)
    return JSONResponse(status_code=200, content=movies)

@router.get('/search/metascore/{metascore}', summary='Search movie by metascore')
async def get_movie_metascore(metascore: int):
    movies = await find_movie_by_metascore(metascore)
    return JSONResponse(status_code=200, content=movies)

@router.get('/all_movies', summary='Get all movies')
async def get_all_movies():
    movies = await find_all_movies()
    return JSONResponse(status_code=200, content=movies)

@router.delete('/register/{id}', summary='Delete a movie')
async def delete_movie(id):
    movies = await delete_movie_by_id(id)
    return JSONResponse(status_code=200, content=movies)