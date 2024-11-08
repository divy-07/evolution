from move_algorithms import l2_norm
from constants import Direction
from position import Position


class Creature:

    NEXT_ID = 1

    def __init__(self):
        self.id = Creature.NEXT_ID
        Creature.NEXT_ID += 1
        self.params = None
        self.position = None

    def __repr__(self):
        return f"Creature {self.id}"

    def set_params(self, params: list[int]):
        if not self.params:
            self.params = params

    def next_move(self):
        move = l2_norm(self.params)
        return Direction(move)

    def set_position(self, position: Position):
        self.position = position

    def get_position(self) -> Position:
        return self.position
