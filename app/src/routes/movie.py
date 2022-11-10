from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.src.schemas.movie import MovieSchema
from app.src.controllers.movie import (
    register_movie
)

router = APIRouter(tags=['Movies'], prefix='/movies')

@router.post('/register', summary='Register a movie')
async def post_movie(movie: MovieSchema):
    add_movie = await register_movie(movie)
    return JSONResponse(status_code=200, content=add_movie)