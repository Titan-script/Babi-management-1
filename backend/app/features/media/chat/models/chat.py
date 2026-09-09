from app.common import Field

from app.toolbox import BaseTenant


class ChatMessage(BaseTenant, table=True):
    __tablename__ = "chat_message"

    user_id: int = Field(foreign_key="user.id", index=True)  # Pour lier à l'utilisateur connecté

    sender: str = Field(description="Soit 'user', soit 'ai'")
    message: str = Field(description="Le contenu du texte")
    category: str = Field(description="categorie")

