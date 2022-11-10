from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.src.schemas.movie import MovieSchema
from app.src.controllers.movie import (
    register_movie,
    find_movie_by_name
)

router = APIRouter(tags=['Movies'], prefix='/movies')

@router.post('/register', summary='Register a movie')
async def post_movie(movie: MovieSchema):
    add_movie = await register_movie(movie)
    return JSONResponse(status_code=200, content=add_movie)

@router.get('/search', summary='Search movie by name')
async def get_movie(name: str):
    movies = await find_movie_by_name(name)
    return JSONResponse(status_code=200, content=movies)