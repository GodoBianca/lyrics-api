from uuid import uuid4, UUID
from typing import Optional
from src.model.music_model import MusicModel
import psycopg2


class MusicRepository:

    def __init__(self):
        self.connection = psycopg2.connect(
            dbname="",
            user="",
            password="",
            host="",
            port=""
        )

    def find(self, id: UUID) -> Optional[MusicModel]:
        try:
            print(f"Searching for music with ID: {id}")
            cursor = self.connection.cursor()
            cursor.execute(
                "SELECT id, artist_id, title, content FROM musics WHERE id = %s", (str(id),))
            result = cursor.fetchone()
            cursor.close()
            print(f"Database result: {result}")
            if result:
                return MusicModel(id=result[0], artist_id=result[1], title=result[2], content=result[3])
            return None
        except Exception as e:
            print(f"Error fetching music: {e}")
            return None

    def save(self, music: MusicModel) -> MusicModel:
        cursor = self.connection.cursor()
        try:
            if music.id is None:
                music.id = uuid4()
                cursor.execute(
                    "INSERT INTO musics (id, artist_id, title, content) VALUES (%s, %s, %s, %s)",
                    (str(music.id), str(music.artist_id), music.title,
                    music.content)  # Adiciona o artist_id
                )
                print(f"Music criado com ID: {music.id}")
            else:
                cursor.execute(
                    "UPDATE musics SET artist_id = %s, title = %s, content = %s WHERE id = %s",
                    (str(music.artist_id), music.title, music.content,
                    str(music.id))  # Inclui artist_id no update também
                )
                print(f"Music atualizado com ID: {music.id}")
        except Exception as e:
            self.connection.rollback()
            print(f"Erro ao salvar música: {e}")
        finally:
            self.connection.commit()
            cursor.close()
        return music

    def delete(self, id: UUID) -> None:
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM musics WHERE id = %s", (str(id),))
        self.connection.commit()
        cursor.close()
