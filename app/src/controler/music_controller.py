# Este arquivo contém as rotas da API e chama os métodos do service.

from fastapi import APIRouter, HTTPException
from src.service.music_service import MusicService
from uuid import UUID

# Cria uma instancia da classe musicService que esta na pasta service
music_service = MusicService()

# Definição da classe routeAPI
class RouteAPI:
    # O init ele é o construtor da classe, e inicializa uma instancia de APIRouter e define as 4 rotas 
    def __init__(self):
        # O router ele e da lib fastAPI e ajuda a modularizar e organizar as rotas, então aqui estou criando uma instancia do APIRouter que servira como um container para as rotas
        self.router = APIRouter()
        self.router.get("/music/{music_id}", response_model=dict)(self.get_music)
        self.router.post("/music", response_model=dict)(self.create_music)
        self.router.put("/music/{music_id}", response_model=dict)(self.update_music)
        self.router.delete("/music/{music_id}")(self.delete_music)

    async def get_music(self, music_id: UUID):
        music = music_service.find(music_id)
        if not music:
            raise HTTPException(status_code=404, detail="Music not found")
        return music

    async def create_music(self, music: dict):
        created_music = music_service.insert(music)
        return created_music  # Retorna o objeto com o ID gerado

    async def update_music(self, music_id: UUID, updated_music: dict):
        music = music_service.update(music_id, updated_music)
        if not music:
            raise HTTPException(status_code=404, detail="Music not found")
        return music

    async def delete_music(self, music_id: UUID):
        if not music_service.delete(music_id):
            raise HTTPException(status_code=404, detail="Music not found")
        return {"message": "Music deleted successfully"}
