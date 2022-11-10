from fastapi import FastAPI
import uvicorn
from app.src.routes import movie

app = FastAPI(
    title="Movie Catalog",
    version="01"
    )

app.include_router(movie.router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)