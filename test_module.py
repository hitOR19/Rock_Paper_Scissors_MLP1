"""
test_module.py

This module provides simple testing utilities for validating
the performance of the Rock–Paper–Scissors AI bot.

It runs the player function against predefined opponent bots
and displays the win rate.

This file is for local testing purposes only and does not
affect the core logic of the project.
"""

from RPS_game import play, quincy, abbey, kris, mrugesh


def test_player(player_func):
    """
    Test the given player function against all bots.
    """

    print("\nRunning tests for player function...\n")

    bots = [
        ("Quincy", quincy),
        ("Abbey", abbey),
        ("Kris", kris),
        ("Mrugesh", mrugesh)
    ]

    for name, bot in bots:
        print(f"Testing against {name}:")
        play(player_func, bot, 1000)
        print("-" * 40)


# Optional: run tests directly
if __name__ == "__main__":
    from RPS import player
    test_player(player)