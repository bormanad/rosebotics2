"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time
import ev3dev.ev3 as ev3
import rosebotics_new as rb



def main():
    """ Runs YOUR specific part of the project """
    run_test_touch_sensor()
    identifySize()

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


def identifySize():
    robot = rb.Snatch3rRobot()
    camera = rb.Camera()
    blob = camera.get_biggest_blob()
    if blob.get_area() >= 600:
        ev3.Sound.beep().wait()









main()
