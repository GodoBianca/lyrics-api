from uuid import uuid4, UUID
from typing import Optional
from src.model.artist_model import ArtistModel
from src.repository.database_connection import DatabaseConnection

class ArtistRepository:
    def find(self, id: UUID) -> Optional[ArtistModel]:
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id, name FROM artists WHERE id = %s", (str(id),))
        result = cursor.fetchone()
        cursor.close()
        DatabaseConnection.return_connection(connection)
        if result:
            return ArtistModel(id=result[0], name=result[1])
        return None

    def artist_exists(self, id: UUID) -> bool:
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT EXISTS(SELECT 1 FROM artists WHERE id = %s)", (str(id),))
        exists = cursor.fetchone()[0]
        cursor.close()
        return exists

    def save(self, artist: ArtistModel) -> ArtistModel:
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        try:
            if artist.id is None:
                artist.id = uuid4()
                cursor.execute("INSERT INTO artists (id, name) VALUES (%s, %s)", (str(
                    artist.id), artist.name))
            else:
                cursor.execute("UPDATE artists SET name = %s WHERE id = %s",
                               (artist.name, str(artist.id)))
        except Exception as e:
            connection.rollback()
            print(f"Error saving artist: {e}")
        finally:
            connection.commit()
            cursor.close()
            DatabaseConnection.return_connection(connection)
        return artist

    def delete(self, id: UUID) -> bool:
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM artists WHERE id = %s", (str(id),))
        deleted = cursor.rowcount > 0
        connection.commit()
        cursor.close()
        DatabaseConnection.return_connection(connection)
        return deleted
