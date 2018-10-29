"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    run_test_touch_sensor()
    run_test_createPolygon()

def run_test_touch_sensor():
    """ Tests the  touch_sensor  of the Snatch3rRobot. """
    robot = rb.Snatch3rRobot()

    print()
    print("Testing the  touch_sensor  of the robot.")
    print("Repeatedly press and release the touch sensor.")
    print("Press Control-C when you are ready to stop testing.")
    time.sleep(1)
    count = 1
    while True:
        print("{:4}.".format(count),
              "Touch sensor value is: ", robot.touch_sensor.get_value())
        time.sleep(0.5)
        count = count + 1

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
        robot.DriveSystem.go_straight_inches(inches,100,stop_action=StopAction.BRAKE)
        robot.DriveSystem.spin_in_place_degrees(angle_moved,100,stop_action=StopAction.BRAKE)

def





main()
