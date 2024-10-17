# Este arquivo contém as rotas da API e chama os métodos do service.
from fastapi import APIRouter, HTTPException, Query
from src.service.music_service import MusicService
from uuid import UUID
from src.model.music_model import MusicModel

music_service = MusicService()


class MusicController:
    def __init__(self):
        self.router = APIRouter()
        self.router.get(
            "/musics/{id}", response_model=MusicModel)(self.get_music)
        self.router.post(
            "/musics", response_model=MusicModel)(self.create_music)
        self.router.put(
            "/musics/{id}", response_model=MusicModel)(self.update_music)
        self.router.delete("/musics/{id}")(self.delete_music)

    async def get_music(self, id: UUID):
        musics = music_service.find(id)
        if not musics:
            raise HTTPException(status_code=404, detail="ID or ArtistId not found")
        return musics
    #Nao validei se o artistId pois nao faz sentido

    async def create_music(self, music: MusicModel):
        if not music.artist_id:
            raise HTTPException(status_code=400, detail="ArtistId is required")
        created_music = music_service.insert(music)
        return created_music

    async def update_music(self, id: UUID, updated_music: MusicModel):
        if not updated_music.artist_id:
            raise HTTPException(status_code=400, detail="ArtistId is required")
        musics = music_service.update(id, updated_music)
        if not musics:
            raise HTTPException(status_code=404, detail="ID not found")
        return musics

    async def delete_music(self, id: UUID):
        if not music_service.delete(id):
            raise HTTPException(status_code=404, detail="ID not found")
        return {"message": "Music deleted successfully"}
