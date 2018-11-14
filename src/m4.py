"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    #run_test_createPolygon()
    run_test_findColor()
    #run_test_followBlackLine()



def run_test_createPolygon():
    print()
    print("Testng the createPolgyon method for the robot")
    print("It will create a pentagon")
    createPolygon(5)
    print('hi')

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
    i = 0
    while i != n:
        robot.drive_system.go_straight_inches(inches, 100)
        print('hi')
        robot.drive_system.left_wheel.reset_degrees_spun()
        robot.drive_system.spin_in_place_degrees(angle_moved, 100)
        print('bye')
        i = i + 1



    print('dont')
def followBlackLine():
    robot = rb.Snatch3rRobot()
    while True:
        if robot.color_sensor.get_color() == 1:
            robot.drive_system.start_moving(30,30)
        else:
            robot.drive_system.stop_moving()
            robot.drive_system.left_wheel.reset_degrees_spun()
            robot.drive_system.spin_in_place_degrees(1,30)



def findColor(color):
    robot = rb.Snatch3rRobot()
    while True:
        robot.drive_system.start_moving(50 ,50)
        if robot.color_sensor.get_color() == color:
            robot.drive_system.stop_moving()
            break






main()
