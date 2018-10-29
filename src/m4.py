"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    run_test_createPolygon()


def run_test_createPolygon():
    print()
    print("Testng the createPolgyon method for the robot")
    print("It will create a pentagon")
    createPolygon(5)


def createPolygon(n):
    robot = rb.Snatch3rRobot()
    """ Calculates the measure of each interior angle. """
    angle_moved = 360/n
    inches = 10
    for k in range(n):
        robot.drive_system.go_straight_inches(inches,100,stop_action=StopAction.BRAKE)
        robot.drive_system.spin_in_place_degrees(angle_moved,100,stop_action=StopAction.BRAKE)

def followBlackLine():



def findColor(color):
    robot = rb.Snatch3rRobot()
    while True:
        if robot.color_sensor.get_reflected_intensity() == color:
            robot.drive_system.stop_moving(stop_action=StopAction.BRAKE)
        else:
            robot.drive_system.start_moving(100,100)




main()
