"""
Exercise 02: Simple Coditional Routing
===========================================
"""

import sys
from pathlib import Path
from typing import TypedDict

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.utils.graph_utils import visualize_graph, print_state
from langgraph.graph import START, END, StateGraph


class CalcState(TypedDict):
    """State that flows through the graph."""

    a: int
    b: int
    operation: str  # 'add' or 'subtract'
    result: int


def addition_node(state: CalcState) -> CalcState:
    """Perform addition"""
    print_state("addition_node", state, "Input")
    state["result"] = state["a"] + state["b"]
    print_state("addition_node", state, "Output")
    return state


def subtraction_node(state: CalcState) -> CalcState:
    """Perform subtraction"""
    print_state("subtraction_node", state, "Input")
    state["result"] = state["a"] - state["b"]
    print_state("subtraction_node", state, "Output")
    return state


def decide_next_node_func(state: CalcState) -> CalcState:
    """Route based on operation"""
    print_state("router_node", state, "Input")
    if state["operation"] == "add":
        # return named edge
        return "addition_operation"
    elif state["operation"] == "subtract":
        # return named edge
        return "subtraction_operation"
    else:
        raise ValueError("Unsupported operation")


def create_conditional_graph():
    """Create and compile the conditional routing graph."""
    workflow = StateGraph(CalcState)

    # Add nodes
    workflow.add_node("addition", addition_node)
    workflow.add_node("subtraction", subtraction_node)
    # router node return current state as is
    workflow.add_node("router", lambda state: state)  # Passthrough function

    # Set entry point
    workflow.set_entry_point("router")
    # alternatively, you can write:
    # workflow.add_edge(START, "router")

    # Add conditional edges
    workflow.add_conditional_edges(
        "router",
        # function that decides the next node based on the state returned from router node
        decide_next_node_func,
        {
            # Edge: Node
            "addition_operation": "addition",
            "subtraction_operation": "subtraction",
        },
    )

    # Add edges to end
    workflow.add_edge("addition", END)
    workflow.add_edge("subtraction", END)

    return workflow.compile()


def main():
    """Run the exercise."""
    graph = create_conditional_graph()

    # Visualize the graph structure
    visualize_graph(graph, "02_conditional_visualization.png")

    # Run the graph with addition
    print("\nRunning graph for addition:")
    result_add = graph.invoke({"a": 10, "b": 5, "operation": "add", "result": 0})
    print(f"\nFinal Result (Addition): {result_add}")

    # Run the graph with subtraction
    print("\nRunning graph for subtraction:")
    result_sub = graph.invoke({"a": 10, "b": 5, "operation": "subtract", "result": 0})
    print(f"\nFinal Result (Subtraction): {result_sub}")


if __name__ == "__main__":
    main()
