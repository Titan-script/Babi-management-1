from fastapi import APIRouter
from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
