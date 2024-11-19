from fastapi import APIRouter, HTTPException
from uuid import UUID
from src.service.artist_service import ArtistService
from src.model.artist_model import ArtistModel

artist_service = ArtistService()

class ArtistController:
    def __init__(self):
        self.router = APIRouter()
        self.router.get("/artists/{id}", response_model=ArtistModel)(self.get_artist)
        self.router.post("/artists", response_model=ArtistModel)(self.create_artist)
        self.router.put("/artists/{id}", response_model=ArtistModel)(self.update_artist)
        self.router.delete("/artists/{id}")(self.delete_artist)
        
    async def get_artist(self, id: UUID):
        artist = artist_service.find(id)
        if not artist:
            raise HTTPException(status_code=404, detail="Artist not found")
        return artist

    async def create_artist(self, model: ArtistModel):
        if not model.name:
            raise HTTPException(status_code=400, detail="Artist name is required")
        created_artist = artist_service.insert(model)
        return created_artist

    async def update_artist(self, id: UUID, update_artist: ArtistModel):
        updated_artist = artist_service.update(id, update_artist)
        if not updated_artist:
            raise HTTPException(status_code=404, detail="Artist not found")
        return updated_artist

    async def delete_artist(self, id: UUID):
        if not artist_service.delete(id):
            raise HTTPException(status_code=404, detail="Artist not found")
        return {"message": "Artist deleted successfully"}
