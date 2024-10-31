from uuid import uuid4, UUID
from typing import Optional
from src.model.artist_model import ArtistModel
import psycopg2


class ArtistRepository:

    def __init__(self):
        self.connection = psycopg2.connect(
            dbname="",
            user="",
            password="",
            host="",
            port=""
        )

    def find(self, artist_id: UUID) -> Optional[ArtistModel]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT artist_id, name FROM artists WHERE artist_id = %s", (str(artist_id),))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return ArtistModel(artist_id=result[0], name=result[1])
        return None

    def save(self, artists: ArtistModel) -> ArtistModel:
        cursor = self.connection.cursor()
        try:
            if artists.artist_id is None:
                artists.artist_id = uuid4()
                cursor.execute("INSERT INTO artists (artist_id, name) VALUES (%s, %s)",
                            (str(artists.artist_id), str(artists.name)))
                print(f"Artist criado com ID: {artists.artist_id}")          
            else:
                cursor.execute("UPDATE artists SET name = %s WHERE artist_id = %s",
                               (str(artists.name), str(artists.artist_id)))
                print(f"Artist atualizado com ID: {artists.artist_id}")
        except Exception as e:
            self.connection.rollback()
            print(f"Erro ao salvar artista: {e}")
        finally:
            self.connection.commit()
            cursor.close()
        return artists 

    def delete(self, artist_id: UUID) -> None:
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM artists WHERE artist_id = %s", (str(artist_id),))
        self.connection.commit()
        cursor.close()