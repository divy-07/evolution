import random

from PyQt6.QtWidgets import QMainWindow, QPushButton

from simulation.conversion_algorithms import linear
from simulation.creature import Creature
from simulation.evaluation_algorithms import sigmoid
from simulation.exceptions import PositionOccupiedError
from simulation.position import Position
from simulation.world import World


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Evolution Simulator")
        self.setMinimumSize(800, 600)

        button = QPushButton("Click me!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

        self.init_world(10)

    def init_world(self, grid_size: int):
        self.world = World(grid_size)
        count = 0
        while count < 10:
            c = Creature(sigmoid, linear)
            c.set_params([random.randint(-10, 10) for _ in range(10)])
            pos = Position(
                random.randint(0, grid_size - 1),
                random.randint(0, grid_size - 1),
            )
            c.set_position(pos)
            try:
                self.world.add_creature(c)
            except PositionOccupiedError:
                pass
            count += 1
        print(f"Initial world state:\n{self.world}")

    def button_clicked(self):
        self.world.perform_step()
        print(f"World state after step:\n{self.world}")
