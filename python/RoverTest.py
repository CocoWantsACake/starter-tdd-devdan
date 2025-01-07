import pytest
from prod_code import Direction
from prod_code import Rover
from prod_code import MarsMap

marsMap = MarsMap(100, 100)

def test_faces_north_on_landing():
    rover = Rover(marsMap)
    assert rover.direction == Direction.NORTH

def simple_forward_movement_of_the_rover():
    marsMap2 = MarsMap(100, 100)
    for i in range(10):
        marsMap2.marsMap[0][i].cellType = None

    rover = Rover(marsMap2)
    for i in range(10):
        rover.moveForward()

    assert rover.xPos == 0
    assert rover.yPos == 10

    assert rover.obstacle_stopped is False
    assert rover.history == [Direction.NORTH for i in range(10)]

def rover_rotation():
    rover = Rover(marsMap)
    rover.turnLeft()
    assert rover.direction == Direction.WEST
    rover.turnRight()
    assert rover.direction == Direction.NORTH




