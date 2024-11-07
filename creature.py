from move_algorithms import sum_mod_algo
from constants import Direction


class Creature:

    NEXT_ID = 1

    def __init__(self):
        self.id = Creature.NEXT_ID
        Creature.NEXT_ID += 1
        self.params = []

    def __repr__(self):
        return f"Creature {self.id}"

    def set_params(self, params):
        self.params = params

    def next_move(self):
        move = sum_mod_algo(self.params)
        return Direction(move)
