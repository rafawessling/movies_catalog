from bson import json_util
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