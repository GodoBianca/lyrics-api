# Define o modelo de dados.
from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class MusicModel(BaseModel):
    id: UUID = None
    artist_id: Optional[UUID]  # Permite valores None
    title: str
    content: str