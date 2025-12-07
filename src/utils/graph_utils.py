"""
Common utilities for working with LangGraph.
"""

from pathlib import Path


def visualize_graph(
    graph, filename="graph_visualization.png", output_dir="visualizations"
):
    """
    Save graph visualization to a PNG file.

    Args:
        graph: Compiled LangGraph graph
        filename: Output filename (default: "graph_visualization.png")
        output_dir: Directory to save visualizations (default: "visualizations")

    Returns:
        True if successful, False otherwise
    """
    try:
        # Create output directory if it doesn't exist
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        # Full path for the file
        file_path = output_path / filename

        # Generate and save PNG
        png_data = graph.get_graph().draw_mermaid_png()
        with open(file_path, "wb") as f:
            f.write(png_data)

        print(f"✓ Graph visualization saved to: {file_path}")
        return True
    except Exception as e:
        print(f"✗ Could not generate visualization: {e}")
        print("  (This is optional - your graph still works!)")
        return False


def print_state(node_name, state, prefix="Input"):
    """
    Pretty print state for debugging.

    Args:
        node_name: Name of the current node
        state: Current state dictionary
        prefix: "Input" or "Output" (default: "Input")
    """
    print(f"[{node_name}] {prefix}: {state}")
