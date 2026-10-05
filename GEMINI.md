# Sanctum: Project Context & AI Directives

## Core Mission and Philosophy
Sanctum is an air-gapped, local-first dialectical epistemic engine. Its purpose is to act as an unyielding adversarial sparring partner that stress-tests human arguments against empirical evidence, historical incident post-mortems, and contrasting primary sources. 

The system explicitly rejects sycophancy. It does not validate cognitive bias or seek polite compromise. Instead, it follows a strict four-stage dialectical arc: Steelmanning, Antithesis cross-examination, Concession logging, and Synthesis. The finish line is always battle-tested truth, achieved by burning away weak assumptions while formally preserving validated premises.

## Architectural Constraints and Stack
The system operates completely offline without external telemetry or third-party cloud APIs.

- Language and Runtime: Python 3.13 managed via Conda (`sanctum` environment).
- Orchestration and State Machine: LangGraph manages the dialectical workflow, interrupt checkpoints, and conversation memory.
- Local Inference: Ollama serving open-weight models locally, primarily `qwen3.5:0.8b`.
- Tool Isolation: Model Context Protocol (MCP) servers communicating over standard input and output (stdio) via JSON-RPC.
- Knowledge Vault: In-process LanceDB for vector retrieval paired with Trafilatura for extracting clean Markdown from ingested sources.
- Ledger: SQLite for maintaining the immutable Register of Concessions.
- Web Layer: FastAPI providing Server-Sent Events (SSE) for streaming graph transitions and deliberation tokens.
- Evaluation: Ragas benchmark suite enforcing mathematical thresholds on rebuttal faithfulness and context precision.

## Repository Layout (src layout)
All application logic lives under the `src/` directory to guarantee clean module resolution:

- `src/sanctum/graph/`: LangGraph state definitions, node functions, and workflow assembly.
- `src/sanctum/mcp/`: Standalone MCP server scripts and tool definitions for vector lookup and concession tracking.
- `src/sanctum/vault/`: Trafilatura ingestion pipelines, chunking utilities, and LanceDB storage interfaces.
- `src/sanctum/api/`: FastAPI route handlers and real-time streaming endpoints.
- `scripts/`: Operational CLI entry points, including the interactive terminal debate runner.
- `tests/`: Pytest suites covering graph state transitions, tool safety, and prompt parsing.

## Engineering Standards for Gemini
When writing or modifying code in this repository, follow these rules:

1. Type Integrity: Use strict Python type annotations everywhere. Rely on Pydantic v2 models for data boundaries and LangGraph TypedDict schemas for graph states.
2. Dialectical Integrity: Never allow the agent to skip the steelmanning phase. Ensure the model cannot challenge points already recorded in the concession ledger.
3. Process Isolation: Keep tool logic completely decoupled from prompt logic. Tools must run as isolated MCP routines rather than in-memory prompt hacks.
4. Privacy and Air-Gapping: Never suggest cloud-hosted embedding or LLM services. All computation, storage, and evaluation must remain local.
5. Code Style: Favor explicit, maintainable Python using standard libraries where possible. Keep functions focused and well-documented.
6. Development Workflow: Make changes to the codebase to fulfil `ruff check` and `ruff format` before running any other commands.

## Common Development Commands
Create and activate the Conda environment:
`conda create -n sanctum python=3.13 -y`
`conda activate sanctum`

Install the package in editable mode with development tools:
`pip install -e ".[dev]"`

Run the terminal sparring session:
`python scripts/run_cli.py`

Run test suites:
`pytest tests/`