"""
Functions for TURNING the robot LEFT and RIGHT.
Authors: David Fisher, David Mutchler and James (Bo) Geyer.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implment turn_left_seconds, then the relevant part of the test function.
#          Test and correct as needed.
#   Then repeat for turn_left_by_time.
#   Then repeat for turn_left_by_encoders.
#   Then repeat for the turn_right functions.
import math
import ev3dev.ev3 as ev3
import time

left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
right_motor = ev3.LargeMotor(ev3.OUTPUT_C)

def test_turn_left_turn_right():
    time_s = 1
    while time_s != 0:
        speed = int(input("Enter a speed for the left turn (0 to 100): ")) * 8
        stop = str(input('Enter stop actions: brake, coast, or hold?'))
        time_s = int(input("Enter a time to drive (seconds): "))
        turn_left_seconds(time_s, speed, stop)
    degrees = 1
    while degrees != 0:
        speed = int(input("Enter a speed for the left turn (0 to 100): ")) * 8
        stop = str(input('Enter stop actions: brake, coast, or hold?'))
        degrees = int(input("Enter degrees to turn through "))
        if degrees == 0:
            break
        turn_left_by_time(degrees, speed, stop)
    degrees = 1
    while degrees != 0:
        speed = int(input("Enter a speed for the left turn (0 to 100): ")) * 8
        degrees = int(input("Enter degrees to turn through "))
        if degrees == 0:
            break
        turn_left_by_encoders(degrees, speed)
    time_s = 1
    while time_s != 0:
        speed = int(input("Enter a speed for the left turn (0 to 100): ")) * 8
        stop = str(input('Enter stop actions: brake, coast, or hold?'))
        time_s = int(input("Enter a time to drive (seconds): "))
        turn_right_seconds(time_s, speed, stop)





    """
    Tests the turn_left and turn_right functions, as follows:
      1. Repeatedly:
          -- Prompts for and gets input from the console for:
             -- Seconds to travel
                  -- If this is 0, BREAK out of the loop.
             -- Speed at which to travel (-100 to 100)
             -- Stop action ("brake", "coast" or "hold")
          -- Makes the robot run per the above.
      2. Same as #1, but gets degrees and runs turn_left_by_time.
      3. Same as #2, but runs turn_left_by_encoders.
      4. Same as #1, 2, 3, but tests the turn_right functions.
    """


def turn_left_seconds(time_s, speed, stop):
    right_motor.run_forever(speed_sp=speed)
    time.sleep(time_s)
    right_motor.stop(stop_action=stop)
    """
    Makes the robot turn in place left for the given number of seconds at the given speed,
    where speed is between -100 (full speed turn_right) and 100 (full speed turn_left).
    Uses the given stop_action.
    """


def turn_left_by_time(degrees, speed, stop):
    tim = (degrees/0.23149)/speed
    right_motor.run_forever(speed_sp=speed)
    left_motor.run_forever(speed_sp=-speed)
    time.sleep(tim)
    right_motor.stop(stop_action=stop)
    left_motor.stop(stop_action=stop)

    """
    Makes the robot turn in place left the given number of degrees at the given speed,
    where speed is between -100 (full speed turn_right) and 100 (full speed turn_left).
    Uses the algorithm:
      0. Compute the number of seconds to move to achieve the desired distance.
      1. Start moving.
      2. Sleep for the computed number of seconds.
      3. Stop moving.
    """


def turn_left_by_encoders(degrees, speed):
    dis = (degrees/0.23149)
    right_motor.run_to_rel_pos(position_sp=dis, speed_sp=speed)
    left_motor.run_to_rel_pos(position_sp=-dis, speed_sp=speed)
    right_motor.wait_while(ev3.Motor.STATE_RUNNING)
    left_motor.wait_while(ev3.Motor.STATE_RUNNING)
    right_motor.stop()
    left_motor.stop()

    """
    Makes the robot turn in place left the given number of degrees at the given speed,
    where speed is between -100 (full speed turn_right) and 100 (full speed turn_left).
    Uses the algorithm:
      1. Compute the number of degrees the wheels should turn to achieve the desired distance.
      2. Move until the computed number of degrees is reached.
    """


def turn_right_seconds(seconds, speed, stop):
    speed = -speed
    turn_left_seconds(seconds, speed, stop)


def turn_right_by_time(degrees, speed, stop):
    speed = -speed
    turn_left_by_time(degrees, speed, stop)



def turn_right_by_encoders(degrees, speed, stop_action):
    speed = -speed
    turn_left_by_encoders(degrees, speed)



test_turn_left_turn_right()