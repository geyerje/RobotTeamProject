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
import fetch


class Snatch3r(object):
    """Commands for the Snatch3r robot that might be useful in many different programs."""
    
    # TODO: Implement the Snatch3r class as needed when working the sandox exercises
    # (and delete these comments)

    def __init__(self):
        self.color_sensor = ev3.ColorSensor()
        self.pixy = ev3.Sensor(driver_name="pixy-lego")
        self.ir_sensor = ev3.InfraredSensor()
        self.left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        self.right_motor = ev3.LargeMotor(ev3.OUTPUT_D)
        self.left_motor.reset()
        self.right_motor.reset()
        self.arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)
        self.mqtt = None
        self.touchyboy = ev3.TouchSensor(ev3.INPUT_1)
        self.count = 0
        self.positions = [self.left_motor.position, self.right_motor.position]


        assert self.left_motor.connected
        assert self.right_motor.connected
        assert self.arm_motor.connected
        assert self.color_sensor
        assert self.pixy
        assert self.ir_sensor

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
        self.positions.extend((self.left_motor.position, self.right_motor.position))

    def turn_left_by_encoders(self, degrees, speed):
        dis = (degrees / 0.23149)
        self.right_motor.run_to_rel_pos(position_sp=dis, speed_sp=speed)
        self.left_motor.run_to_rel_pos(position_sp=-dis, speed_sp=speed)
        self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)
        self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)
        self.right_motor.stop()
        self.left_motor.stop()

    def turn_right_by_encoders(self, degrees, speed):
        dis = (degrees / 0.23149)
        self.right_motor.run_to_rel_pos(position_sp=-dis, speed_sp=speed)
        self.left_motor.run_to_rel_pos(position_sp=dis, speed_sp=speed)
        self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)
        self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)
        self.right_motor.stop()
        self.left_motor.stop()

    def turn_left(self, speed):
        self.right_motor.run_forever(speed_sp=speed)
        self.left_motor.run_forever(speed_sp=-speed)

    def turn_right(self, speed):
        self.right_motor.run_forever(speed_sp=-speed)
        self.left_motor.run_forever(speed_sp=speed)

    def arm_up(self):
        while True:
            self.arm_motor.run_forever(speed_sp=400)
            time.sleep(0.05)
            if self.touchyboy.is_pressed:
                break
        self.arm_motor.stop()

    def arm_close(self):
        self.arm_motor.run_forever(speed_sp=400)
        time.sleep(5)
        self.arm_motor.stop()

    def arm_open(self):
        self.arm_motor.run_forever(speed_sp=-400)
        time.sleep(5)
        self.arm_motor.stop()

    def arm_down(self):
        self.arm_motor.run_forever(speed_sp=-400)
        time.sleep(14.5)
        self.arm_motor.stop()

    def printer(self, value):
        print(value)


    #Stops moving the robot when it hits a black line
    def move2(self, left_speed, right_speed):
        # self.right_motor.run_forever(speed_sp=right_speed)
        # self.left_motor.run_forever(speed_sp=left_speed)
        # if self.color_sensor.color == 1:
        #     self.left_motor.stop()
        #     self.right_motor.stop()
        #     time.sleep(0.05)
        print('1')
        print(self.color_sensor.reflected_light_intensity)
        print(self.color_sensor.color)

    #makes the robot print the current location of SIG1 object

    #finds an object trained to pixy 1 and centers the robot on it
    def re_center(self):
            while self.pixy.value(1) < 170:
                self.turn_left(100)
            self.stop_robot()
            time.sleep(0.05)

            while self.pixy.value(1) > 190:
                self.turn_right(100)
            self.stop_robot()
            time.sleep(0.05)
    def re_centerryan(self):
            while self.pixy.value(1) == 0:
                time.sleep(.1)
                print('no object')

            while self.pixy.value(1) < 139:
                if self.color_sensor.color == 1:
                    break
                self.turn_left(100)
            self.stop_robot()
            time.sleep(0.05)

            while self.pixy.value(1) > 144:
                if self.color_sensor.color == 1:
                    break
                self.turn_right(100)
            self.stop_robot()
            time.sleep(0.05)

    def abs_move(self, pos_l, pos_r):
        self.left_motor.run_to_abs_pos(position_sp=pos_l, speed_sp=300)
        self.right_motor.run_to_abs_pos(position_sp=pos_r, speed_sp=300)
        self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)
        self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)
        self.right_motor.stop()
        self.left_motor.stop()
        time.sleep(0.05)


    def resetter(self):
        while True:
            if self.touchyboy.is_pressed:
                self.count = 0
                break

    def move3(self, left_speed, right_speed, value):
        if value == 0:
            if self.count >=3:
                ev3.Sound.speak('Press red button to reset')
                self.mqtt.send_message("printer", ["PRESS RED BUTTON TO RESET"])
                while True:
                    self.resetter()
                    return
            elif self.color_sensor.reflected_light_intensity <=20:
                self.right_motor.run_timed(speed_sp=-800, time_sp=100)
                self.left_motor.run_timed(speed_sp=-800, time_sp=100)
                ev3.Sound.speak('LOOK OUT!')
                self.count += 1
                self.mqtt.send_message("printer", ["LOOK OUT FOR THE LINE"])
                time.sleep(2)
                return
            else:
                self.right_motor.run_timed(speed_sp=right_speed, time_sp = 50)
                self.left_motor.run_timed(speed_sp=left_speed, time_sp = 50)
        else:
            if self.count >=3:
                ev3.Sound.speak('Press red button to reset')
                self.mqtt.send_message("printer", ["PRESS RED BUTTON TO RESET"])
                while True:
                    self.resetter()
                    return
            elif self.color_sensor.reflected_light_intensity <=20:
                self.right_motor.run_timed(speed_sp=-800, time_sp=100)
                self.left_motor.run_timed(speed_sp=-800, time_sp=100)
                ev3.Sound.speak('LOOK OUT!')
                self.count += 1
                self.mqtt.send_message("printer", ["LOOK OUT FOR THE LINE"])
                time.sleep(2)
                return
            else:
                self.right_motor.run_forever(speed_sp=right_speed)
                self.left_motor.run_forever(speed_sp=left_speed)
                if self.color_sensor.reflected_light_intensity <= 20:
                    self.right_motor.run_timed(speed_sp=-800, time_sp=100)
                    self.left_motor.run_timed(speed_sp=-800, time_sp=100)
                    ev3.Sound.speak('LOOK OUT!')
                    self.count += 1
                    self.mqtt.send_message("printer", ["LOOK OUT FOR THE LINE"])
                    time.sleep(2)
                    return


# Andrew Notes: Need to make MQTT 2 way, add something to TKINTER, reenable touchyboy,
    # Ryans code
    def ryan_start(self, deliver):

        self.arm_motor.run_forever(speed_sp=400)
        time.sleep(5)
        self.arm_motor.stop()

        self.re_centerryan()
        time1 = time.time()
        while self.color_sensor.color != 1:
            self.move(600, 600)
            if self.color_sensor.color == 1:
                break
        self.stop_robot()
        time2 = time.time()
        if deliver == 1:
            self.arm_motor.run_forever(speed_sp=-400)
            time.sleep(5)
            self.arm_motor.stop()
            self.mqtt.send_message('reach')

        self.move(-600, -600)
        time.sleep(time2 - time1)
        self.stop_robot()
        if deliver == 0:
            self.arm_motor.run_forever(speed_sp=-400)
            time.sleep(5)
            self.arm_motor.stop()
            self.mqtt.send_message('reach2')

    def bo_project(self):
        fetch.main()
        self.mqtt.send_message('respond')

    #####################
    #  David's Project  #
    #####################

    def watch_move(self, left_speed, right_speed):
        # while self.color_sensor.color != 1:
        while self.color_sensor.color != 1:
            self.right_motor.run_forever(speed_sp=right_speed)
            self.left_motor.run_forever(speed_sp=left_speed)
            # time.sleep(0.05)
        self.hard_stop()
        ev3.Sound.speak('WALL')
        self.right_motor.run_timed(speed_sp=-400, time_sp=300)
        self.left_motor.run_timed(speed_sp=-400, time_sp=300)
        # if self.color_sensor.color == 0:
        # if self.color_sensor.reflected_light_intensity <= 20:

    def watch_turn(self, left_speed, right_speed):
        self.right_motor.run_timed(speed_sp=right_speed, time_sp=1300)
        self.left_motor.run_timed(speed_sp=left_speed, time_sp=1300)

    def hard_stop(self, stop_action='brake'):
        self.left_motor.stop(stop_action=stop_action)
        self.right_motor.stop(stop_action=stop_action)
        self.arm_motor.stop(stop_action=stop_action)
        time.sleep(0.05)

    def arm_up_maze(self):
        while True:
            self.arm_motor.run_forever(speed_sp=400)
            time.sleep(0.05)
            if self.touchyboy.is_pressed:
                self.mqtt.send_message('end_response')
                break
        self.arm_motor.stop()
        self.mqtt.send_message('end_response')
