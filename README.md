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
