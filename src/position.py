class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Position({self.x}, {self.y})"

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)


class Direction:
    def __init__(self, name: str, position: Position):
        self.name = name
        self.position = position

    def __repr__(self):
        return f"{self.name}"


LEFT = Direction("LEFT", Position(-1, 0))
RIGHT = Direction("RIGHT", Position(1, 0))
UP = Direction("UP", Position(0, -1))
DOWN = Direction("DOWN", Position(0, 1))

ALL_DIRECTIONS = [LEFT, RIGHT, UP, DOWN]
