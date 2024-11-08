from creature import Creature
from exceptions import PositionOccupiedError
from position import Position


class World:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid = [
            [None for _ in range(self.grid_size)] for _ in range(self.grid_size)
        ]
        self.creatures = {}  # id: Creature

    def add_creature(self, creature: Creature):
        if not creature.get_position():
            raise ValueError("Creature must have a position.")
        if self.grid[creature.position.x][creature.position.y]:
            raise PositionOccupiedError

        pos = creature.get_position()
        self.grid[pos.x][pos.y] = creature.id
        self.creatures[creature.id] = creature

    def __repr__(self) -> str:
        s = ""
        for row in self.grid:
            for cell in row:
                if cell:
                    s += f"{cell} "
                else:
                    s += ". "
            s += "\n"
        return s
