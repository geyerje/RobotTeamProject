import mqtt_remote_method_calls as com
import robot_controller as robo


def main():
    robot = robo.Snatch3r()
    mqtt_client = com.MqttClient(robot)
    mqtt_client.connect_to_pc()
    robot.loop_forever()

    while True:
        if robot.color_sensor.color == 1:
            mqtt_client.send_message("printer", ["LOOK OUT FOR THE BLACK LINES"])


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
