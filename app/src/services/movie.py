from bson import json_util, ObjectId
import json
from app.src.server.database import db

async def get_movie_by_name(name):
    query = {
            "name": {
                "$regex": name,
                "$options": "i"
            }
        }
    movies = list(db.movie_collection.find(query))
    if movies:
        return json.loads(json_util.dumps(movies))
    return None

async def get_all_movies():
    movies = db.movie_collection.find()
    if movies:
        return json.loads(json_util.dumps(movies))
    return None

async def delete_movie_id(id):
    movies = db.movie_collection.delete_one({'_id': ObjectId(id)})
    if movies.deleted_count:
        return True
    return False