from PyQt6.QtWidgets import QGridLayout, QWidget

from simulator.world import World


class WorldWidget(QWidget):
    def __init__(self, world: World):
        super().__init__()

        self.world = world

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.init_grid()

    def init_grid(self):
        for i in range(self.world.grid_size):
            for j in range(self.world.grid_size):
                cell = QWidget()
                self.layout.addWidget(cell, i, j)
                if self.world.grid[i][j]:
                    cell.setStyleSheet("background-color: red")
                else:
                    cell.setStyleSheet("background-color: yellow")

    def update_grid(self):
        for i in range(self.world.grid_size):
            for j in range(self.world.grid_size):
                cell = self.layout.itemAtPosition(i, j).widget()
                if self.world.grid[i][j]:
                    cell.setStyleSheet("background-color: red")
                else:
                    cell.setStyleSheet("background-color: yellow")
