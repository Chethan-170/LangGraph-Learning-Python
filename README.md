# LangGraph Learning Python

A structured repository for learning LangGraph with Python.

## Setup

1. Clone the repository
2. Ensure `uv` is installed
3. Run `uv sync` to install dependencies
4. Copy `.env.example` to `.env` and add your API keys

## Project Structure

```
LangGraph-Learning-Python/
├── src/
│   └── exercises/    # Exercise implementations
├── .python-version   # Pinned Python version
├── pyproject.toml    # Project dependencies
└── README.md
```

## LangGraph Basics

### Core Concepts

**State**: The data structure that flows through your graph. It represents the current state of your application and gets passed between nodes. Define state using TypedDict or Pydantic models.

**Nodes**: Functions that perform specific tasks. Each node receives the current state, processes it, and returns updates to the state. Nodes are the building blocks of your graph.

**Graph**: The overall structure that connects nodes together. It defines the workflow and how data flows through your application.

**Edges**: Direct connections between nodes that define the flow of execution. Once a node completes, edges determine which node runs next.

**Conditional Edges**: Dynamic routing based on the current state. They allow your graph to make decisions about which path to take based on logic you define.

**Start**: The entry point of your graph. This is where execution begins and the initial state enters the workflow.

**End**: The terminal point of your graph. When execution reaches an end node, the graph completes and returns the final state.

**StateGraph**: The main class used to build your graph. You define nodes, add edges, set the entry point, and compile the graph into an executable workflow.

### Basic Pattern

```python
from langgraph.graph import StateGraph, START, END
from typing import TypedDict

# Define your state
class State(TypedDict):
    messages: list[str]
    count: int

# Create the graph
graph = StateGraph(State)

# Add nodes
graph.add_node("process", process_function)
graph.add_node("validate", validate_function)

# Add edges
graph.add_edge(START, "process")
graph.add_conditional_edges("process", routing_function)
graph.add_edge("validate", END)

# Compile and run
app = graph.compile()
result = app.invoke(initial_state)
```

## Branch Strategy

Each exercise will be in its own branch:

- `master` - Base setup and documentation
- `exercise-01-linear-chain` - First exercise
- `exercise-02-conditional-routing` - Second exercise
- etc.

## Running Code

```bash
# Run any Python file
uv run python src/exercises/01_linear_chain.py

# This will:
# 1. Print debug output to console
# 2. Generate a PNG visualization of the graph
# 3. Show the final results

# Format code
uv run ruff format .

# Check code for issues
uv run ruff check .
```

## Viewing Graph Visualizations

After running any exercise, you'll get a PNG file showing your graph structure:

- `graph_visualization.png` - Shows nodes, edges, and flow
- Open with any image viewer
- Great for understanding what you built!

## Learning Path

1. Basic graph creation
2. State management
3. Conditional edges
4. Human-in-the-loop
5. Persistence and checkpoints
6. Advanced patterns

## Quick Reference Commands

```bash
# Add a new dependency
uv add package-name

# Run Python with project environment
uv run python script.py

# Format your code
uv run ruff format .

# Check for code issues
uv run ruff check .

# Fix issues automatically
uv run ruff check --fix .

# Sync dependencies (after pulling changes)
uv sync

# Create a new branch for an exercise
git checkout -b exercise-01-linear-chain
```

## Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangChain Documentation](https://python.langchain.com/)
- [uv Documentation](https://docs.astral.sh/uv/)
