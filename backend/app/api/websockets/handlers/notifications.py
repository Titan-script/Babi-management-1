from typing import Dict, List

from fastapi import WebSocket


class NotifyWebSocketManager:
    def __init__(self):
        # Connexions directes par utilisateur (pour tes notifications et alertes)
        self.active_connections: Dict[int, WebSocket] = {}

        # Canaux de diffusion par bus (ex: bus_id -> liste de WebSockets connectés pour le suivre)
        self.bus_channels: Dict[int, List[WebSocket]] = {}

    async def connect_user(self, websocket: WebSocket, user_id: int):
        """Connecte un utilisateur pour les notifications personnelles."""
        await websocket.accept()
        self.active_connections[user_id] = websocket

    def disconnect_user(self, user_id: int):
        self.active_connections.pop(user_id, None)

    async def send_personal_message(self, message: str, user_id: int):
        if user_id in self.active_connections:
            try:
                await self.active_connections[user_id].send_json({"message": message})
            except Exception:
                self.disconnect_user(user_id)


notify_ws_manager = NotifyWebSocketManager()
