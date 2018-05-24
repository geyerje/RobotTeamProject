import ev3dev.ev3 as ev3
import time

import robot_controller as robo

robot = robo.Snatch3r()

while True:
    Location = robot.right_motor.position
    print(Location)
    time.sleep(2)
