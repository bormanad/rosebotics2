"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    run_test_createPolygon()
    run_test_findColor()
    run_test_followBlackLine()



def run_test_createPolygon():
    print()
    print("Testng the createPolgyon method for the robot")
    print("It will create a pentagon")
    createPolygon(5)

def run_test_followBlackLine():
    print()
    print("Testing the followBlackLine method")
    followBlackLine()

def run_test_findColor():
    print()
    print("Testing the findColor method")
    findColor(5)


def createPolygon(n):
    robot = rb.Snatch3rRobot()
    """ Calculates the measure of each interior angle. """
    angle_moved = 360/n
    inches = 10
    for k in range(n):
        robot.drive_system.go_straight_inches(inches,100)
        robot.drive_system.spin_in_place_degrees(angle_moved,100)

def followBlackLine():
    robot = rb.Snatch3rRobot()
    degree = 0
    while True:
        if robot.color_sensor.get_color() == 1:
            robot.drive_system.move_for_seconds(100,100)
        else:
            degree = degree + 15
            robot.drive_system.spin_in_place_degrees(degree,100)



def findColor(color):
    robot = rb.Snatch3rRobot()
    while True:
        robot.drive_system.start_moving(100,100)
        if robot.color_sensor.get_color() == color:
            robot.drive_system.stop_moving(stop_action=StopAction.BRAKE)





main()
