import random

from PyQt6.QtWidgets import QHBoxLayout, QMainWindow, QPushButton, QWidget

from simulator.conversion_algorithms import linear
from simulator.creature import Creature
from simulator.evaluation_algorithms import sigmoid
from simulator.exceptions import PositionOccupiedError
from simulator.position import Position
from simulator.world import World
from ui.world import WorldWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Evolution Simulator")
        self.setMinimumSize(800, 600)

        grid_size = 10
        self.init_world(grid_size)
        self.world_widget = WorldWidget(self.world)
        self.setCentralWidget(self.world_widget)

        button = QPushButton("Perform step")
        button.clicked.connect(self.button_clicked)

        layout = QHBoxLayout()
        layout.addWidget(self.world_widget)
        layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def init_world(self, grid_size: int):
        self.world = World(grid_size)
        count = 0
        num_creatures = 10
        while count < num_creatures:
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
        self.world_widget.update_grid()
        print(f"World state after step:\n{self.world}")
