import random

from conversion_algorithms import linear
from creature import Creature
from evaluation_algorithms import sigmoid
from exceptions import PositionOccupiedError
from position import Direction, Position
from world import World

grid_size = 10
w = World(grid_size)
count = 0
while count < 10:
    c = Creature(sigmoid, linear)
    c.set_params([random.randint(-10, 10) for _ in range(10)])
    pos = Position(random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
    c.set_position(pos)
    try:
        w.add_creature(c)
    except PositionOccupiedError:
        pass
    count += 1
print(w)
w.perform_step()
print(w)
