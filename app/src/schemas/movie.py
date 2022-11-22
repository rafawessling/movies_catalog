import re
from typing import Optional
from pydantic import BaseModel, Field, validator
from fastapi import HTTPException


class MovieSchema(BaseModel):
    title: str = Field(..., unique = True, min_length=1, max_length=80, description="Name",)
    release_date: str = Field(..., description="Release date")
    runtime: int = Field(..., ge=1, description="Runtime in minutes")
    genre: str = Field(..., min_length=3, max_length=50, description="Genre")
    director: str = Field(..., min_length=3, max_length=200, description="Director")
    actors: str = Field(..., min_length=3, max_length=200, description="Actors")
    plot: str = Field(..., min_length=3, max_length=1200, description="Plot")
    language: str = Field(..., min_length=3, max_length=50, description="Language")
    country: str = Field(..., min_length=3, max_length=200, description="Country")
    poster: Optional[str] = Field(None, min_length=3, description="Poster")
    metascore: int = Field(..., ge=1, le=100, description="Metascore")
    type_of_media: str = Field(..., min_length=3, max_length=10, description="Type")
    production: Optional[str] = Field(None, min_length=3, max_length=250, description="Production companies")

    class Config:
        schema_extra = {
            "example": {
                "title": "Interstellar",
                "release_date": "2014-11-07",
                "runtime": 169,
                "genre": "Adventure, Drama, Sci-Fi",
                "director": "Christopher Nolan",
                "actors": "Matthew McConaughey, Anne Hathaway, Jessica Chastain",
                "plot": "Earth's future has been riddled by disasters, famines, and droughts. There is only one way to ensure mankind's survival: Interstellar travel. A newly discovered wormhole in the far reaches of our solar system allows a team of astronauts to go where no man has gone before, a planet that may have the right environment to sustain human life.",
                "language": "English",
                "country": "United States, United Kingdom, Canada",
                "poster": "https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg",
                "metascore": 7,
                "type_of_media": "Movie",
                "production": "Paramount Pictures, Warner Bros. Pictures, Legendary Pictures, Syncopy, Lynda Obst Productions"
            }
        }
    
    @validator("release_date")
    def date_validation(cls, v):
        pattern = r"\d{4}\-\d{2}\-\d{2}"
        
        if not re.match(pattern, v):
            raise HTTPException(
                status_code=400,
                detail="Pattern of release date: YYYY-MM-DD")
        return v

class MovieUpdateSchema(BaseModel):
    title: Optional[str] = Field(None, unique = True, min_length=1, max_length=80, description="Name",)
    release_date: Optional[str] = Field(None, description="Release date")
    runtime: Optional[str] = Field(None, description="Runtime in minutes")
    genre: Optional[str] = Field(None, min_length=3, max_length=50, description="Genre")
    director: Optional[str] = Field(None, min_length=3, max_length=200, description="Director")
    actors: Optional[str] = Field(None,min_length=3, max_length=200, description="Actors")
    plot: Optional[str] = Field(None, min_length=3, max_length=1200, description="Plot")
    language: Optional[str] = Field(None, min_length=3, max_length=50, description="Language")
    country: Optional[str] = Field(None, min_length=3, max_length=200, description="Country")
    poster: Optional[str] = Field(None, min_length=3, description="Poster")
    metascore: Optional[str] = Field(None, description="Metascore")
    type_of_media: Optional[str] = Field(None, min_length=3, max_length=10, description="Type")
    production: Optional[str] = Field(None, min_length=3, max_length=250, description="Production companies")

    class Config:
        schema_extra = {
            "example": {
                "metascore": 75
            }
        }