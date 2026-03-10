from langgraph.graph import StateGraph, END
from typing import TypedDict
from tools import (
    log_interaction,
    edit_interaction,
    get_doctor_history,
    summarize_interaction,
    suggest_next_action
)


class AgentState(TypedDict):
    message: str
    result: str


def agent_node(state: AgentState):

    message = state["message"].lower()

    if "edit" in message:
        output = edit_interaction(state["message"])

    elif "history" in message:
        output = get_doctor_history(state["message"])

    elif "summarize" in message:
        output = summarize_interaction(state["message"])

    elif "suggest" in message:
        output = suggest_next_action(state["message"])

    else:
        output = log_interaction(state["message"])

    return {"result": output}


workflow = StateGraph(AgentState)

workflow.add_node("agent", agent_node)

workflow.set_entry_point("agent")

workflow.add_edge("agent", END)

graph = workflow.compile()