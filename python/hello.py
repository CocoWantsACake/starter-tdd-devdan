from enum import Enum

class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4

class MarsMap:
    xLength = None
    yLength = None
    marsMap = None

    def __init__(self, xLength, yLength):
        self.xLength = xLength
        self.yLength = yLength
        self.marsMap = [[Cell(i, j) for j in range(yLength)] for i in range(xLength)]

class Cell:
    cellType = None
    xPos = None
    yPos = None

    def __init__(self, xPos, yPos, cellType="flat"):
        self.xPos = xPos
        self.yPos = yPos
        self.cellType = cellType

    def isObstacle(self):
        return self.cellType in ["mountain"]


class Rover:
    direction = None
    initCell = None
    currCell = None
    marsMap = None

    def __init__(self, marsMap, xPos, yPos):
        self.marsMap = marsMap
        self.direction = Direction.NORTH

        start_cell = marsMap.marsMap[xPos][yPos]

        self.initCell = start_cell
        self.currCell = start_cell

    def forward(self):
        if self.direction is Direction.NORTH:
            pass

        if self.direction is Direction.SOUTH:
            pass

        if self.direction is Direction.EAST:
            pass

        if self.direction is Direction.WEST:
            pass

    def backward(self):
        self.turnLeft()
        self.turnLeft()
        self.forward()

    def turnLeft(self):
        pass

    def turnRight(self):
        pass

    def isThereObstacle(self):
        pass


