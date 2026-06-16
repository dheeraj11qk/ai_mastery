import httpx
from fastapi import HTTPException

from app.config import Settings
from app.models import Message


class AIClient:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    async def generate(self, messages: list[Message]) -> str:
        provider = self.settings.provider

        if provider == "echo":
            return await self._echo(messages)
        if provider == "ollama":
            return await self._ollama(messages)
        if provider == "openai_compatible":
            return await self._openai_compatible(messages)

        raise HTTPException(status_code=500, detail=f"Unsupported AI provider: {provider}")

    async def _echo(self, messages: list[Message]) -> str:
        last_user_message = next(
            (message.content for message in reversed(messages) if message.role == "user"),
            "",
        )
        return f"Echo provider received: {last_user_message}"

    async def _ollama(self, messages: list[Message]) -> str:
        payload = {
            "model": self.settings.ollama_model,
            "messages": [message.model_dump() for message in messages],
            "stream": False,
        }

        try:
            async with httpx.AsyncClient(timeout=120) as client:
                response = await client.post(
                    f"{self.settings.ollama_base_url}/api/chat",
                    json=payload,
                )
                response.raise_for_status()
        except httpx.HTTPError as exc:
            raise HTTPException(status_code=502, detail=f"Ollama request failed: {exc}") from exc

        data = response.json()
        message = data.get("message", {})
        content = message.get("content")
        if not content:
            raise HTTPException(status_code=502, detail="Ollama returned an empty response")
        return content

    async def _openai_compatible(self, messages: list[Message]) -> str:
        if not self.settings.openai_compatible_api_key:
            raise HTTPException(
                status_code=500,
                detail="OPENAI_COMPATIBLE_API_KEY is required for openai_compatible provider",
            )

        payload = {
            "model": self.settings.openai_compatible_model,
            "messages": [message.model_dump() for message in messages],
        }
        headers = {"Authorization": f"Bearer {self.settings.openai_compatible_api_key}"}

        try:
            async with httpx.AsyncClient(timeout=120) as client:
                response = await client.post(
                    f"{self.settings.openai_compatible_base_url}/chat/completions",
                    headers=headers,
                    json=payload,
                )
                response.raise_for_status()
        except httpx.HTTPError as exc:
            raise HTTPException(status_code=502, detail=f"Model provider request failed: {exc}") from exc

        data = response.json()
        try:
            return data["choices"][0]["message"]["content"]
        except (KeyError, IndexError, TypeError) as exc:
            raise HTTPException(status_code=502, detail="Provider returned an unexpected response") from exc
