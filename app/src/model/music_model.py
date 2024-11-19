from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class MusicModel(BaseModel):
    id: UUID = None
    artist_id: Optional[UUID]
    title: str
    content: str
