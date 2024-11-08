from typing import List

from conversion_algorithms import linear
from evaluation_algorithms import sigmoid
from position import Direction, Position


class Creature:

    NEXT_ID = 1

    def __init__(self, eval_algo, conversion_algo):
        self.id = Creature.NEXT_ID
        Creature.NEXT_ID += 1
        self.params = None
        self.position = None
        self.eval_algo = eval_algo
        self.conversion_algo = conversion_algo

    def __repr__(self):
        return f"Creature {self.id}"

    def set_params(self, params: List[int]):
        if not self.params:
            self.params = params

    def next_direction(self) -> Direction:
        move = self.eval_algo(self.params)
        return self.conversion_algo(move)

    def set_position(self, position: Position):
        self.position = position

    def get_position(self) -> Position:
        return self.position
