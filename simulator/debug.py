import random

from simulator.conversion_algorithms import linear
from simulator.creature import Creature
from simulator.evaluation_algorithms import sigmoid
from simulator.exceptions import PositionOccupiedError
from simulator.position import Position
from simulator.world import World

grid_size = 10
w = World(grid_size)
count = 0
num_creatures = 10
while count < num_creatures:
    c = Creature(sigmoid, linear)
    c.set_params([random.randint(-10, 10) for _ in range(10)])
    pos = Position(
        random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
    )
    c.set_position(pos)
    try:
        w.add_creature(c)
    except PositionOccupiedError:
        pass
    count += 1
print(w)
w.perform_step()
print(w)
