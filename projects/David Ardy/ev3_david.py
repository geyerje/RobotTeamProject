# class RobotDelegate(object):
#     def __init__(self):
#         self.robot = robo.Snatch3r()
#
#     def blah(self):
#         self.robot

import mqtt_remote_method_calls as com
import robot_controller as robo


def main():
    robot = robo.Snatch3r()
    mqtt_client = com.MqttClient(robot)
    robot.mqtt = mqtt_client
    mqtt_client.connect_to_pc()
    robot.loop_forever()


main()
