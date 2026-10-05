from typing import Annotated, Sequence, TypedDict
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class DialecticalState(TypedDict):
    """The central epistemic state tracking the dialectical progression."""

    messages: Annotated[Sequence[BaseMessage], add_messages]
    thesis: str
    steelman: str
    concessions: list[str]
    phase: str
    turn_count: int