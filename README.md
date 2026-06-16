# AI Mastery

This repository contains a 3-month AI mastery roadmap and hands-on weekly projects.

## Structure

```text
docx/
  AI_Mastery_Roadmap.docx
  AI_Mastery_Roadmap.md
  Ai_Topics.md

task/
  Week-1-Python-AI-API-Integration-task.md

week-1-python-i-api-Integration/
  FastAPI async AI chat API project
```

## Roadmap

The main roadmap is available in:

- `docx/AI_Mastery_Roadmap.docx`
- `docx/AI_Mastery_Roadmap.md`

It covers 12 weeks of AI engineering, automation, RAG, agents, voice AI, fine-tuning, guardrails, and scalable AI architecture.

## Week 1 Project

Week 1 builds an asynchronous AI chat API using FastAPI.

Project folder:

```bash
cd week-1-python-i-api-Integration
```

Install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run with Ollama:

```bash
ollama pull gemma2:2b
ollama serve
```

In another terminal:

```bash
uvicorn app.main:app --reload
```

Test the API:

```bash
curl http://localhost:8000/health
```

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"session_id":"user-123","message":"Explain async Python simply"}'
```

For detailed Week 1 usage, see:

```text
week-1-python-i-api-Integration/README.md
```

## Notes

- Do not commit real API keys.
- Local `.env` files and virtual environments are ignored by Git.
- Week tasks live in the `task/` folder.
