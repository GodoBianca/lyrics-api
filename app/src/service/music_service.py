# Este arquivo contém a lógica dos métodos find, insert, update e delete mockado

from uuid import uuid4, UUID
from typing import Dict, Optional

class MusicService:
    def __init__(self):
        self.music_db: Dict[UUID, dict] = {}

    def find(self, music_id: UUID) -> Optional[dict]:
        return self.music_db.get(music_id)

    def insert(self, music: dict) -> dict:
        music_id = uuid4()  # Gera um novo UUID
        music['id'] = music_id
        self.music_db[music_id] = music
        return music

    def update(self, music_id: UUID, updated_music: dict) -> Optional[dict]:
        if music_id in self.music_db:
            self.music_db[music_id].update(updated_music)
            return self.music_db[music_id]
        return None

    def delete(self, music_id: UUID) -> bool:
        if music_id in self.music_db:
            del self.music_db[music_id]
            return True
        return False