"""
The functions in this file convert a float in [0,1] into a move.
These are used to determine the creature's next move.
"""

from simulator.position import ALL_DIRECTIONS, Direction


def linear(move: float) -> Direction:
    i = min(int(move * len(ALL_DIRECTIONS)), len(ALL_DIRECTIONS) - 1)
    return ALL_DIRECTIONS[i]
