def watch_move(self, left_speed, right_speed):
    self.right_motor.run_forever(speed_sp=right_speed)
    self.left_motor.run_forever(speed_sp=left_speed)
    # while self.color_sensor.color == 1:
    #     pass
    # self.stop_robot()
    # ev3.Sound.speak('WALL')
    # self.right_motor.run_timed(speed_sp=-800, time_sp=1000)
    # self.left_motor.run_timed(speed_sp=-800, time_sp=1000)


def watch_turn(self, left_speed, right_speed):
    self.right_motor.run_timed(speed_sp=right_speed, time_sp=2000)
    self.left_motor.run_timed(speed_sp=left_speed, time_sp=2000)


def hard_stop(self, stop_action='brake'):
    self.left_motor.stop(stop_action=stop_action)
    self.right_motor.stop(stop_action=stop_action)
    self.arm_motor.stop(stop_action=stop_action)
    time.sleep(0.05)