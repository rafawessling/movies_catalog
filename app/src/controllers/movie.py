import logging
from fastapi.exceptions import HTTPException
from app.src.schemas.movie import MovieSchema
from app.src.server.database import db
from app.src.services.movie import (
    get_movie_by_name,
    get_movie_by_genre,
    get_all_movies,
    delete_movie_id
)


logger = logging.getLogger(__name__)

async def register_movie(movie: MovieSchema):
    """
    Method responsible for registering a movie

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
    Method responsible for getting a movie with `name` as a search key

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

async def find_movie_by_genre(genre):
    """
    Method responsible for getting a movie with `genre` as a search key

    Args:
        genre: str
    Returns:
        type: list(dict("movie": movie))
        obs: The movie is only returned if it is found the search key in the genre
    Raises:
        HTTPException: status_code=400
    """
    try:
        movies = await get_movie_by_genre(genre)
        if movies is not None:
            return movies
        return {'status': 'No movies found'}
    except Exception as e:
        logger.exception(f'find_movie_by_genre.error: {e}')
        raise HTTPException(status_code=400)

async def find_all_movies():
    """
    Method responsible for getting all movies registered

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
    Method responsible for removing a movie by `id`

    Args:
        id: str
    Returns:
        type: ("status": status)
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
