#Authors: David Fisher and James (Bo) Geyer.


import ev3dev.ev3 as ev3
import time

import robot_controller as robo

# import tkinter
# from tkinter import ttk
#
# import mqtt_remote_method_calls as com

# mqtt_client = com.MqttClient()
# mqtt_client.connect_to_ev3()
#
# root = tkinter.Tk()
# root.title("MQTT Remote")
#
# main_frame = ttk.Frame(root, padding=20, relief='raised')
# main_frame.grid()
#
# stop_button = ttk.Button(main_frame, text="Stop")
# stop_button.grid(row=3, column=1)
# # stop_button and '<space>' key (note, does not need left_speed_entry, right_speed_entry)
# stop_button['command'] = lambda: stop(mqtt_client)
# root.bind('<space>', lambda event: stop(mqtt_client))
#
# root.mainloop()

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
    army = False
    ir_sensor = robot.ir_sensor


    #while True:
    #    print(ir_sensor.proximity)
    #    time.sleep(0.1)

    while True:
            print("(X, Y)=({}, {}) Width={} Height={}".format(
                pixy.value(1), pixy.value(2), pixy.value(3),
                pixy.value(4)))

            while pixy.value(1) == 0:
                time.sleep(1)

            while pixy.value(1) < 170:
                robot.turn_left(200)
            robot.stop_robot()
            time.sleep(0.05)

            while pixy.value(1) > 190:
                robot.turn_right(200)
            robot.stop_robot()
            time.sleep(0.05)

            while pixy.value(1) > 170 and pixy.value(1) < 190:
                time.sleep(1)
                while ir_sensor.proximity >= 35:
                    robot.move(400, 400)
                    if (pixy.value(1) < 170 or pixy.value(1) > 190):
                        robot.stop_robot()
                        robot.re_center()
                while ir_sensor.proximity > 0:
                    robot.move(150,150)
                    time.sleep(0.1)
                robot.stop_robot()
                time.sleep(1)

                robot.arm_up()
                army = True
                break

            print(robot.positions)
            print(army)
            while army == True:
                for k in range(len(robot.positions), 0, -2):
                    print("Im inside the loop")
                    pos_r = robot.positions[k-1]
                    pos_l = robot.positions[k-2]
                    robot.abs_move(pos_l, pos_r)
                print("I got here")
                robot.turn_right_by_encoders(180, 200)
                robot.arm_down()
                army = False
                robot.turn_left_by_encoders(180, 200)
                robot.right_motor.reset()
                robot.left_motor.reset()
                robot.positions = [robot.left_motor.position, robot.right_motor.position]
                ev3.Sound.speak("roof roof").wait()



            # time.sleep(0.25)
            # print("Goodbye!")
            # ev3.Sound.speak("Goodbye").wait()
