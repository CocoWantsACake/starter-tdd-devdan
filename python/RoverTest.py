import pytest
from prod_code import Direction
from prod_code import Rover

# marsMap = MarsMap(100, 100)

def test_faces_north_on_landing():
    rover = Rover()
    assert rover.direction == Direction.NORTH

def test_rover_moves_forward_ten_times():
    rover = Rover(50, 50)
    for i in range(10):
        rover.moveForward()

    assert rover.xPos == 50
    assert rover.yPos == 40

def test_rover_moves_forward_east_direction_fifteen_times():
    rover = Rover(50, 50)
    for i in range(10):
        rover.moveForward()

    assert rover.xPos == 50
    assert rover.yPos == 40







"""
def moving_forward_10_times():
    rover = Rover(50, 50)
    rover.forward()

    xPos = rover.currCell.xPos
    yPos = rover.currCell.yPos

    assert xPos == 50
    assert yPos == 40
"""