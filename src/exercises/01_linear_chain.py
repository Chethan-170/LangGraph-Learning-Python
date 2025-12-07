"""
Exercise 01: Simple Linear Chain
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from typing import TypedDict

from langgraph.graph import END, StateGraph

from src.utils.graph_utils import visualize_graph, print_state


class TextState(TypedDict):
    """State that flows through the graph."""

    text: str
    word_count: int


def uppercase_node(state: TextState) -> TextState:
    """Convert text to uppercase."""
    print_state("uppercase_node", state, "Input")
    result = {"text": state["text"].upper(), "word_count": state["word_count"]}
    print_state("uppercase_node", result, "Output")
    return result


def add_prefix_node(state: TextState) -> TextState:
    """Add 'PROCESSED: ' prefix to the text."""
    print_state("add_prefix_node", state, "Input")
    result = {
        "text": f"PROCESSED: {state['text']}",
        "word_count": state["word_count"],
    }
    print_state("add_prefix_node", result, "Output")
    return result


def count_words_node(state: TextState) -> TextState:
    """Count the number of words in the text."""
    print_state("count_words_node", state, "Input")
    words = state["text"].split()
    result = {"text": state["text"], "word_count": len(words)}
    print_state("count_words_node", result, "Output")
    return result


def create_linear_graph():
    """Create and compile the linear graph."""
    workflow = StateGraph(TextState)

    # Add nodes
    workflow.add_node("uppercase", uppercase_node)
    workflow.add_node("add_prefix", add_prefix_node)
    workflow.add_node("count_words", count_words_node)

    # Set entry point
    workflow.set_entry_point("uppercase")

    # Add edges (linear chain)
    workflow.add_edge("uppercase", "add_prefix")
    workflow.add_edge("add_prefix", "count_words")
    workflow.add_edge("count_words", END)

    return workflow.compile()


def main():
    """Run the exercise."""
    graph = create_linear_graph()

    # Visualize the graph (using common utility)
    visualize_graph(graph, "01_linear_chain_solution_visualization.png")

    # Test with different inputs
    test_cases = [
        "hello world this is langgraph",
        "learning graphs is fun",
        "one",
    ]

    print("\nRunning Linear Chain Graph:\n")
    for input_text in test_cases:
        print(f"{'=' * 60}")
        print(f"Input: {input_text}")
        print(f"{'=' * 60}")

        result = graph.invoke({"text": input_text, "word_count": 0})

        print(f"\n{'=' * 60}")
        print(f"RESULTS:")
        print(f"  Original: {input_text}")
        print(f"  Processed: {result['text']}")
        print(f"  Word Count: {result['word_count']}")
        print(f"{'=' * 60}\n\n")


if __name__ == "__main__":
    main()
