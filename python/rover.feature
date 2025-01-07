Scenario: Landing
        Given the rover lands
        Then it is always facing north

Scenario: Moving the rover forward 10 times
        Given a rover at coordinate (50,50)
        When the rover moves 10 times
        Then the rover arrives at (50,40)

Scenario: Moving the rover in the EAST direction 15 times
        Given a rover at coordinate (60,60)
        When the rover orients itself to east
        And the rover moves 15 times
        Then the rover arrives at (75,60)



Feature: Moving the Rover on the terrain
  As a Rover controller
  I want to be able to move the Rover on the terrain
  In order to explore the area while avoiding obstacles

  Background:
    Given a 100x100 terrain
    And a Rover positioned at (0,0) facing North
    And 5 obstacles randomly placed on the terrain

  Scenario: Simple forward movement of the Rover
    When I move the Rover forward 10 meters
    Then the Rover's position should be (0,10)
    And no obstacle is hit
    And the command is recorded in history

  Scenario: Rover rotation
    When I turn the Rover left
    Then the Rover should be facing West
    When I turn the Rover right
    Then the Rover should be facing North

  Scenario: Obstacle detection
    Given an obstacle at position (0,5) with a radius of 1 meter
    When I move the Rover forward 10 meters
    Then an obstacle is detected
    And the command is cancelled
    And the command is recorded in history

  Scenario Outline: Multiple Rover movements
    When I <action> the Rover by <distance> meters
    Then the Rover's position should be <final_position>
    And the command is recorded in history

    Examples:
      | action  | distance | final_position |
      | advance | 5       | (0,5)          |
      | reverse | 3       | (0,-3)         |

  Scenario: Command history
    When I move the Rover forward 5 meters
    And I turn the Rover left
    And I move the Rover backward 3 meters
    Then the history should contain 3 commands