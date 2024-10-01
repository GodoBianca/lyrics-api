# Este arquivo contém a lógica dos métodos find, insert, update e delete mockado
from uuid import uuid4, UUID
from typing import Optional
from src.model.music_model import MusicModel
from src.repository.music_repository import MusicRepository

class MusicService:
    
    #Mudei aqui para ele injetar agora no repository
    def __init__(self):
        self.repository = MusicRepository()

    def find(self, id: UUID) -> Optional[MusicModel]:
        return self.repository.find(id)

    def insert(self, music: MusicModel) -> MusicModel:
        return self.repository.save(music)
    
    def update(self, id: UUID, updated_music: MusicModel) -> Optional[MusicModel]:
        if not self.find(id):
            return None
        updated_music.id = id
        return self.repository.save(updated_music)

    def delete(self, id: UUID) -> bool:
        if not self.find(id):
            return False
        self.repository.delete(id)
        return True