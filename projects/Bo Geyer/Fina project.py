#Authors: David Fisher and James (Bo) Geyer.


import ev3dev.ev3 as ev3
import time

import robot_controller as robo

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com

mqtt_client = com.MqttClient()
mqtt_client.connect_to_ev3()

root = tkinter.Tk()
root.title("MQTT Remote")

main_frame = ttk.Frame(root, padding=20, relief='raised')
main_frame.grid()

stop_button = ttk.Button(main_frame, text="Stop")
stop_button.grid(row=3, column=1)
# stop_button and '<space>' key (note, does not need left_speed_entry, right_speed_entry)
stop_button['command'] = lambda: stop(mqtt_client)
root.bind('<space>', lambda event: stop(mqtt_client))

root.mainloop()

def main():
    print("--------------------------------------------")
    print(" Fetch")
    print("--------------------------------------------")
    ev3.Sound.speak("Lets play fetch").wait()
    print("Press the touch sensor to exit this program.")


    robot = robo.Snatch3r()
    pixy = ev3.Sensor(driver_name="pixy-lego")
    pixy.mode = "SIG1"
    turn_speed = 100

    ir_sensor = robot.ir_sensor


    while True:
            print("(X, Y)=({}, {}) Width={} Height={}".format(
                pixy.value(1), pixy.value(2), pixy.value(3),
                pixy.value(4)))

            while pixy.value(1) == 0:
                time.sleep(1)


            print("(X, Y)=({}, {}) Width={} Height={}".format(
                pixy.value(1), pixy.value(2), pixy.value(3),
                pixy.value(4)))

            while pixy.value(1) < 150:
                robot.turn_left(200)
            robot.left_motor.stop()
            robot.right_motor.stop()
            time.sleep(0.05)

            while pixy.value(1) > 170:
                robot.turn_right(200)
            robot.left_motor.stop()
            robot.right_motor.stop()
            time.sleep(0.05)

            while pixy.value(1) > 150 and pixy.value(1) < 170:
                time.sleep(1)
                while ir_sensor.proximity >= 60:
                    robot.move(400,400)
                    time.sleep(1)
                    robot.left_motor.stop()
                    robot.right_motor.stop()
                    robot.re_center()
                while ir_sensor.proximity > 0:
                    robot.move(200,200)
                robot.left_motor.stop()
                robot.right_motor.stop()
                time.sleep(1)

                robot.arm_up()
                break
            break

    robot.turn_left_by_encoders(180,500)
    pixy.mode = "SIG2"

    while True:
            print("(X, Y)=({}, {}) Width={} Height={}".format(
                pixy.value(1), pixy.value(2), pixy.value(3),
                pixy.value(4)))

            while pixy.value(1) == 0:
                time.sleep(1)


            print("(X, Y)=({}, {}) Width={} Height={}".format(
                pixy.value(1), pixy.value(2), pixy.value(3),
                pixy.value(4)))

            while pixy.value(1) < 150:
                robot.turn_left(200)
            robot.left_motor.stop()
            robot.right_motor.stop()
            time.sleep(0.05)

            while pixy.value(1) > 170:
                robot.turn_right(200)
            robot.left_motor.stop()
            robot.right_motor.stop()
            time.sleep(0.05)

            while pixy.value(1) > 150 and pixy.value(1) < 170:
                time.sleep(1)
                while True:
                    robot.move(400,400)
                    time.sleep(1)
                    robot.left_motor.stop()
                    robot.right_motor.stop()
                    robot.re_center()
                    mqtt_client.send_message("stop_robot")
                robot.arm_down()
                break
            break


        # DOne: 3. Use the x value to turn the robot
        #   If the Pixy x value is less than 150 turn left (-turn_speed, turn_speed)
        #   If the Pixy x value is greater than 170 turn right (turn_speed, -turn_speed)
        #   If the Pixy x value is between 150 and 170 stop the robot
        # Continuously track the color until the touch sensor is pressed to end the program.



        time.sleep(0.25)

    print("Goodbye!")
    ev3.Sound.speak("Goodbye").wait()

main()