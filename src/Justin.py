"""
  Capstone Project.  Code written by JUSTIN OGASAWARA.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time
import ev3dev.ev3 as ev3

def main():
    """ Runs YOUR specific part of the project """
    #run_test_move_for_seconds()
    run_test_go_straight_inches()
    #run_test_spin_in_place_degrees()
    #run_test_turn_degrees()
    run_test_infared_sensor()

def run_test_move_for_seconds():

    print()
    print('Testing move_for_seconds function')
    print('---------------------------------')
    print('Expects to run for 5 seconds')

    robot = rb.Snatch3rRobot()
    robot.drive_system.move_for_seconds(5, 20, 20)

    print('Ran for:', time.time(), 's')

def run_test_go_straight_inches():

    print()
    print('Testing go_straight_inches')
    print('--------------------------')
    print('Expected to move 10 inches')

    robot = rb.Snatch3rRobot()
    robot.drive_system.go_straight_inches(10, 100)


    print('Degrees the wheels turned:', robot.drive_system.right_wheel.get_degrees_spun())

def run_test_spin_in_place_degrees():

    print()
    print('Testing spin_in_place_degrees function')
    print('---------------------')
    print('Expected to spin 3600 degrees')

    robot = rb.Snatch3rRobot()
    robot.drive_system.spin_in_place_degrees(360, 100)

    print('Degrees the wheels turned:', robot.drive_system.left_wheel.get_degrees_spun())

def run_test_turn_degrees():

    print()
    print('Testing turn_degrees function')
    print('-----------------------------')
    print('Expected to make a 360 degree turn')


    robot = rb.Snatch3rRobot()
    robot.drive_system.turn_degrees(90, 100)

    print('Degrees the wheels turned:', robot.drive_system.right_wheel.get_degrees_spun())


def run_test_infared_sensor():

    print()
    print('Testing infared_sensor function')
    print('-------------------------------')
    print('Should beep if an object is within 9 inches')

    robot = rb.Snatch3rRobot()
    print('robot')
    while True:
        print('in')
        distance = robot.proximity_sensor.get_distance_to_nearest_object_in_inches()
        print(distance)
        if int(distance) <= 15 and int(distance) >= 9:
            ev3.Sound.beep().wait()








main()
