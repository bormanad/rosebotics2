"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def run_test_color_sensor():
    """ Tests the  color_sensor  of the Snatch3rRobot. """
    robot = rb.Snatch3rRobot()

    print()
    print("Testing the  color_sensor  of the robot.")
    print("Repeatedly move the robot to different surfaces.")
    print("Press Control-C when you are ready to stop testing.")
    time.sleep(1)
    count = 1
    while True:
        print("{:4}.".format(count),
              "Color sensor value/color/intensity is: ",
              "{:3} {:3} {:3}".format(robot.color_sensor.get_value()[0],
                                      robot.color_sensor.get_value()[1],
                                      robot.color_sensor.get_value()[2]),
              "{:4}".format(robot.color_sensor.get_color()),
              "{:4}".format(robot.color_sensor.get_reflected_intensity()))
        time.sleep(0.5)
        count = count + 1


def run_test_wait_until_intensity_is_less_than():

    robot = rb.Snatch3rRobot()
    print()
    print("Testing the function on different colors")
    print("Let the robot go over different colors")
    print("Stops Test when threshold is reached")

    robot.color_sensor.wait_until_intensity_is_less_than(85)
    print('done')


def run_test_wait_until_intensity_is_greater_than():

    robot = rb.Snatch3rRobot()
    print()
    print("Testing the function on different colors")
    print("Let the robot go over different colors")
    print("Stops Test when threshold is reached")

    robot.color_sensor.wait_until_intensity_is_greater_than(85)
    print('Done')


def run_test_wait_until_color_is():

    robot = rb.Snatch3rRobot()
    print()
    print('Testing the function on different colors')
    print('Let the robot go over different colors')
    print('Stops the test when the color is detected.')

    robot.color_sensor.wait_until_color_is(5)
    print('Done')


def run_test_wait_until_color_is_one_of():
    robot = rb.Snatch3rRobot()
    print()
    print('Testing the function on different colors')
    print('Let the robot go over different colors')
    print('Stops the test when the color is detected')

    robot.color_sensor.wait_until_color_is_one_of([3, 4, 5])
    print('Done')

def main():

    #run_test_color_sensor()
    #run_test_wait_until_intensity_is_less_than()
    #run_test_wait_until_intensity_is_greater_than()
    #run_test_wait_until_color_is()
    #run_test_wait_until_color_is_one_of()

    """ Runs YOUR specific part of the project """


main()
