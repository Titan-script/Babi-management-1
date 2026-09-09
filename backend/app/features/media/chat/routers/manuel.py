
from .services.gemini_service import GeminiChatService


@router.post("/chat")
def chat_with_gemini(payload: ChatRequest, user_id: int, db: Session = Depends(get_db)):
    # 1. Enregistrer le message de l'utilisateur en DB
    user_msg = ChatMessage(user_id=user_id, sender="user", message=payload.message)
    db.add(user_msg)
    db.commit()

    # 2. Appeler l'IA (Gemini)
    ai_service = GeminiChatService()
    reply_text = ai_service.generate_response(payload.message)

    # 3. Enregistrer la réponse de l'IA en DB
    ai_msg = ChatMessage(user_id=user_id, sender="ai", message=reply_text)
    db.add(ai_msg)
    db.commit()

    # 4. Renvoyer au front
    return {"reply": reply_text}

