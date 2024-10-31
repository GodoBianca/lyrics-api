from fastapi import APIRouter, HTTPException, Query
from src.service.artist_service import ArtistService
from uuid import UUID
from src.model.artist_model import ArtistModel

artist_service = ArtistService()

class ArtistControler:
    def __init__(self):
        self.router = APIRouter()
        self.router.get("/artists/{artist_id}", response_model=ArtistModel)(self.get_artist)
        self.router.post("/artists", response_model=ArtistModel)(self.create_artist)
        self.router.put("/artists/{artist_id}", response_model=ArtistModel)(self.update_artist)
        self.router.delete("/artists/{artist_id}")(self.delete_artist)
        
    async def get_artist(self, artist_id: UUID):
        artist = artist_service.find(artist_id)
        if not artist:
            raise HTTPException(status_code=404, detail="Artist not found")
        return artist

    async def create_artist(self, model: ArtistModel):
        if not model.name:
            raise HTTPException(status_code=400, detail="ArtistId is required")
        created_artist = artist_service.insert(model)
        return created_artist

    async def update_artist(self, artist_id: UUID, update_artist: ArtistModel):
        artists = artist_service.update(artist_id, update_artist)
        if not artists:
            raise HTTPException(status_code=404, detail="Artist not found")
        return artists

    async def delete_artist(self, artist_id: UUID):
        if not artist_service.delete(artist_id):
            raise HTTPException(status_code=404, detail="Artist not found")
        return {"message": "Artist deleted successfully"}