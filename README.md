<div align="center">

# 🏛️ Sanctum

**The dialectical sparring partner that stress-tests your convictions.**

*An air-gapped, local-first adversarial engine built with FastAPI, Model Context Protocol (MCP), LanceDB, and continuous Ragas evaluation.*

<br/>

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-3776AB.svg?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688.svg?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![MCP Standard](https://img.shields.io/badge/protocol-MCP_2024--11-6B46C1.svg?style=flat-square)](https://modelcontextprotocol.io/)
[![Ragas Benchmark](https://img.shields.io/badge/eval-Ragas_0.2+-FF6F61.svg?style=flat-square)](https://docs.ragas.io/)
[![LanceDB](https://img.shields.io/badge/vector_db-LanceDB_Embedded-blue.svg?style=flat-square)](https://lancedb.com/)
[![Kubernetes Ready](https://img.shields.io/badge/deploy-k8s_manifests-326CE5.svg?style=flat-square&logo=kubernetes&logoColor=white)](https://kubernetes.io/)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache_2.0-black.svg?style=flat-square)](LICENSE)

<br/>

[The Philosophy](#-the-philosophy) •
[The Dialectical Engine](#-how-it-works-the-dialectical-loop) •
[Architecture](#-system-architecture) •
[Quickstart](#-quickstart) •
[Live Session Preview](#-live-session-preview) •
[Evaluation](#-ragas-truth-guardrails) •
[Deployment](#-kubernetes-deployment)

</div>

---

> *"The aim of argument should not be victory, but progress."*  
> — Joseph Joubert  

Most AI assistants suffer from **systemic sycophancy**: they smile, flatter your premises, and hallucinate consensus. If you present a flawed architectural decision, an unverified macroeconomic take, or a one-sided news interpretation, standard models will politely validate your cognitive bias.

**Sanctum does the opposite.**

Operating entirely on your local machine, Sanctum acts as an intellectual sparring partner. It interrogates your claims against primary source records, historical post-mortems, and conflicting viewpoints. It is not an unhelpful contrarian; it follows classical dialectics to systematically burn away weak assumptions until only battle-tested, defensible truth remains.

---

## 🧭 The Philosophy: Dialectics, Not Debating for Sport

A contrarian that never yields is just a troll. Sanctum solves this by grounding every conversation in a strict four-stage conversational arc:

```text
 ┌───────────────┐        ┌───────────────────┐        ┌───────────────────┐        ┌─────────────────┐
 │   1. THESIS   │  ───►  │  2. STEELMANNING  │  ───►  │   3. ANTITHESIS   │  ───►  │  4. SYNTHESIS   │
 │  Your claim   │        │   Best defense    │        │  Cross-exam & MCP │        │  Battle-tested  │
 └───────────────┘        └───────────────────┘        └─────────┬─────────┘        └─────────────────┘
                                                                 │
                                                                 ▼
                                                    [ Register of Concessions ]
                                                    • Proven claims locked
                                                    • Immutable SQLite ledger
```

* **The Steelmanning Gate:** Before Sanctum is permitted to attack your premise, it must articulate the *strongest possible version* of your argument. Cheap straw men and semantic nitpicks are rejected by the system.
* **Empirical Cross-Examination:** The model retrieves counter-evidence, contrasting perspectives, and primary statistical filings using isolated **Model Context Protocol (MCP)** tools.
* **The Register of Concessions:** Whenever you provide verified empirical proof or sound deductive logic that defeats an objection, Sanctum formally concedes the point. This concession is written to an immutable session ledger—once conceded, the agent is strictly forbidden from re-challenging that point.
* **Dialectical Synthesis:** When the points of friction have been resolved, the adversarial posture drops. Sanctum delivers a refined synthesis: what survived the test, which assumptions were stripped away, and the exact boundaries where your thesis holds true.

---

## ⚡ System Architecture

Sanctum is built from scratch to showcase modern, production-grade AI engineering: asynchronous orchestration, tool process isolation, and continuous evaluation.

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        Sanctum Host (FastAPI)                          │
│                                                                        │
│  ┌───────────────────────┐             ┌────────────────────────────┐  │
│  │ Local LLM Engine      │             │ Orchestration Plane        │  │
│  │ (Ollama / llama.cpp)  │◄───────────►│ • Dialectical State Router │  │
│  │  Qwen 2.5 / Llama 3.3 │             │ • Real-Time SSE Streamer   │  │
│  └───────────────────────┘             │ • Untrusted Context Gate   │  │
│                                        └──────────────┬─────────────┘  │
└───────────────────────────────────────────────────────┼────────────────┘
                                                        │ JSON-RPC (stdio)
                ┌───────────────────────────────────────┴─────────────────┐
                ▼                                                         ▼
     ┌───────────────────────┐                                 ┌───────────────────────┐
     │ Evidence Vault MCP    │                                 │ Concessions MCP       │
     │ • LanceDB Vector DB   │                                 │ • SQLite Ledger       │
     │ • Trafilatura Cleaner │                                 │ • Locked Claim Guard  │
     └───────────────────────┘                                 └───────────────────────┘
```

### The Engineering Pillars

* **FastAPI Orchestration Plane:** Enforces the finite state machine transitions, controls context delimiters, and streams tokens and tool calls via Server-Sent Events (SSE).
* **Anthropic MCP Layer:** Isolates tools into lightweight child processes over standard I/O (`stdio`). If an ingestion script hangs or a database read times out, the main agent never crashes.
* **Dual-Track Knowledge Vault:** Ingests articles, policy filings, and post-mortems via `trafilatura` to strip ads and layout clutter. Chunks are stored in an in-process, serverless LanceDB table with zero cloud egress.
* **Continuous Truth Evaluation (Ragas):** In an adversarial debate, the model is under pressure to "win." Sanctum uses automated Ragas benchmarks to mathematically penalize ungrounded rebuttals or hallucinated citations.
* **Air-Gapped Kubernetes Packaging:** Packaged with declarative manifests enforcing strict memory limits, NVMe persistent volume mounts, and zero-egress network policies.

---

## 🚀 Quickstart

### Prerequisites

* **Python 3.11+**
* **Local Inference:** [Ollama](https://ollama.ai) running locally (`ollama serve`)
* **Recommended Model:** `qwen2.5:14b` or `llama3.3:8b` (both excel at strict tool calling)

```bash
# Pull the recommended model
ollama pull qwen2.5:14b
```

### 1. Installation

```bash
git clone [https://github.com/yourusername/sanctum.git](https://github.com/yourusername/sanctum.git)
cd sanctum

python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[eval]"
```

### 2. Configure Environment

```bash
cp .env.example .env
```

Your default `.env` works out of the box for local Ollama setups:

```ini
SANCTUM_OLLAMA_BASE_URL=http://localhost:11434
SANCTUM_MODEL_NAME=qwen2.5:14b
SANCTUM_EMBEDDING_MODEL=BAAI/bge-small-en-v1.5
SANCTUM_DATA_DIR=./data
```

### 3. Launch Sanctum

```bash
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
```

The interactive API dashboard will be live at `http://localhost:8000/docs`.

---

## 💬 Live Session Preview

### 1. Ingest Background Material

Before sparring over a complex topic, seed the vault with a URL, policy paper, or engineering post-mortem:

```bash
curl -X POST http://localhost:8000/api/v1/vault/ingest \
  -H "Content-Type: application/json" \
  -d '{
    "source_url": "[https://example.com/clean-energy-macroeconomics](https://example.com/clean-energy-macroeconomics)",
    "topic": "energy_markets"
  }'
```

### 2. Stream a Sparring Turn

```bash
curl -N -X POST http://localhost:8000/api/v1/debate/stream \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "session-42",
    "thesis": "Solar plus short-duration battery storage will completely eliminate the need for baseload gas within five years."
  }'
```

Sanctum streams structured events and reasoning tokens via Server-Sent Events:

```text
event: state_transition
data: {"phase": "STEELMANNING"}

event: token
data: {"content": "Formulating the strongest case for your position: Solar deployment curves and declining lithium-ion pack costs have consistently outpaced legacy energy agency projections..."}

event: state_transition
data: {"phase": "ANTITHESIS"}

event: tool_call
data: {"server": "evidence_vault", "tool": "search_counterevidence", "query": "seasonal intermittency grid inertia multi-day dunkelflaute"}

event: token
data: {"content": "However, empirical grid data reveals a critical failure point. In high-latitude grids, multi-day winter lulls require seasonal, multi-week storage duration rather than 4-hour battery balancing..."}
```

---

## 🎯 Ragas Truth Guardrails

An adversarial model must not resort to bluffing, misquoting numbers, or citing phantom studies. Sanctum runs an automated evaluation harness to verify that every counter-argument is anchored in retrieved ground truth.

```bash
# Run the continuous truth benchmark suite
python -m evaluation.evaluator --threshold 0.85
```

| Metric | Threshold | Why It Matters |
| :--- | :---: | :--- |
| **Faithfulness** | $\ge 0.88$ | Ensures every adversarial counter-claim is derived directly from retrieved passages, completely eliminating hallucinated statistics. |
| **Context Precision** | $\ge 0.82$ | Verifies that the MCP search tools retrieve high-signal primary sources rather than irrelevant noise. |
| **Answer Relevance** | $\ge 0.85$ | Guarantees the agent addresses your actual premise rather than sliding into evasive rhetoric. |

---

## ☸️ Kubernetes Deployment

Sanctum includes production-ready manifests designed for local clusters (k3s, Minikube, k3d) that enforce full air-gapped isolation:

```bash
# 1. Create persistent storage for LanceDB and SQLite
kubectl apply -f k8s/pvc.yaml

# 2. Apply zero-egress network policy (blocks unauthorized outbound telemetry)
kubectl apply -f k8s/network-policy.yaml

# 3. Deploy Sanctum with strict cgroup CPU/memory quotas
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

```yaml
# Strict compute boundaries in k8s/deployment.yaml
resources:
  requests:
    cpu: "2000m"
    memory: "2Gi"
  limits:
    cpu: "4000m"
    memory: "4Gi"
```

---

## 📂 Project Structure

```text
sanctum/
├── api/                  # FastAPI routers, SSE streaming, and state machine
│   ├── routers/          # /debate, /vault, and /eval endpoints
│   └── state_machine.py  # Dialectical transition guards and session tracking
├── core/                 # Untrusted context delimiters and prompt schemas
├── mcp_servers/          # Model Context Protocol servers (stdio JSON-RPC)
│   ├── evidence_vault/   # LanceDB semantic search & primary source retrieval
│   └── concessions/      # SQLite-backed immutable Register of Concessions
├── ingestion/            # Trafilatura HTML cleaner & markdown chunker
├── evaluation/           # Ragas benchmark suite and synthetic test generator
├── k8s/                  # Zero-egress manifests, PVCs, and resource limits
└── pyproject.toml        # Unified project dependencies and tooling configs
```

---

## 📄 License

Sanctum is open-source software licensed under the **[Apache License 2.0](LICENSE)**.