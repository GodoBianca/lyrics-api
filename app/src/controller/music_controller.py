from fastapi import APIRouter, HTTPException
from uuid import UUID
from src.service.music_service import MusicService
from src.model.music_model import MusicModel

music_service = MusicService()

class MusicController:
    def __init__(self):
        self.router = APIRouter()
        self.router.get("/musics/{id}", response_model=MusicModel)(self.get_music)
        self.router.post("/musics", response_model=MusicModel)(self.create_music)
        self.router.put("/musics/{id}", response_model=MusicModel)(self.update_music)
        self.router.delete("/musics/{id}")(self.delete_music)
        
    async def get_music(self, id: UUID):
        music = music_service.find(id)
        if not music:
            raise HTTPException(status_code=404, detail="Music not found")
        return music
        
    async def create_music(self, model: MusicModel):
        if not model.title or not model.content or not model.artist_id:
            raise HTTPException(status_code=400, detail="All fields are required")
        try:
            created_music = music_service.insert(model)
            return created_music
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        
        # async def create_music(self, model: MusicModel):
        # if not model.title or not model.content or not model.artist_id:
        #     raise HTTPException(status_code=400, detail="All fields are required")
        
        # created_music = music_service.insert(model)  # Chama o serviço para salvar
        # return created_music

    async def update_music(self, id: UUID, update_music: MusicModel):
        try:
            update_music.id = id
            updated_music = music_service.update(update_music)
            if not updated_music:
                raise HTTPException(status_code=404, detail="Music not found")
            return updated_music
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
    
    async def delete_music(self, id: UUID):
        if not music_service.delete(id):
            raise HTTPException(status_code=404, detail="Music not found")
        return {"message": "Music deleted successfully"}
