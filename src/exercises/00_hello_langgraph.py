"""
Exercise 0: Hello LangGraph
A simple example to verify setup is working.
"""

import sys
from pathlib import Path
from typing import TypedDict

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from langgraph.graph import END, StateGraph
from src.utils.graph_utils import visualize_graph, print_state


class State(TypedDict):
    """Define the state structure."""

    message: str


def hello_node(state: State) -> State:
    """A simple node that updates the message."""
    print_state("hello_node", state, "Input")
    result = {"message": f"Hello from LangGraph! Original: {state['message']}"}
    print_state("hello_node", result, "Output")
    return result


def create_hello_graph():
    """Create a simple graph."""
    workflow = StateGraph(State)

    # Add nodes
    workflow.add_node("hello", hello_node)

    # Set entry point
    workflow.set_entry_point("hello")

    # Add edge to end
    workflow.add_edge("hello", END)

    return workflow.compile()


if __name__ == "__main__":
    # Create the graph
    graph = create_hello_graph()

    # Visualize the graph structure
    visualize_graph(graph, "00_hello_visualization.png")

    # Run the graph
    print("\nRunning graph:")
    result = graph.invoke({"message": "World"})
    print(f"\nFinal Result: {result}")
