from enum import Enum
from random import randint

class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4


class Cell:
    cellType = None
    xPos = None
    yPos = None

    def __init__(self, xPos, yPos, cellType="flat"):
        self.xPos = xPos
        self.yPos = yPos
        self.cellType = cellType

    def isObstacle(self):
        return self.cellType in ["obstacle"]


class MarsMap:
    xLength = None
    yLength = None
    marsMap = None

    def __init__(self, xLength, yLength):
        self.xLength = xLength
        self.yLength = yLength
        self.marsMap = [[Cell(i, j) for j in range(yLength)] for i in range(xLength)]

        for i in range(5):
            xPosObst = randint(0, xLength-1)
            yPosObst = randint(0, yLength-1)
            self.marsMap[xPosObst][yPosObst].cellType = "obstacle"





class Rover:
    xPos = None
    yPos = None
    direction = None
    history = []
    obstacle_stopped = False
    marsMap = None

    def __init__(self, marsMap, x=0, y=0):
        self.marsMap = marsMap
        self.xPos = x
        self.yPos = y
        self.direction = Direction.NORTH

    def moveForward(self):
        if self.direction is Direction.NORTH:
            self.yPos += 1

        if self.direction is Direction.SOUTH:
            self.yPos -= 1

        if self.direction is Direction.EAST:
            self.xPos += 1

        if self.direction is Direction.WEST:
            self.xPos -= 1

        self.history.append(self.direction)

    def turnLeft(self):
        pass

    def turnRight(self):
        pass

