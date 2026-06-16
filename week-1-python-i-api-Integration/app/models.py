from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    session_id: str = Field(min_length=1, examples=["user-123"])
    message: str = Field(min_length=1, examples=["Hello"])


class ChatResponse(BaseModel):
    session_id: str
    provider: str
    response: str
    history_length: int


class Message(BaseModel):
    role: str
    content: str
