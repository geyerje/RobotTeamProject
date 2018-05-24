def watch_move(self, left_speed, right_speed):
    # while self.color_sensor.color != 1:
    while self.color_sensor.color != 1:
        self.right_motor.run_forever(speed_sp=right_speed)
        self.left_motor.run_forever(speed_sp=left_speed)
        # time.sleep(0.05)
    self.hard_stop()
    ev3.Sound.speak('WALL')
    self.right_motor.run_timed(speed_sp=-400, time_sp=400)
    self.left_motor.run_timed(speed_sp=-400, time_sp=400)
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
            break
    self.arm_motor.stop()
    self.mqtt.send_message('end_response')