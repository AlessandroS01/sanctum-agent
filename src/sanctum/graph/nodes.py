from typing import Any

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_ollama import ChatOllama

from sanctum.graph.state import DialecticalState

llm = ChatOllama(model="qwen3.5:0.8b", temperature=0.1)


def steelman_node(state: DialecticalState) -> dict[str, Any]:
    """Construct the strongest possible version of the user's premise."""
    messages = [
        SystemMessage(
            content=(
                "You are an epistemic sparring partner. Construct the strongest "
                "possible version of the user's premise (steelmanning). Detail the "
                "best empirical and logical arguments supporting their claim without "
                "attacking it."
            )
        ),
        HumanMessage(content=f"Please steelman my thesis: {state['thesis']}"),
    ]
    response = llm.invoke(messages)
    return {
        "steelman": response.content,
        "phase": "steelmanning",
        "messages": [AIMessage(content=f"### Steelmanned Core\n\n{response.content}")],
    }


def antithesis_node(state: DialecticalState) -> dict[str, Any]:
    """Stress-test the thesis against edge cases and unverified assumptions."""
    concessions_formatted = (
        "\n".join(f"- {c}" for c in state.get("concessions", [])) or "None logged yet."
    )
    system_instruction = (
        "You are the Inquisitor. Stress-test the user's thesis. Look for unverified "
        "assumptions, edge-case failure modes, and systemic trade-offs.\n"
        "Rules:\n"
        "1. Never attack surface semantics; challenge the underlying mechanism.\n"
        "2. Do not re-challenge points listed under Locked Concessions.\n"
        "3. Focus on one critical vulnerability per turn.\n\n"
        f"Initial Thesis: {state['thesis']}\n"
        f"Steelmanned Baseline: {state['steelman']}\n"
        f"Locked Concessions:\n{concessions_formatted}"
    )

    call_messages = [SystemMessage(content=system_instruction)] + list(
        state["messages"]
    )
    response = llm.invoke(call_messages)
    return {
        "phase": "antithesis",
        "turn_count": state.get("turn_count", 0) + 1,
        "messages": [response],
    }


def synthesis_node(state: DialecticalState) -> dict[str, Any]:
    """Synthesize battle-tested conclusions after adversarial pressure testing."""
    concessions_formatted = (
        "\n".join(f"- {c}" for c in state.get("concessions", [])) or "None."
    )
    prompt = (
        "The adversarial phase is finished. Provide an objective, "
        "battle-tested synthesis:\n"
        "1. What survived the pressure testing.\n"
        "2. What assumptions were falsified or stripped away.\n"
        "3. The explicit operational boundaries where the thesis remains true.\n\n"
        f"Original Thesis: {state['thesis']}\n"
        f"Concessions:\n{concessions_formatted}"
    )

    call_messages = [SystemMessage(content=prompt)] + list(state["messages"])
    response = llm.invoke(call_messages)
    return {
        "phase": "synthesis",
        "messages": [
            AIMessage(content=f"### Battle-Tested Synthesis\n\n{response.content}")
        ],
    }
