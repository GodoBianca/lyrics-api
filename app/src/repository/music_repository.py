from uuid import uuid4, UUID
from typing import Optional
from src.model.music_model import MusicModel

class MusicRepository:
    
    def __init__(self):
        self.music_db: dict[UUID, MusicModel] = {}
        
    def find(self, id: UUID) -> Optional[MusicModel]:
        return self.music_db.get(id)
    
    def save(self, music: MusicModel) -> MusicModel:
        if music.id is None: #ve se o id existe se nao ele cria um novo
            music_id = uuid4()
            music.id = music_id
            self.music_db[music_id] = music
            return music
        else: #se o id ja existir ele atualiza
            self.music_db[music.id].title = music.title
            self.music_db[music.id].content = music.content
            return self.music_db[music.id]

    def delete(self, id: UUID) -> None:
        if id in self.music_db:
            del self.music_db[id]