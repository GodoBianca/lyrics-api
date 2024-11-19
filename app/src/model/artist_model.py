from pydantic import BaseModel
from uuid import UUID

class ArtistModel(BaseModel):
    artist_id: UUID = None
    name: str
