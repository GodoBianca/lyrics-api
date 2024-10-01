# Este arquivo contém a lógica dos métodos find, insert, update e delete mockado
from uuid import uuid4, UUID
from typing import Optional
from src.model.music_model import MusicModel

class MusicService:
    
    def __init__(self):
        self.music_db: dict[UUID, MusicModel] = {}  # Armazena MusicModel diretamente

    def find(self, id: UUID) -> Optional[MusicModel]:
        return self.music_db.get(id)

    def insert(self, music: MusicModel) -> MusicModel:
        music_id = uuid4()
        music.id = music_id
        self.music_db[music_id] = music
        return music
    
    def update(self, id: UUID, updated_music: MusicModel) -> Optional[MusicModel]:
        if id not in self.music_db:
            return None
        self.music_db[id].title = updated_music.title
        self.music_db[id].content = updated_music.content
        return self.music_db[id]

    def delete(self, id: UUID) -> bool:
        if id not in self.music_db:
            return False
        del self.music_db[id]
        return True