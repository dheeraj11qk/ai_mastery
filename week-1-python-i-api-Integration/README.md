# Week-1-Python-AI-API-Integration

Asynchronous FastAPI chat API for Week 1 of the AI Mastery Roadmap.

## Features

- Async `POST /chat` endpoint.
- Per-session in-memory conversation history.
- Provider abstraction with `echo`, `ollama`, and `openai_compatible` modes.
- Docker support.
- Session inspect and clear endpoints.
- Small concurrent request demo script.

## Run Locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

Health check:

```bash
curl http://localhost:8000/health
```

Chat request:

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"session_id":"user-123","message":"Hello"}'
```

## Use Ollama

Start Ollama and pull a model:

```bash
ollama pull gemma2:2b
ollama serve
```

Set `.env`:

```env
AI_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=gemma2:2b
```

## Use OpenAI-Compatible Providers

This mode works for OpenAI-compatible chat completion APIs, including OpenAI and providers that expose `/chat/completions`.

```env
AI_PROVIDER=openai_compatible
OPENAI_COMPATIBLE_BASE_URL=https://api.openai.com/v1
OPENAI_COMPATIBLE_API_KEY=your-api-key
OPENAI_COMPATIBLE_MODEL=gpt-4o-mini
```

For DeepSeek, use its OpenAI-compatible base URL and model name.

## Run With Docker

```bash
docker build -t week-1-ai-chat-api .
docker run --env-file .env -p 8000:8000 week-1-ai-chat-api
```

If Docker needs to call Ollama running on your host machine, set `OLLAMA_BASE_URL` to your host-accessible address.

## Concurrent Request Demo

Start the API first, then run:

```bash
python scripts/concurrent_demo.py
```

## Test

```bash
pytest
```
