"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Meghna Allamudi.
"""


# ------------------------------------------------------------------------------
# TODO: 2. With your instructor, review the "big picture" of laptop-robot
# TODO:    communication, per the comment in mqtt_sender.py.
# TODO:    Once you understand the "big picture", delete this TODO.
# ------------------------------------------------------------------------------

import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():

    print('in main')
    robot = rb.Snatch3rRobot()
    rc = RemoteControlEtc(robot)
    client = com.MqttClient(rc)
    client.connect_to_pc()


    # --------------------------------------------------------------------------
    # TODO: 3. Construct a Snatch3rRobot.  Test.  When OK, delete this TODO.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # TODO: 4. Add code that constructs a   com.MqttClient   that will
    # TODO:    be used to receive commands sent by the laptop.
    # TODO:    Connect it to this robot.  Test.  When OK, delete this TODO.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # TODO: 5. Add a class for your "delegate" object that will handle messages
    # TODO:    sent from the laptop.  Construct an instance of the class and
    # TODO:    pass it to the MqttClient constructor above.  Augment the class
    # TODO:    as needed for that, and also to handle the go_forward message.
    # TODO:    Test by PRINTING, then with robot.  When OK, delete this TODO.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # TODO: 6. With your instructor, discuss why the following WHILE loop,
    # TODO:    that appears to do nothing, is necessary.
    # TODO:    When you understand this, delete this TODO.
    # --------------------------------------------------------------------------
    #while True:
        #if robot.beacon_button_sensor.is_top_red_button_pressed():
           # ev3.Sound.beep().wait()
       # if robot.beacon_button_sensor.is_bottom_blue_button_pressed():
           # ev3.Sound.speak('Hello. How are you?').wait()
        # ----------------------------------------------------------------------
        # TODO: 7. Add code that makes the robot beep if the top-red button
        # TODO:    on the Beacon is pressed.  Add code that makes the robot
        # TODO:    speak "Hello. How are you?" if the top-blue button on the
        # TODO:    Beacon is pressed.  Test.  When done, delete this TODO.
        # ----------------------------------------------------------------------
        #time.sleep(0.01)  # For the delegate to do its work
class RemoteControlEtc(object):
    def __init__(self,robot):
        """
            Stores robot
            :type robot:rb.Snatch3rRobot
        """
        self.robot = robot

    def get_color(self,color_number):
        """Makes the robot stop at color given """
        print('Stop moving robot at', color_number)
        color_int = int(color_number)
        self.robot.drive_system.start_moving(50 ,50)
        while True:
            if self.robot.color_sensor.get_color() == color_int:
                self.robot.drive_system.start_moving(0,0)
                break
        camera = rb.Camera()
        blob = camera.get_biggest_blob()
        while True:
            if blob.get_area() >= 600:
                ev3.Sound.speak('Object approaching').wait()
                blob = camera.get_biggest_blob()







main()