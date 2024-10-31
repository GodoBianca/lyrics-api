# Arquivo main.py: inicializa o servidor HTTP e inclui o roteamento.

from fastapi import FastAPI
from src.controler.music_controller import MusicController
from src.controler.artist_controller import ArtistControler

app = FastAPI()

music_controller = MusicController()
artist_controller = ArtistControler()

app.include_router(music_controller.router)
app.include_router(artist_controller.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)