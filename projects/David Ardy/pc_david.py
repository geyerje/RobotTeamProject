import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com


def main():
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title("MQTT Remote")

    main_frame = ttk.Frame(root, padding=25, relief='raised')
    main_frame.grid()

    left_speed_label = ttk.Label(main_frame, text="Left")
    left_speed_label.grid(row=0, column=0)

    left_speed_entry = ttk.Entry(main_frame, width=8)
    left_speed_entry.insert(0, "600")
    left_speed_entry.grid(row=1, column=0)

    right_speed_label = ttk.Label(main_frame, text="Right")
    right_speed_label.grid(row=0, column=3)
    right_speed_entry = ttk.Entry(main_frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "600")
    right_speed_entry.grid(row=1, column=3)

    button_left = ttk.Button(main_frame, text="Left")
    button_left.grid(row=3, column=0)
    button_left['command'] = lambda: send_left(mqtt_client, left_speed_entry.get(), right_speed_entry.get())
    root.bind('<Right>', lambda event: send_left(mqtt_client, left_speed_entry.get(), right_speed_entry.get()))

    button_right = ttk.Button(main_frame, text="Right")
    button_right.grid(row=3, column=3)
    button_right['command'] = lambda: send_right(mqtt_client, left_speed_entry.get(), right_speed_entry.get())
    root.bind('<Right>', lambda event: send_right(mqtt_client, left_speed_entry.get(), right_speed_entry.get()))

    root.mainloop()

###########################################################
# Callbacks for robot functions with drive and arm motors # 
###########################################################


# turns the robot left by turning left base motor backwards and right base motor forwards
def send_left(mqtt_client, left, right):
    print("robot_left with left speed", -int(left), "and right speed", right)
    mqtt_client.send_message("move", [-int(left), right])


# turns the robot right by turning right base motor backwards and left base motor forwards
def send_right(mqtt_client, left, right):
    print("robot_right with left speed", left, "and right speed", -int(right))
    mqtt_client.send_message("move", [left, -int(right)])


def send_forward(mqtt_client, left, right):
    print("robot_forward with left speed", left, "and right speed", right)
    mqtt_client.send_message("move", [left, right])


def send_back(mqtt_client, left, right):
    print("robot_back with left speed", -int(left), "and right speed", -int(right))
    mqtt_client.send_message("move", [-int(left), -int(right)])


def stop(mqtt_client):
    print("robot_stop")
    mqtt_client.send_message("stop_robot")


def send_up(mqtt_client):
    print("arm_up")
    mqtt_client.send_message("arm_up")


def send_down(mqtt_client):
    print("arm_down")
    mqtt_client.send_message("arm_down")


# Quit callbacks to quit program without errors
def quit_program(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("shutdown")
        mqtt_client.send_message("shutdown")
    mqtt_client.close()
    exit()


main()
