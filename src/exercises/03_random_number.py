"""
Exercise 03: Generate Random Number for 5 times using Looping
====================================================
"""

import sys
from pathlib import Path
from typing import TypedDict

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.utils.graph_utils import visualize_graph, print_state
from langgraph.graph import START, END, StateGraph

import random


class AgentState(TypedDict):
    """State that flows through the graph."""

    name: str
    counter: int
    random_numbers: list[int]


def greeting_node(state: AgentState) -> AgentState:
    """Greet the agent"""
    print_state("greeting_node", state, "Input")
    state["name"] = f"Hello, {state['name']}! Let's generate some random numbers."
    print_state("greeting_node", state, "Output")
    return state


def random_number_node(state: AgentState) -> AgentState:
    """Generate a random number and append to the list"""
    print_state("random_number_node", state, "Input")
    rand_num = random.randint(1, 10)
    state["random_numbers"].append(rand_num)
    state["counter"] += 1
    print_state("random_number_node", state, "Output")
    return state


def should_continue(state: AgentState) -> AgentState:
    """Check if we have generated 5 random numbers"""
    print_state("check_counter_node", state, "Input")
    if state["counter"] < 5:
        return "loop_edge"
    else:
        return "exit_edge"


def create_random_number_graph():
    """Create and compile the random number generation graph."""
    workflow = StateGraph(AgentState)

    # Add nodes
    workflow.add_node("greeting", greeting_node)
    workflow.add_node("random", random_number_node)

    # Set entry point
    workflow.set_entry_point("greeting")

    # Add edges
    # workflow.add_edge(START, "greeting")
    workflow.add_edge("greeting", "random")

    # Conditional edges based on counter check
    workflow.add_conditional_edges(
        "random",
        should_continue,
        {
            "loop_edge": "random",
            "exit_edge": END,
        },
    )

    # Compile the graph
    return workflow.compile()


def main():
    """Main function to run the random number generation graph."""

    # Create and run the graph
    graph = create_random_number_graph()

    # Visualize the graph
    visualize_graph(graph, "random_number_graph.png")

    # Initial state
    initial_state: AgentState = {
        "name": "Agent007",
        "counter": 0,
        "random_numbers": [],
    }

    final_state = graph.invoke(initial_state)

    print("\nFinal State:")
    print(final_state)


if __name__ == "__main__":
    main()
