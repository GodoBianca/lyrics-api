from pydantic import BaseModel
from uuid import UUID

class ArtistModel(BaseModel):
    id: UUID = None
    name: str
