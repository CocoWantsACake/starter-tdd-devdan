from enum import Enum

class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4

class Rover:
    xPos = None
    yPos = None
    direction = None

    def __init__(self, x=0, y=0):
        self.xPos = x
        self.yPos = y
        self.direction = Direction.NORTH

    def moveForward(self):
        if self.direction is Direction.NORTH:
            self.yPos -= 1

        if self.direction is Direction.SOUTH:
            self.yPos += 1

        if self.direction is Direction.EAST:
            self.xPos += 1

        if self.direction is Direction.WEST:
            self.xPos -= 1

