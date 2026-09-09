from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from ..handlers.notifications import notify_ws_manager

router = APIRouter(tags=["WebSockets-notifications"])


@router.websocket("/ws/notifications/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    await notify_ws_manager.connect(websocket, user_id)
    try:
        while True:
            # Garde la connexion active et écoute les pings du client
            data = await websocket.receive_text()
            if data == "ping":
                await websocket.send_text("pong")
    except WebSocketDisconnect:
        notify_ws_manager.disconnect(user_id)


notifications_ws_router = [
    router,
]
