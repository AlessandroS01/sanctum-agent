from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph
from sanctum.graph.nodes import antithesis_node, steelman_node, synthesis_node
from sanctum.graph.state import DialecticalState


def route_debate(state: DialecticalState) -> str:
    last_message = (
        state["messages"][-1].content.lower() if state["messages"] else ""
    )
    if (
        "synthesize" in last_message
        or "conclude" in last_message
        or state.get("turn_count", 0) >= 4
    ):
        return "synthesis"
    return "antithesis"


builder = StateGraph(DialecticalState)
builder.add_node("steelman", steelman_node)
builder.add_node("antithesis", antithesis_node)
builder.add_node("synthesis", synthesis_node)

builder.add_edge(START, "steelman")
builder.add_edge("steelman", "antithesis")
builder.add_conditional_edges(
    "antithesis",
    route_debate,
    {
        "antithesis": "antithesis",
        "synthesis": "synthesis",
    },
)
builder.add_edge("synthesis", END)

checkpointer = MemorySaver()

# Both nodes now interrupt to wait for human input
sanctum_graph = builder.compile(
    checkpointer=checkpointer,
    interrupt_after=["steelman", "antithesis"],
)