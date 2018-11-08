"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and JUSTIN OGASAWARA.
"""
# ------------------------------------------------------------------------------
# DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.  Then delete this DONE.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# DONE: 2. With your instructor, review the "big picture" of laptop-robot
# DONE:    communication, per the comment in mqtt_sender.py.
# DONE:    Once you understand the "big picture", delete this DONE.
# ------------------------------------------------------------------------------

import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():
    robot = rb.Snatch3rRobot()
    # --------------------------------------------------------------------------
    # DONE: 3. Construct a Snatch3rRobot.  Test.  When OK, delete this DONE.
    # --------------------------------------------------------------------------
    rc = RemoteControlEtc(robot)
    client = com.MqttClient(rc)
    client.connect_to_pc()
    # --------------------------------------------------------------------------
    # DONE: 4. Add code that constructs a   com.MqttClient   that will
    # DONE:    be used to receive commands sent by the laptop.
    # DONE:    Connect it to this robot.  Test.  When OK, delete this DONE.
    # --------------------------------------------------------------------------


    # --------------------------------------------------------------------------
    # DONE: 5. Add a class for your "delegate" object that will handle messages
    # DONE:    sent from the laptop.  Construct an instance of the class and
    # DONE:    pass it to the MqttClient constructor above.  Augment the class
    # DONE:    as needed for that, and also to handle the go_forward message.
    # DONE:    Test by PRINTING, then with robot.  When OK, delete this DONE.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # DONE: 6. With your instructor, discuss why the following WHILE loop,
    # DONE:    that appears to do nothing, is necessary.
    # DONE:    When you understand this, delete this DONE.
    # --------------------------------------------------------------------------
    while True:
        if robot.beacon_button_sensor.is_top_red_button_pressed():
            ev3.Sound.beep().wait()
        elif robot.beacon_button_sensor.is_top_blue_button_pressed():
            ev3.Sound.speak('Hello. How are you?').wait()
        # ----------------------------------------------------------------------
        # DONE: 7. Add code that makes the robot beep if the top-red button
        # DONE:    on the Beacon is pressed.  Add code that makes the robot
        # DONE:    speak "Hello. How are you?" if the top-blue button on the
        # DONE:    Beacon is pressed.  Test.  When done, delete this DONE.
        # ----------------------------------------------------------------------
        time.sleep(0.01)  # For the delegate to do its work

class RemoteControlEtc(object):

    def __init__(self, robot):
        """
        Stores the robot.
            :type robot: rb.Snatch3rRobot
        """
        self.robot = robot

    def go_forward(self, speed_string):
        print('In Go_Forward')
        speed = int(speed_string)
        self.robot.drive_system.start_moving(speed, speed)

main()