from typing import TypedDict

from langgraph.graph import END, StateGraph

from adapters.common import submit_to_authority


class DeploymentState(TypedDict, total=False):
    request: dict
    decision: dict


def evaluate(state: DeploymentState) -> DeploymentState:
    return {"decision": submit_to_authority(state["request"])}


def run(request: dict) -> dict:
    graph = StateGraph(DeploymentState)
    graph.add_node("authority_boundary", evaluate)
    graph.set_entry_point("authority_boundary")
    graph.add_edge("authority_boundary", END)
    return graph.compile().invoke({"request": request})["decision"]

