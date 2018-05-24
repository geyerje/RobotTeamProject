def watch_move(self, left_speed, right_speed):
    while self.color_sensor.color != 1:
        self.right_motor.run_forever(speed_sp=right_speed)
        self.left_motor.run_forever(speed_sp=left_speed)
    self.stop_robot()
    self.right_motor.run_timed(speed_sp=-800, time_sp=100)
    self.left_motor.run_timed(speed_sp=-800, time_sp=100)
