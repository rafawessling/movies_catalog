import logging
from fastapi.exceptions import HTTPException
from app.src.schemas.movie import MovieSchema
from app.src.server.database import db
from app.src.services.movie import get_movie_by_name


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