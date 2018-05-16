"""
  Library of EV3 robot functions that are useful in many different applications. For example things
  like arm_up, arm_down, driving around, or doing things with the Pixy camera.

  Add commands as needed to support the features you'd like to implement.  For organizational
  purposes try to only write methods into this library that are NOT specific to one tasks, but
  rather methods that would be useful regardless of the activity.  For example, don't make
  a connection to the remote control that sends the arm up if the ir remote control up button
  is pressed.  That's a specific input --> output task.  Maybe some other task would want to use
  the IR remote up button for something different.  Instead just make a method called arm_up that
  could be called.  That way it's a generic action that could be used in any task.
"""

import ev3dev.ev3 as ev3
import math
import time


class Snatch3r(object):
    """Commands for the Snatch3r robot that might be useful in many different programs."""
    
    # TODO: Implement the Snatch3r class as needed when working the sandox exercises
    # (and delete these comments)

    def __init__(self):
        self.cs = ev3.ColorSensor()
        self.left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        self.right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
        self.arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)

        assert self.left_motor.connected
        assert self.right_motor.connected
        assert self.arm_motor.connected

    def move(self, left_speed, right_speed):
        self.right_motor.run_forever(speed_sp=right_speed)
        self.left_motor.run_forever(speed_sp=left_speed)

    def forward(self, inches, speed=100, stop_action='brake'):
        K = 360 / 4.2
        degrees_motor = K * inches
        self.left_motor.run_to_rel_pos(position_sp=degrees_motor, speed_sp=8*speed, stop_action=stop_action)
        self.right_motor.run_to_rel_pos(position_sp=degrees_motor, speed_sp=8 * speed, stop_action=stop_action)
        self.left_motor.wait_while('running')
        self.right_motor.wait_while('running')


    def loop_forever(self):
        while True:
            time.sleep(0.05)

    def stop_robot(self):
        self.left_motor.stop()
        self.right_motor.stop()
        self.arm_motor.stop()
        time.sleep(0.05)

    def turn_left_by_encoders(self, degrees, speed):
        dis = (degrees / 0.23149)
        right_motor.run_to_rel_pos(position_sp=dis, speed_sp=speed)
        left_motor.run_to_rel_pos(position_sp=-dis, speed_sp=speed)
        right_motor.wait_while(ev3.Motor.STATE_RUNNING)
        left_motor.wait_while(ev3.Motor.STATE_RUNNING)
        right_motor.stop()
        left_motor.stop()

    def turn_right_by_encoders(self, degrees, speed):
        dis = (degrees / 0.23149)
        right_motor.run_to_rel_pos(position_sp=-dis, speed_sp=speed)
        left_motor.run_to_rel_pos(position_sp=dis, speed_sp=speed)
        right_motor.wait_while(ev3.Motor.STATE_RUNNING)
        left_motor.wait_while(ev3.Motor.STATE_RUNNING)
        right_motor.stop()
        left_motor.stop()

    def arm_up(self, speed=200):
        while ev3.TouchSensor == 0:
            self.arm_motor.run_forever(speed_sp=speed)
        self.arm_motor.stop()
        time.sleep(0.05)


    def arm_down(self, speed=200):
        self.arm_motor.run_forever(speed_sp=-speed)
        time.sleep(3)
        self.arm_motor.stop()
        time.sleep(0.05)

    def printer(self, value):
        print(value)

    def move2(self, left_speed, right_speed, color):
        self.right_motor.run_forever(speed_sp=right_speed)
        self.left_motor.run_forever(speed_sp=left_speed)
        if self.cs.color is ev3.ColorSensor.COLOR_BLACK:
            self.left_motor.stop()
            self.right_motor.stop()
            time.sleep(0.05)

    # def turn_degrees(self, degrees_to_turn, turn_speed_sp, stop_action = 'brake'):
    #     self.left_motor.run_to_rel_pos(position_sp=degrees_to_turn, speed_sp=8*turn_speed_sp, stop_action=stop_action)
    #     self.right_motor.run_to_rel_pos(position_sp=-degrees_to_turn, speed_sp=8*turn_speed_sp, stop_action=stop_action)
    #     self.left_motor.wait_while('running')
    #     self.right_motor.wait_while('running')

