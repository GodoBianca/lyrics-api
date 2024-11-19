from fastapi import FastAPI
from src.controller.music_controller import MusicController
from src.controller.artist_controller import ArtistController

app = FastAPI()

music_controller = MusicController()
artist_controller = ArtistController()

app.include_router(music_controller.router)
app.include_router(artist_controller.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
