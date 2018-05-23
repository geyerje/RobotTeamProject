import mqtt_remote_method_calls as com
import robot_controller as robo
import ev3dev as ev3

def main():
    robot = robo.Snatch3r()
    mqtt_client = com.MqttClient(robot)
    robot.mqtt = mqtt_client
    mqtt_client.connect_to_pc()
    robot.loop_forever()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
