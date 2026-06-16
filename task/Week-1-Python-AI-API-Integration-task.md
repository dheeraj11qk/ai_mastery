# Week-1-Python-AI-API-Integration-task

## Goal

Build an asynchronous AI chat API that accepts a `session_id` and `message`, calls an AI model provider asynchronously, stores conversation history per session, and runs locally in Docker.

## Outcome

By Sunday, you should be able to send multiple concurrent requests to the API and show:

- Requests do not block each other.
- Each `session_id` keeps its own conversation history.
- The app can run locally through Docker.
- The `/chat` endpoint returns AI responses reliably.

## Project

**Asynchronous AI Chat API**

Suggested stack:

- Python
- FastAPI
- Uvicorn
- OpenAI, Gemini, Claude, DeepSeek async SDK, or Ollama local models
- `python-dotenv` or Pydantic settings
- Docker
- Postman, curl, or HTTPie for testing

## Daily Tasks

### Monday - Learn

- [ ] Study how Python `asyncio` works.
- [ ] Understand `async` / `await` syntax.
- [ ] Learn why non-blocking network calls matter for AI APIs.
- [ ] Write a tiny async script that runs multiple fake API calls concurrently with `asyncio.gather`.

Deliverable:

- [ ] A short note explaining event loop, coroutine, awaitable, and task.

### Tuesday - Learn

- [ ] Study async REST endpoints in FastAPI.
- [ ] Learn how Uvicorn handles async requests.
- [ ] Learn how to load secrets from a `.env` file.
- [ ] Decide which model provider SDK you will use first.

Deliverable:

- [ ] A minimal FastAPI app with a health endpoint.
- [ ] A `.env.example` file listing required config keys.

### Wednesday - Build

- [ ] Initialize the Week 1 project folder.
- [ ] Create a virtual environment or dependency file.
- [ ] Install FastAPI, Uvicorn, provider SDK, and config dependencies.
- [ ] Create an async `POST /chat` route.
- [ ] Accept this request shape:

```json
{
  "session_id": "user-123",
  "message": "Hello"
}
```

Deliverable:

- [ ] `/chat` route accepts valid JSON and returns a placeholder response.

### Thursday - Build

- [ ] Add async client integration for OpenAI, Gemini, Claude, DeepSeek, or Ollama local models.
- [ ] Move provider configuration into environment variables.
- [ ] Add basic error handling for missing API keys and provider failures.
- [ ] Keep model-calling code separate from route code.

Deliverable:

- [ ] `/chat` returns a real model response from the selected provider.

### Friday - Build

- [ ] Add in-memory session history using a dictionary keyed by `session_id`.
- [ ] Append each user message and assistant response to the session history.
- [ ] Send previous session turns back to the model so context is retained.
- [ ] Add a simple max-history limit to avoid unbounded memory growth.

Deliverable:

- [ ] Two different `session_id` values keep separate conversations.

### Saturday - Build

- [ ] Create a `Dockerfile`.
- [ ] Add a `.dockerignore`.
- [ ] Run the FastAPI app inside Docker.
- [ ] Verify environment variables are passed correctly.
- [ ] Test the Dockerized `/chat` endpoint from your host machine.

Deliverable:

- [ ] The app runs in Docker and responds to `/chat` requests.

### Sunday - Showcase

- [ ] Send multiple concurrent requests using Postman, curl, HTTPie, or a small script.
- [ ] Show that one slow request does not block other requests.
- [ ] Show that session history is retained per `session_id`.
- [ ] Capture logs or screenshots proving the behavior.
- [ ] Write a short project summary: what works, what failed, what to improve next.

Deliverable:

- [ ] A working demo of the asynchronous AI chat API.

## Acceptance Checklist

- [ ] `POST /chat` accepts `session_id` and `message`.
- [ ] Endpoint is async.
- [ ] AI provider call is async.
- [ ] Session history is stored separately per `session_id`.
- [ ] Basic provider errors are handled.
- [ ] App can run locally.
- [ ] App can run in Docker.
- [ ] Concurrent requests have been tested.
- [ ] Sunday showcase notes are written.

## Stretch Goals

- [ ] Add request/response logging with timestamps.
- [ ] Add `/sessions/{session_id}` to inspect stored history.
- [ ] Add `/sessions/{session_id}` DELETE to clear a session.
- [ ] Add simple tests for session history behavior.
- [ ] Add a concurrency test script using `httpx.AsyncClient`.
- [ ] Replace in-memory storage with Redis.

## Suggested File Structure

```text
week-1-ai-chat-api/
  app/
    main.py
    config.py
    models.py
    ai_client.py
    session_store.py
  tests/
    test_sessions.py
  .env.example
  .dockerignore
  Dockerfile
  requirements.txt
  README.md
```

## Notes

- Keep the first version simple. In-memory storage is acceptable for Week 1.
- Do not commit real API keys.
- Prefer small working increments over a large rewrite.
- The main skill this week is understanding async behavior, not building a perfect chatbot.
