import ev3dev.ev3 as ev3
import time

import robot_controller as robo

def main():
    ev3.Sound.speak("arm down").wait()

    robot = robo.Snatch3r()
    robot.arm_down()

    ev3.Sound.speak("done").wait()

main()