import random

from creature import Creature
from exceptions import PositionOccupiedError
from position import Position
from world import World

grid_size = 10
w = World(grid_size)
count = 0
while count < 10:
    c = Creature()
    pos = Position(random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
    c.set_position(pos)
    try:
        w.add_creature(c)
    except PositionOccupiedError:
        pass
    count += 1
print(w)
