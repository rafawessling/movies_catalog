from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.src.schemas.movie import MovieSchema, MovieUpdateSchema
from app.src.controllers.movie import (
    find_all_movies,
    register_movie,
    find_movie_by_title,
    find_movie_by_genre,
    update_movie_by_id,
    delete_movie_by_id
)

router = APIRouter(tags=['Movies and Series'], prefix='')

@router.get('/movies/', summary='Get Movies')
async def get_all_movies():
    movies = await find_all_movies()
    return JSONResponse(status_code=200, content=movies)

@router.post('/movies/', summary='Create Movies')
async def post_movie(movie: MovieSchema):
    add_movie = await register_movie(movie)
    return JSONResponse(status_code=200, content=add_movie)

@router.get('/movies/{title}', summary='Get Movies By Title')
async def get_movie(title: str):
    movies = await find_movie_by_title(title)
    return JSONResponse(status_code=200, content=movies)

@router.get('/movies/{type_of_movie}/{genre}', summary='Get Movies or Series By Genre')
async def get_movie_by_genre(type_of_movie: str, genre: str):
    movies = await find_movie_by_genre(type_of_movie, genre)
    return JSONResponse(status_code=200, content=movies)

@router.put('/movies/{id}', summary='Update Movies')
async def update_movie(id, movie: MovieUpdateSchema):
    movie = await update_movie_by_id(id, movie)
    return JSONResponse(status_code=200, content=movie)

@router.delete('/movies/{id}', summary='Delete Movies')
async def delete_movie(id):
    movies = await delete_movie_by_id(id)
    return JSONResponse(status_code=200, content=movies)