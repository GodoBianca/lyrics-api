# Define o modelo de dados.
from pydantic import BaseModel
from uuid import UUID

class MusicModel(BaseModel):
    id: UUID = None
    artist_id: UUID
    title: str
    content: str