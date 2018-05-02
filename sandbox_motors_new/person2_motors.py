"""
Functions for SPINNING the robot LEFT and RIGHT.
Authors: David Fisher, David Mutchler and Ryan Antenore.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implment spin_left_seconds, then the relevant part of the test function.
#          Test and correct as needed.
#   Then repeat for spin_left_by_time.
#   Then repeat for spin_left_by_encoders.
#   Then repeat for the spin_right functions.


import ev3dev.ev3 as ev3
import time


def Main():
    spin_left_seconds(5, 500, ev3.Motor.STOP_ACTION_COAST)


def test_spin_left_spin_right():
    """
    Tests the spin_left and spin_right functions, as follows:
      1. Repeatedly:
          -- Prompts for and gets input from the console for:
             -- Seconds to travel
                  -- If this is 0, BREAK out of the loop.
             -- Speed at which to travel (-100 to 100)
             -- Stop action ("brake", "coast" or "hold")
          -- Makes the robot run per the above.
      2. Same as #1, but gets degrees and runs spin_left_by_time.
      3. Same as #2, but runs spin_left_by_encoders.
      4. Same as #1, 2, 3, but tests the spin_right functions.
    """
    time_s = 1  # Any value other than 0.
    while time_s != 0:
        time_s = int(input("Enter seconds to travel left (seconds): "))
        if time_s == 0:
            break
        speed = int(input("Enter a speed for the left turn (-100 - 100): "))
        stop_action = input('enter a stop action: (brake, coast, hold)')
        spin_left_seconds(time_s, speed, stop_action)

    time_s = 1  # Any value other than 0.
    while time_s != 0:
        time_s = int(input("Enter seconds to travel right (seconds): "))
        if time_s == 0:
            break
        speed = int(input("Enter a speed for the right turn (-100 - 100): "))
        stop_action = input('enter a stop action: (brake, coast, hold)')
        spin_right_seconds(time_s, speed, stop_action)

    degrees = 1  # Any value other than 0.
    while degrees != 0:
        degrees = int(input("Enter degrees to spin left: (using time)"))
        if degrees == 0:
            break
        speed = int(input("Enter a speed for left turn by time (-100 - 100): "))
        stop_action = input('enter a stop action: (brake, coast, hold)')
        spin_left_by_time(degrees, speed, stop_action)

    degrees = 1  # Any value other than 0.
    while degrees != 0:
        degrees = int(input("Enter degrees to spin left: (using encoders) "))
        if degrees == 0:
            break
        speed = int(input("Enter a speed for left turn by time (-100 - 100): "))
        stop_action = input('enter a stop action: (brake, coast, hold)')
        spin_left_by_encoders(degrees, speed, stop_action)


def spin_left_seconds(seconds, speed, stop_action):
    """
    Makes the robot spin in place left for the given number of seconds at the given speed,
    where speed is between -100 (full speed spin_right) and 100 (full speed spin_left).
    Uses the given stop_action.
    """
    # Connect two large motors on output ports B and C
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)

    # Check that the motors are actually connected
    assert left_motor.connected
    assert right_motor.connected

    left_motor.run_timed(speed_sp=-speed * 8, time_sp=seconds * 1000, stop_action=stop_action)
    right_motor.run_timed(speed_sp=speed * 8, time_sp=seconds * 1000, stop_action=stop_action)


def spin_left_by_time(degrees, speed, stop_action):
    """
    Makes the robot spin in place left the given number of degrees at the given speed,
    where speed is between -100 (full speed spin_right) and 100 (full speed spin_left).
    Uses the algorithm:
      0. Compute the number of seconds to move to achieve the desired distance.
      1. Start moving.
      2. Sleep for the computed number of seconds.
      3. Stop moving.
    """
    # Connect two large motors on output ports B and C
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)

    # Check that the motors are actually connected
    speed *= 8
    assert left_motor.connected
    assert right_motor.connected
    encoder_degrees = (degrees * 4.25)
    time_run = abs(encoder_degrees / speed)

    left_motor.run_timed(speed_sp=-speed, time_sp=time_run * 1000, stop_action=stop_action)
    right_motor.run_timed(speed_sp=speed, time_sp=time_run * 1000, stop_action=stop_action)


def spin_left_by_encoders(degrees, speed, stop_action):
    """
    Makes the robot spin in place left the given number of degrees at the given speed,
    where speed is between -100 (full speed spin_right) and 100 (full speed spin_left).
    Uses the algorithm:
      1. Compute the number of degrees the wheels should spin to achieve the desired distance.
      2. Move until the computed number of degrees is reached.
    """
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)

    # Check that the motors are actually connected
    speed *= 8
    assert left_motor.connected
    assert right_motor.connected
    encoder_degrees = (degrees * 4.5)

    left_motor.run_to_rel_pos(position_sp=-encoder_degrees, speed_sp=speed, stop_action=stop_action)
    right_motor.run_to_rel_pos(position_sp=encoder_degrees, speed_sp=speed, stop_action=stop_action)
    left_motor.wait_while(ev3.Motor.STATE_RUNNING)
    right_motor.wait_while(ev3.Motor.STATE_RUNNING)


def spin_right_seconds(seconds, speed, stop_action):
    """ Calls spin_left_seconds with negative speeds to achieve spin_right motion. """
    spin_left_seconds(seconds, -speed, stop_action)


def spin_right_by_time(degrees, speed, stop_action):
    """ Calls spin_left_by_time with negative speeds to achieve spin_right motion. """
    spin_left_by_time(degrees, -speed, stop_action)


def spin_right_by_encoders(degrees, speed, stop_action):
    """ Calls spin_left_by_encoders with negative speeds to achieve spin_right motion. """
    spin_left_by_encoders(degrees, -speed, stop_action)


test_spin_left_spin_right()
