# Este arquivo inicializa o servidor HTTP e inclui o roteamento.

from fastapi import FastAPI
from src.controler.music_controller import MusicController 

app = FastAPI()

route_api = MusicController()
app.include_router(route_api.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)