# Define o modelo de dados.
from pydantic import BaseModel
from uuid import UUID

class MusicModel(BaseModel):
    id: UUID = None
    title: str
    content: str