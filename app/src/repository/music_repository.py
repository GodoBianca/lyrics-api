from uuid import uuid4, UUID
from typing import Optional
from src.model.music_model import MusicModel
import psycopg2


class MusicRepository:

    def __init__(self):
        self.connection = psycopg2.connect(
            dbname="MusicCatalog",
            user="postgres",
            password="351641",
            host="localhost",
            port="5432"
        )

    def find(self, id: UUID) -> Optional[MusicModel]:
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT id, artist_id, title, content FROM musics WHERE id = %s", (str(id),))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return MusicModel(id=result[0], artist_id=result[1], title=result[2], content=result[3])
        return None

    def save(self, music: MusicModel) -> MusicModel:
        cursor = self.connection.cursor()
        try:
            if music.id is None:
                music.id = uuid4()
                cursor.execute(
                    "INSERT INTO musics (id, artist_id, title, content) VALUES (%s, %s, %s, %s)",
                    (str(music.id), str(music.artist_id), music.title, music.content)
                )
                print(f"Music criado com ID: {music.id}")
            else:
                cursor.execute(
                    "UPDATE musics SET artist_id = %s,title= %s, content = %s WHERE id = %s",
                    ( str(music.artist_id), music.title, music.content, str(music.id))
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
