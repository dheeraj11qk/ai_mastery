from fastapi import Depends, FastAPI
from app.ai_client import AIClient
from app.config import Settings, get_settings
from app.models import ChatRequest, ChatResponse, Message
from app.session_store import InMemorySessionStore


settings = get_settings()
session_store = InMemorySessionStore(max_messages=settings.max_history_messages)

app = FastAPI(title=settings.app_name)


def get_ai_client(current_settings: Settings = Depends(get_settings)) -> AIClient:
    return AIClient(current_settings)


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, ai_client: AIClient = Depends(get_ai_client)) -> ChatResponse:
    history = session_store.get_history(request.session_id)
    messages = history + [Message(role="user", content=request.message)]

    ai_response = await ai_client.generate(messages)
    updated_history = session_store.append_turn(
        session_id=request.session_id,
        user_message=request.message,
        assistant_message=ai_response,
    )

    return ChatResponse(
        session_id=request.session_id,
        provider=settings.provider,
        response=ai_response,
        history_length=len(updated_history),
    )


@app.get("/sessions/{session_id}")
async def get_session(session_id: str) -> dict[str, object]:
    return {
        "session_id": session_id,
        "messages": [message.model_dump() for message in session_store.snapshot(session_id)],
    }


@app.delete("/sessions/{session_id}")
async def clear_session(session_id: str) -> dict[str, object]:
    cleared = session_store.clear(session_id)
    return {"session_id": session_id, "cleared": cleared}
