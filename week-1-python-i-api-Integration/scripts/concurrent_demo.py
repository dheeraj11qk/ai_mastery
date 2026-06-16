import asyncio
import time

import httpx


URL = "http://localhost:8000/chat"


async def send_message(session_id: str, message: str) -> None:
    async with httpx.AsyncClient(timeout=120) as client:
        start = time.perf_counter()
        response = await client.post(URL, json={"session_id": session_id, "message": message})
        elapsed = time.perf_counter() - start
        print(f"{session_id}: {response.status_code} in {elapsed:.2f}s")
        print(response.json())


async def main() -> None:
    await asyncio.gather(
        send_message("demo-a", "Explain asyncio in one sentence."),
        send_message("demo-b", "Explain FastAPI in one sentence."),
        send_message("demo-a", "What did I ask before?"),
    )


if __name__ == "__main__":
    asyncio.run(main())
