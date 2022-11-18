import logging
from fastapi.exceptions import HTTPException
from app.src.schemas.movie import MovieSchema
from app.src.server.database import db
from app.src.services.movie import (
    get_movie_by_title,
    get_movie_by_genre,
    get_media_by_genre,
    get_movie_by_metascore,
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
        existing_movie = await get_movie_by_title(movie.title)
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

async def find_movie_by_title(title):
    """
    Method responsible for getting a movie with `title` as a search key

    Args:
        name: str
    Returns:
        type: list(dict("movie": movie))
        obs: The movie is only returned if it is found the search key in the title
    Raises:
        HTTPException: status_code=400
    """
    try:
        movies = await get_movie_by_title(title)
        if movies is not None:
            return movies
        return {'status': 'No movies found'}
    except Exception as e:
        logger.exception(f'find_movie_by_title.error: {e}')
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

async def find_media_by_genre(type_of_media, genre):
    """
    Method responsible for getting a media with `type` and `genre` as search keys

    Args:
        type_of_media: str
        genre: str
    Returns:
        type: list(dict("movie": movie))
        obs: The media is only returned if it is found the search keys
    Raises:
        HTTPException: status_code=400
    """
    try:
        media = await get_media_by_genre(type_of_media, genre)
        if media is not None:
            return media
        return {'status': 'No movies or series found'}
    except Exception as e:
        logger.exception(f'find_media_by_genre.error: {e}')
        raise HTTPException(status_code=400)

async def find_movie_by_metascore(metascore):
    """
    Method responsible for getting a movie with `metascore` as a search key

    Args:
        metascore: int
    Returns:
        type: list(dict("movie": movie))
        obs: The movie is only returned if the metascore is greater than or equal to the search key
    Raises:
        HTTPException: status_code=400
    """
    try:
        movies = await get_movie_by_metascore(metascore)
        if movies is not None:
            return movies
        return {'status': 'No movies found'}
    except Exception as e:
        logger.exception(f'find_movie_by_metascore.error: {e}')
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
