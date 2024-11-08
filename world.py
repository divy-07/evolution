from creature import Creature
from exceptions import PositionOccupiedError
from position import Position


class World:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid = [
            [None for _ in range(self.grid_size)] for _ in range(self.grid_size)
        ]
        self.creatures: dict[int, Creature] = {}  # id: Creature

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

    def perform_step(self):
        for id, creature in self.creatures.items():
            pos = creature.get_position()
            next_dir = creature.next_direction()
            next_pos = pos + next_dir.position
            if (
                next_pos.x < 0
                or next_pos.x >= self.grid_size
                or next_pos.y < 0
                or next_pos.y >= self.grid_size
            ):
                continue
            if self.grid[next_pos.x][next_pos.y]:
                continue

            self.grid[pos.x][pos.y] = None
            self.grid[next_pos.x][next_pos.y] = creature.id
            creature.set_position(next_pos)
