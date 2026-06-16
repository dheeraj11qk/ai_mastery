# 3-Month AI Mastery Roadmap
## Combined Path: AI Engineer + AI Automation Engineer + AI System Architect

This roadmap is structured as a **12-week schedule (3 months)**. It is optimized for software engineers who already understand standard backend development (APIs, databases, Docker, Git) and want to learn AI architectures, automation, and infrastructure.

**Learning Strategy:** Use AI tools (like ChatGPT, Claude, or Gemini) to explain the concepts step-by-step, read the background theory, and immediately build the weekly project tasks.

---

## Roadmap Overview

| Week | Focus Area | Project Showcase Checklist |
| :--- | :--- | :--- |
| **Week 1** | Python & AI API Integration | [ ] **Asynchronous AI Chat API** (Sunday Showcase) |
| **Week 2** | AI Fundamentals & Streaming | [ ] **Streaming Text Summarizer CLI/Web** (Sunday Showcase) |
| **Week 3** | LLM Engineering & Structured Outputs | [ ] **AI Travel Planner** (Sunday Showcase) |
| **Week 4** | RAG (Retrieval-Augmented Gen) Basics | [ ] **Local PDF Q&A Bot** (Sunday Showcase) |
| **Week 5** | Advanced RAG & Search Routing | [ ] **Enterprise Search Engine** (Sunday Showcase) |
| **Week 6** | Agentic Systems & MCP | [ ] **Autonomous Web Research Agent** (Sunday Showcase) |
| **Week 7** | Multi-Agent Systems & Collaboration | [ ] **Collaborative AI Software Dev Team** (Sunday Showcase) |
| **Week 8** | AI Automation & Workflows | [ ] **Event-Driven Lead Enrichment Pipeline** (Sunday Showcase) |
| **Week 9** | Voice AI & Realtime APIs | [ ] **Interactive Voice Concierge** (Sunday Showcase) |
| **Week 10** | Fine-Tuning & Dataset Engineering | [ ] **FAQ Dataset Generator & PEFT Fine-Tune** (Sunday Showcase) |
| **Week 11** | MLOps, Guardrails & Security | [ ] **Secure AI Gateway Proxy** (Sunday Showcase) |
| **Week 12** | AI System Architecture & Scaling | [ ] **High-Throughput Distributed Agent Platform** (Sunday Showcase) |

---

## Day-by-Day Weekly Breakdown

### Week 1 — Python & AI API Integration
Set up the core development patterns needed to communicate with AI model providers asynchronously.

*   **Daily Action Plan:**
    *   **Monday (Learn):** Research how Python's `asyncio` and `async/await` syntax manage non-blocking network calls under the hood.
    *   **Tuesday (Learn):** Study how async REST endpoints work in FastAPI and how to load config variables from a `.env` file securely.
    *   **Wednesday (Build):** Initialize the project structure, install the needed SDKs, and create an async FastAPI POST route `/chat` accepting a `session_id` and `message`.
    *   **Thursday (Build):** Integrate the OpenAI, Gemini, Claude, or **DeepSeek** Python SDK using their async client framework.
    *   **Friday (Build):** Implement simple in-memory session history storage (using a dictionary keyed by `session_id`) to track and append previous conversation turns.
    *   **Saturday (Build):** Containerize the API with a `Dockerfile`, run the app locally inside Docker, and verify standard connection routing.
    *   **Sunday (Showcase):** Send multiple concurrent requests using Postman or Curl. Verify that async tasks do not block each other, and show that context/history is accurately retained per session.

---

### Week 2 — AI Basics & Streaming Endpoints
Understand how model weights translate to words, how token limits govern conversation context, and how to build responsive user interfaces using streaming.

*   **Daily Action Plan:**
    *   **Monday (Learn):** Research the difference between AI, Machine Learning, and Deep Learning, plus how neural networks make predictions (weights, biases, training vs inference).
    *   **Tuesday (Learn):** Learn what tokens are, how context windows restrict model memory, how temperature/top-p affects output creativity, and how Server-Sent Events (SSE) work over HTTP.
    *   **Wednesday (Build):** Set up a FastAPI endpoint `/stream-summary` configured to return a `StreamingResponse` (SSE stream).
    *   **Thursday (Build):** Connect the endpoint to your LLM streaming client, yielding text chunks as they arrive from the API provider.
    *   **Friday (Build):** Integrate a library (like `tiktoken`) to calculate exact input/output tokens and estimate API call costs in real-time.
    *   **Saturday (Build):** Add a simple command-line interface (CLI) or frontend page to render the streaming response and display metrics (TTFT, tokens/sec, cost).
    *   **Sunday (Showcase):** Feed a large article through the app. Record a demo showing the streaming output starting instantly, and showcase the final speed and token cost analysis.

---

### Week 3 — LLM Engineering & Structured Output
Learn how to get structured, reliable, machine-readable data from creative models to feed downstream databases and systems.

*   **Daily Action Plan:**
    *   **Monday (Learn):** Learn the fundamentals of the Transformer architecture (Attention mechanism) and the differences between LLMs, SLMs, VLMs, and **Multimodal AI** (processing images, text, and audio).
    *   **Tuesday (Learn):** Study prompt engineering patterns, specifically System Prompts, Few-shot prompting, and Chain-of-Thought (CoT). Understand how LLM Tool Calling mechanics operate.
    *   **Wednesday (Build):** Define Pydantic schemas enforcing a strict JSON structure for travel itineraries (destination, budget, daily activities, weather limits).
    *   **Thursday (Build):** Register a mock tool `get_current_weather(location: str)` and configure the LLM to access it via function calling definition metadata.
    *   **Friday (Build):** Write the main agent loop: query model -> handle weather tool call -> feed result back -> parse structured JSON response.
    *   **Saturday (Build):** Implement validation code to check if the generated JSON output accurately fits the Pydantic schema, and write a simple error recovery catch.
    *   **Sunday (Showcase):** Run queries for different destinations. Showcase the raw tool-call invocation logs and display the beautifully structured JSON output that contains weather-specific travel recommendations.

---

### Week 4 — Retrieval-Augmented Generation (RAG) Basics
Extend the model's knowledge base using external documents without expensive training or fine-tuning.

*   **Daily Action Plan:**
    *   **Monday (Learn):** Research what RAG is and why grounding queries in external documents avoids hallucination.
    *   **Tuesday (Learn):** Study how text chunking strategies work (chunk size, overlap, semantic splits) and what vector embeddings represent. Learn how to serve open source models locally using **Ollama**.
    *   **Wednesday (Build):** Write a PDF parsing script and chunk the documents into ~500-token chunks with 50-token overlap.
    *   **Thursday (Build):** Generate vector embeddings using an API-based embedding model or a local model hosted on Ollama, and load them into a local vector DB like ChromaDB or FAISS.
    *   **Friday (Build):** Write the retrieve-and-generate logic: embed user query, search DB for top-3 chunks, inject them into the system prompt context.
    *   **Saturday (Build):** Refine prompt instructions to enforce that answers must cite the document page or section and say "I don't know" if the context lacks information.
    *   **Sunday (Showcase):** Upload a complex PDF (e.g., a software manual or financial report) and ask questions. Show how the bot successfully retrieves and cites sources for its answers.

---

### Week 5 — Advanced RAG & Search Routing
Optimize retrieval accuracy for enterprise databases where keywords, metadata, and document hierarchies overlap.

*   **Daily Action Plan:**
    *   **Monday (Learn):** Learn the limits of semantic-only search and why Hybrid Search (dense vector + lexical search) is standard.
    *   **Tuesday (Learn):** Study Rerankers (Cross-encoders) and how they compute similarity scores, plus metadata filtering logic.
    *   **Wednesday (Build):** Spin up a cloud vector DB instance (Qdrant or Pinecone) and ingest documents with tags/metadata.
    *   **Thursday (Build):** Implement a Python search query combining vector search and BM25 keywords.
    *   **Friday (Build):** Integrate a reranking API (Cohere Rerank or local cross-encoder) to re-evaluate the top 15 results down to the best 4.
    *   **Saturday (Build):** Apply metadata filters so queries can target specific categories or upload times.
    *   **Sunday (Showcase):** Run queries comparing semantic-only search results against hybrid search and reranked outputs to show accuracy gains.

---

### Week 6 — Single-Agent Systems & MCP
Transition from static pipelines to dynamic agentic loops that can plan, self-correct, and use tools recursively.

*   **Daily Action Plan:**
    *   **Monday (Learn):** Understand **Agentic AI** design patterns, ReAct loops, and the theoretical paths toward achieving **AGI** (Artificial General Intelligence).
    *   **Tuesday (Learn):** Study agent state tracking, memory strategies, and the Model Context Protocol (MCP) for tool sharing.
    *   **Wednesday (Build):** Setup the core agent loop using raw code or LangChain/LangGraph.
    *   **Thursday (Build):** Bind tools for Google Search (Tavily/SerpAPI) and document reading.
    *   **Friday (Build):** Write a self-reflection node: before formatting the final response, the agent must check if it fully answered the query.
    *   **Saturday (Build):** Handle API limits, execution timeouts, and print detailed execution trace logs.
    *   **Sunday (Showcase):** Pose a highly complex research question that requires multi-step internet searches and verify the logical reasoning path.

---

### Week 7 — Multi-Agent Systems & Collaboration
Coordinate multiple specialized AI agents with distinct roles to solve complex tasks that are too massive for a single agent.

*   **Daily Action Plan:**
    *   **Monday (Learn):** Learn multi-agent routing patterns (hierarchical vs peer-to-peer collaboration).
    *   **Tuesday (Learn):** Study shared graph state, routing conditions, and state serialization.
    *   **Wednesday (Build):** Define the orchestration graph using LangGraph, CrewAI, or AutoGen.
    *   **Thursday (Build):** Build three agents: PM (spec writer), Architect (system designer), and Developer (coder).
    *   **Friday (Build):** Build a QA Tester agent that runs static code checks or unit tests on the developer's output.
    *   **Saturday (Build):** Wire up the loop back to the developer if the QA agent finds syntax/logical bugs.
    *   **Sunday (Showcase):** Input a description of a command-line tool, let the agents collaborate, and demonstrate the executed output.

---

### Week 8 — AI Automation & Workflows
Connect AI models to external SaaS tools and business events using automation platforms.

*   **Daily Action Plan:**
    *   **Monday (Learn):** Learn how automation platforms connect web triggers, JSON parsers, and API gateways. Understand how workflows drive **Hyperautomation** and construct a **Digital Workforce**.
    *   **Tuesday (Learn):** Study webhook schemas, payloads, and asynchronous web-scrapers.
    *   **Wednesday (Build):** Install and run n8n on Docker.
    *   **Thursday (Build):** Build a webhook trigger and hook it up to a webpage content scraper.
    *   **Friday (Build):** Integrate an LLM node in n8n to analyze the scraped page, classify business data, and draft messages.
    *   **Saturday (Build):** Configure external API nodes (Airtable/Google Sheets and email integration) to write data.
    *   **Sunday (Showcase):** Submit a mock client form, watch n8n scrape/enrich the lead, record the database update and draft email.

---

### Week 9 — Voice AI & Realtime APIs
Build natural, low-latency conversational voice interfaces that process streaming audio inputs and outputs.

*   **Daily Action Plan:**
    *   **Monday (Learn):** Learn audio buffering, digital signal processing for voice, and audio streaming formats.
    *   **Tuesday (Learn):** Study WebSockets for bi-directional streaming and ElevenLabs or OpenAI Realtime audio APIs.
    *   **Wednesday (Build):** Set up a script using `sounddevice` to capture microphone inputs.
    *   **Thursday (Build):** Direct the audio stream to a Whisper model for transcription, sending results to an LLM.
    *   **Friday (Build):** Connect the LLM output to a TTS system (OpenAI TTS or ElevenLabs) to stream voice chunks.
    *   **Saturday (Build):** Handle audio latency, interrupts (user speaking over assistant), and background noise filters.
    *   **Sunday (Showcase):** Conduct a live spoken dialogue with the voice concierge, showing near-instant verbal feedback.

---

### Week 10 — Fine-Tuning & Dataset Engineering
Learn when and how to adapt open-weight models to follow specific stylistic rules, formats, or domain-specific language.

*   **Daily Action Plan:**
    *   **Monday (Learn):** Learn model creation phases: **Pretraining** vs Fine-Tuning, Instruction Tuning, and alignment methods (**RLHF** - Reinforcement Learning from Human Feedback and **DPO** - Direct Preference Optimization).
    *   **Tuesday (Learn):** Study data quality rules for model tuning. Learn model optimization and compression: **Quantization**, **Distillation**, and **Pruning**.
    *   **Wednesday (Build):** Write a prompt engineering pipeline that converts company documentation into 200 high-quality Q&A samples.
    *   **Thursday (Build):** Save the generated dataset in `.jsonl` format and validate structure.
    *   **Friday (Build):** Set up Hugging Face's `SFTTrainer` and PEFT to configure QLoRA for Mistral or Llama-3 (on Google Colab/GPU). Study hardware limits like **VRAM**, **CUDA** library configurations, and **Distributed Training** scaling.
    *   **Saturday (Build):** Trigger a short training job and track the training loss logs using Weights & Biases.
    *   **Sunday (Showcase):** Run side-by-side prompt tests comparing the raw base model against the fine-tuned checkpoint.

---

### Week 11 — MLOps, Guardrails & Security
Deploy LLM systems with safety, privacy, cost management, and guardrails to prevent exploitation.

*   **Daily Action Plan:**
    *   **Monday (Learn):** Learn vulnerabilities in LLMs: prompt injections, jailbreaks, data leakage, and training data poison.
    *   **Tuesday (Learn):** Study guardrail architecture (NeMo Guardrails, Llama Guard, Presidio) and how they fit in proxy systems.
    *   **Wednesday (Build):** Build a proxy FastAPI server positioned in front of your LLM calls.
    *   **Thursday (Build):** Create a prompt scanner using regex/classifier models to intercept injection scripts.
    *   **Friday (Build):** Integrate Presidio to scan incoming text and redact sensitive PII (emails, phone numbers).
    *   **Saturday (Build):** Write output checks and configure rate limiters and cost tracking logs.
    *   **Sunday (Showcase):** Attempt to jailbreak the endpoint, input sensitive data, and verify that the security filters block and redact data correctly.

---

### Week 12 — AI System Architecture & Scaling
Design distributed systems that handle high throughput, optimize API call costs, and handle background processing.

*   **Daily Action Plan:**
    *   **Monday (Learn):** Study **Enterprise AI** architectures, how to design **AI Native** and **AI First** systems driving **AI Transformation**, build custom **Vertical AI** domains, and secure data pipelines to establish an **AI Moat**.
    *   **Tuesday (Learn):** Study KV cache issues, and research high-performance **Model Serving** using dedicated **Inference Servers** (like **vLLM** or Triton). Learn about message queues (Kafka, RabbitMQ) and distributed caching (Redis).
    *   **Wednesday (Build):** Implement Redis and write a wrapper to check semantic cache similarity using embeddings.
    *   **Thursday (Build):** Configure RabbitMQ or Celery to handle long-running agent tasks in the background.
    *   **Friday (Build):** Implement rate limiting and cost limits per user key.
    *   **Saturday (Build):** Set up a Prometheus metric dashboard tracking API queues, queue latency, and cost per request.
    *   **Sunday (Showcase):** Flood the API with 100 simultaneous requests, show background worker consumption, and demonstrate cached response times.
