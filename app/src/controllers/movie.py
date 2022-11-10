import logging
from fastapi.exceptions import HTTPException
from app.src.schemas.movie import MovieSchema
from app.src.server.database import db
from app.src.services.movie import (
    get_movie_by_name,
    get_all_movies,
    delete_movie_id
)


logger = logging.getLogger(__name__)

async def register_movie(movie: MovieSchema):
    """
    Method responsible for register a movie

    Args:
        movie (MovieSchema)
    Returns:
        type: dict("status": status, "movie": movie)
    Raises:
        HTTPException: status_code = 422
    """
    try:
        existing_movie = await get_movie_by_name(movie.name)
        if existing_movie is None:
            add_movie = db.movie_collection.insert_one(movie.dict())
            
            if add_movie.inserted_id:
                return {
                    'status': 'Movie has been registered',
                    'movie': movie.dict()
                }
        return {'status': 'Movie already exists'}
    except Exception as e:
        logger.exception(f'register_movie.error: {e}')
        raise HTTPException(status_code=422)

async def find_movie_by_name(name):
    """
    Get a movie with `name` as search key

    Args:
        name: str
    Returns:
        type: list(dict("movie": movie))
        obs: The movie is only returned if it is found the search key in the name
    Raises:
        HTTPException: status_code=400
    """
    try:
        movies = await get_movie_by_name(name)
        if movies is not None:
            return movies
        return {'status': 'No movies found'}
    except Exception as e:
        logger.exception(f'find_movie_by_name.error: {e}')
        raise HTTPException(status_code=400)


async def find_all_movies():
    """
    Get all movies registered

    Returns:
        type: list(dict("movie": movie))
        obs: The movie is only returned if it is found the search key in the name
    Raises:
        HTTPException: status_code=400
    """
    try:
        movies = await get_all_movies()
        if movies is not None:
            return movies
        return {'status': 'No movies found'}
    except Exception as e:
        logger.exception(f'find_all_movies.error: {e}')
        raise HTTPException(status_code=400)

async def delete_movie_by_id(id):
    """
    Remove a movie by `id`

    Args:
        _id: str
    Returns:
        type: list(dict("movie": movie))
        obs: The movie is only returned if it is found the search key in the name
    Raises:
        HTTPException: status_code=400
    """
    try:
        movie = await delete_movie_id(id)
        if movie == True:
            return {'status': 'The movie was removed'}
        return {'status': 'No movies found'}
    except Exception as e:
        logger.exception(f'delete_movie_by_id.error: {e}')
        raise HTTPException(status_code=400)
