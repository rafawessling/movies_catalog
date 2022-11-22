from bson import json_util, ObjectId
import json
from app.src.server.database import db

async def get_all_movies():
    movies = db.movie_collection.find().sort("title")
    if movies:
        return json.loads(json_util.dumps(movies))
    return None

async def get_movie_by_title(title):
    query = {
            "title": {
                "$regex": title,
                "$options": "i"
            }
        }
    movies = list(db.movie_collection.find(query))
    if movies:
        return json.loads(json_util.dumps(movies))
    return None

async def get_movie_by_genre(type_of_movie, genre):
    query = {
            "type_of_media": {
                "$regex": type_of_movie,
                "$options": "i"
            }
        }
    movie_type = list(db.movie_collection.find(query))
    if movie_type:
        query_2 = {
            "genre": {
                "$regex": genre,
                "$options": "i"
            }
        }
        movie_genre = list(db.movie_collection.find(query_2))
        if movie_genre:
            return json.loads(json_util.dumps(movie_genre))
        return None
    return None

async def update_movie_id(id, movie):
    movie = {key: value for key, value in movie if value is not None}
    updated_movie = db.movie_collection.update_one(
        {'_id': ObjectId(id)},
        {'$set': movie}
    )
    if updated_movie.modified_count:
        return True
    return False

async def delete_movie_id(id):
    movies = db.movie_collection.delete_one({'_id': ObjectId(id)})
    if movies.deleted_count:
        return True
    return False