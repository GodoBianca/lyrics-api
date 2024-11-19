from uuid import uuid4, UUID
from typing import Optional
from src.model.music_model import MusicModel
from src.repository.database_connection import DatabaseConnection

class MusicRepository:
    def find(self, id: UUID) -> Optional[MusicModel]:
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id, artist_id, title, content FROM musics WHERE id = %s", (str(id),))
        result = cursor.fetchone()
        cursor.close()
        DatabaseConnection.return_connection(connection)
        if result:
            return MusicModel(id=result[0], artist_id=result[1], title=result[2], content=result[3])
        return None

    def save(self, music: MusicModel) -> MusicModel:
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        try:
            if music.id is None:
                music.id = uuid4()
                cursor.execute("INSERT INTO musics (id, title, content, artist_id) VALUES (%s, %s, %s, %s)", 
                               (str(music.id), music.title, music.content, str(music.artist_id)))
            else:
                cursor.execute("UPDATE musics SET title = %s, content = %s, artist_id = %s WHERE id = %s",
                               (music.title, music.content, str(music.artist_id), str(music.id)))
        except Exception as e:
            connection.rollback()
            print(f"Error saving music: {e}")
        finally:
            connection.commit()
            cursor.close()
            DatabaseConnection.return_connection(connection)
        return music

    def delete(self, id: UUID) -> bool:
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM musics WHERE id = %s", (str(id),))
        deleted = cursor.rowcount > 0
        connection.commit()
        cursor.close()
        DatabaseConnection.return_connection(connection)
        return deleted
