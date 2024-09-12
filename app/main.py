# Este arquivo inicializa o servidor HTTP e inclui o roteamento.

from fastapi import FastAPI
from src.controler.music_controller import RouteAPI  # Importando a classe RouteAPI

app = FastAPI()

# Instancia a classe RouteAPI e inclui o roteador dela no app
route_api = RouteAPI()
app.include_router(route_api.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)