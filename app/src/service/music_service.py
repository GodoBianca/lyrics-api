from src.model.music_model import MusicModel
from src.repository.music_repository import MusicRepository
from src.service.artist_service import ArtistService
from uuid import UUID
from typing import Optional

class MusicService:
    def __init__(self):
        self.repository = MusicRepository()
        self.artist_service = ArtistService()

    def validate_artist_id(self, artist_id: UUID) -> bool:
        # Verifica se o artist_id existe no banco
        return bool(self.artist_service.find(artist_id))

    def insert(self, music: MusicModel) -> MusicModel:
        # Valida o artist_id antes de inserir
        if not self.validate_artist_id(music.artist_id):
            raise ValueError("Artist ID não encontrado.")
        return self.repository.save(music)
    
    def find(self, id: UUID):
        return self.repository.find(id)

    def update(self, music: MusicModel) -> Optional[MusicModel]:
        # Valida o artist_id antes de atualizar
        if not self.validate_artist_id(music.artist_id):
            raise ValueError("Artist ID não encontrado.")
        return self.repository.save(music)
    
    def delete(self, id: UUID) -> bool:
        if not self.repository.find(id):
            return False  # Música não encontrada, retorna False
        return self.repository.delete(id)  # Retorna True se deletado com sucesso