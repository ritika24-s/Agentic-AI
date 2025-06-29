from typing import Annotated
from typing_extensions import TypedDict

from langgraph.graph.message import add_messages


class State(TypedDict):
    """
    The state of the chatbot.
    """
    messages: Annotated[list[str], add_messages]

