"""
Exercise 04: Guessing Game
===========================
A simple guessing game where the player has to guess a randomly generated number within a limited number of attempts.

Main features:
- Welcome the player.
- Generate a random target number.
- Allow the player to make guesses.
- Provide hints (higher/lower) after each guess.
- End the game when the player guesses correctly or exhausts attempts.
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


class GameState(TypedDict):
    player_name: str
    guesses: list[int]
    target_number: int
    hints: list[str]


def welcome_node(state: GameState) -> GameState:
    """Welcome the player"""
    print(f"Welcome, {state['player_name']}! Let's play a guessing game.")
    print_state("welcome_node", state, "Output")
    return state


def setup_game_node(state: GameState) -> GameState:
    """Set up the game by generating a target number"""
    state["target_number"] = random.randint(1, 20)
    state["guesses"] = []
    state["hints"] = []
    print_state("setup_game_node", state, "Output")
    return state


def guessing_node(state: GameState) -> GameState:
    """Simulate a player making a guess"""
    attempts = len(state["guesses"])
    if attempts == 0:
        state["guesses"].append(random.randint(1, 20))
    else:
        hintText = state["hints"][-1]
        lastGuessedNumber = state["guesses"][-1]
        if hintText == "higher":
            state["guesses"].append(random.randint(lastGuessedNumber + 1, 20))
        else:
            state["guesses"].append(random.randint(1, lastGuessedNumber - 1))

    print_state("guessing_node", state, "Output")
    return state


def evaluate_and_hint_node(state: GameState) -> GameState:
    """Evaluate the guess and provide a hint"""
    current_guess = state["guesses"][-1]
    if current_guess < state["target_number"]:
        state["hints"].append("higher")
    elif current_guess > state["target_number"]:
        state["hints"].append("lower")
    else:
        state["hints"].append("correct")
    print_state("evaluate_and_hint_node", state, "Output")
    return state


def game_status_checker(state: GameState) -> GameState:
    """Check the game status and proceed accordingly"""
    attemts = len(state["guesses"])

    is_correct_guess = False
    if len(state["hints"]) > 0 and state["hints"][-1] == "correct":
        is_correct_guess = True

    if is_correct_guess:
        print_state("game_status_checker", state, "Output - Game Won")
        return "end_game_edge"
    elif attemts == 5:
        print_state("game_status_checker", state, "Output - Max attempts reached")
        return "end_game_edge"
    else:
        print_state("game_status_checker", state, "Output - Continue guessing")
        return "continue_guessing_edge"


def create_guessing_game_graph():
    """Create and compile the guessing game graph"""
    workflow = StateGraph(GameState)

    # Add Nodes
    workflow.add_node("welcome", welcome_node)
    workflow.add_node("setup_game", setup_game_node)
    workflow.add_node("guessing", guessing_node)
    workflow.add_node("evaluate_and_hint", evaluate_and_hint_node)

    # Add Normal Edges
    workflow.set_entry_point("welcome")
    workflow.add_edge("welcome", "setup_game")
    workflow.add_edge("setup_game", "guessing")
    workflow.add_edge("guessing", "evaluate_and_hint")

    # Add Condtional Edges
    workflow.add_conditional_edges(
        "evaluate_and_hint",
        game_status_checker,
        {"continue_guessing_edge": "guessing", "end_game_edge": END},
    )

    return workflow.compile()


def main():
    """Main function to run the guessing game graph."""

    # Create and run the graph
    graph = create_guessing_game_graph()

    # Visualize the graph
    visualize_graph(graph, "guessing_game_graph.png")

    final_state = graph.invoke(
        {"player_name": "Player123", "guesses": [], "target_number": 0, "hints": []}
    )
    if final_state["hints"] and final_state["hints"][-1] == "correct":
        print(
            f"Congratulations {final_state['player_name']}! You've guessed the number {final_state['target_number']} correctly in {len(final_state['guesses'])} attempts."
        )
    else:
        print(
            f"Game Over! The correct number was {final_state['target_number']}. Better luck next time!"
        )


if __name__ == "__main__":
    main()
