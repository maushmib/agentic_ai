from langgraph.graph import StateGraph, END
from typing import TypedDict

class ChatState(TypedDict):
    messages: list

def add_message(state: ChatState, msg: str):
    state["messages"].append(msg)
    return state

def create_graph():
    graph = StateGraph(ChatState)

    graph.add_node("start", lambda state: add_message(state, "Conversation started."))
    graph.add_node("respond", lambda state: state)  

    graph.set_entry_point("start")
    graph.add_edge("start", "respond")
    graph.add_edge("respond", END)

    return graph