from uuid import uuid4, UUID
from typing import Optional
from src.model.artist_model import ArtistModel
from src.repository.database_connection import DatabaseConnection

class ArtistRepository:
    def find(self, artist_id: UUID) -> Optional[ArtistModel]:
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT artist_id, name FROM artists WHERE artist_id = %s", (str(artist_id),))
        result = cursor.fetchone()
        cursor.close()
        DatabaseConnection.return_connection(connection)
        if result:
            return ArtistModel(artist_id=result[0], name=result[1])
        return None

    def artist_exists(self, artist_id: UUID) -> bool:
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT EXISTS(SELECT 1 FROM artists WHERE id = %s)", (str(artist_id),))
        exists = cursor.fetchone()[0]
        cursor.close()
        return exists

    def save(self, artist: ArtistModel) -> ArtistModel:
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        try:
            if artist.artist_id is None:
                artist.artist_id = uuid4()
                cursor.execute("INSERT INTO artists (artist_id, name) VALUES (%s, %s)", (str(
                    artist.artist_id), artist.name))
            else:
                cursor.execute("UPDATE artists SET name = %s WHERE artist_id = %s",
                               (artist.name, str(artist.artist_id)))
        except Exception as e:
            connection.rollback()
            print(f"Error saving artist: {e}")
        finally:
            connection.commit()
            cursor.close()
            DatabaseConnection.return_connection(connection)
        return artist

    def delete(self, artist_id: UUID) -> bool:
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM artists WHERE artist_id = %s", (str(artist_id),))
        deleted = cursor.rowcount > 0
        connection.commit()
        cursor.close()
        DatabaseConnection.return_connection(connection)
        return deleted
