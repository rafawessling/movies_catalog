from bson import json_util, ObjectId
import json
from app.src.server.database import db

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

async def get_movie_by_genre(genre):
    query = {
            "genre": {
                "$regex": genre,
                "$options": "i"
            }
        }
    movies_genre = list(db.movie_collection.find(query))
    if movies_genre:
        return json.loads(json_util.dumps(movies_genre))
    return None

async def get_movie_by_metascore(metascore):
    movies_metascore = list(db.movie_collection.find({"metascore": {"$gte": metascore}}))
    if movies_metascore:
        return json.loads(json_util.dumps(movies_metascore))
    return None

async def get_all_movies():
    movies = db.movie_collection.find().sort("name")
    if movies:
        return json.loads(json_util.dumps(movies))
    return None

async def delete_movie_id(id):
    movies = db.movie_collection.delete_one({'_id': ObjectId(id)})
    if movies.deleted_count:
        return True
    return False