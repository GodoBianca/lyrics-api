from uuid import uuid4, UUID
from typing import Optional
from src.model.artist_model import ArtistModel
from src.repository.artist_repository import ArtistRepository

class ArtistService:
    
    def __init__(self):
        self.repository = ArtistRepository()

    def find(self, artist_id: UUID) -> Optional[ArtistModel]:
        return self.repository.find(artist_id)

    def insert(self, name: str) -> ArtistModel:
        return self.repository.save(name)

    def update(self, artist_id: UUID, update_artist: ArtistModel) -> Optional[ArtistModel]:
        if not self.find(artist_id):
            return None
        update_artist.artist_id = artist_id
        return self.repository.save(update_artist)

    def delete(self, artist_id: UUID) -> bool:
        if not self.find(artist_id):
            return False
        self.repository.delete(artist_id)
        return True