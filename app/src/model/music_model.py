# Define o modelo de dados.

from uuid import UUID

class Music:
    def __init__(self, id: UUID, title: str, content: str):
        self.id = id
        self.title = title
        self.content = content
