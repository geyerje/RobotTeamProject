import tkinter
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

import mqtt_remote_method_calls as com


def main():
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title("MQTT Remote")

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    photo = Image.open("maze.png")
    lime = ImageTk.PhotoImage(photo)
    label = Label(root, image=lime)
    label.grid(row=1, column=3)

    left_speed_label = ttk.Label(main_frame, text="Left")
    left_speed_label.grid(row=0, column=0)
    left_speed_entry = ttk.Entry(main_frame, width=8)
    left_speed_entry.insert(0, "600")
    left_speed_entry.grid(row=1, column=0)

    right_speed_label = ttk.Label(main_frame, text="Right")
    right_speed_label.grid(row=0, column=2)
    right_speed_entry = ttk.Entry(main_frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "600")
    right_speed_entry.grid(row=1, column=2)

    button_left = ttk.Button(main_frame, text="Left")
    button_left.grid(row=3, column=0)
    button_left['command'] = lambda: send_left(mqtt_client, left_speed_entry.get(), right_speed_entry.get())
    root.bind('<Left>', lambda event: send_left(mqtt_client, left_speed_entry.get(), right_speed_entry.get()))

    button_right = ttk.Button(main_frame, text="Right")
    button_right.grid(row=3, column=2)
    button_right['command'] = lambda: send_right(mqtt_client, left_speed_entry.get(), right_speed_entry.get())
    root.bind('<Right>', lambda event: send_right(mqtt_client, left_speed_entry.get(), right_speed_entry.get()))

    button_forward = ttk.Button(main_frame, text="Forward")
    button_forward.grid(row=2, column=1)
    button_forward['command'] = lambda: send_forward(mqtt_client, left_speed_entry.get(), right_speed_entry.get())
    root.bind('<Up>', lambda event: send_forward(mqtt_client, left_speed_entry.get(), right_speed_entry.get()))

    button_back = ttk.Button(main_frame, text="Back")
    button_back.grid(row=4, column=1)
    button_back['command'] = lambda: send_back(mqtt_client, left_speed_entry.get(), right_speed_entry.get())
    root.bind('<Down>', lambda event: send_back(mqtt_client, left_speed_entry.get(), right_speed_entry.get()))

    button_stop = ttk.Button(main_frame, text="Stop")
    button_stop.grid(row=3, column=1)
    button_stop['command'] = lambda: stop(mqtt_client)
    root.bind('<space>', lambda event: stop(mqtt_client))

    button_quit = ttk.Button(main_frame, text="Quit")
    button_quit.grid(row=5, column=2)
    button_quit['command'] = (lambda: quit_program(mqtt_client, False))

    button_exit = ttk.Button(main_frame, text="Exit")
    button_exit.grid(row=6, column=2)
    button_exit['command'] = (lambda: quit_program(mqtt_client, True))

    button_arm_up = ttk.Button(main_frame, text="Arm Up")
    button_arm_up.grid(row=5, column=0)
    button_arm_up['command'] = lambda: send_up(mqtt_client)

    button_arm_down = ttk.Button(main_frame, text="Arm Down")
    button_arm_down.grid(row=6, column=0)
    button_arm_down['command'] = lambda: send_down(mqtt_client)

    root.mainloop()

###########################################################
# Callbacks for robot functions with drive and arm motors #
###########################################################


# turns the robot left by turning left base motor backwards and right base motor forwards
def send_left(mqtt_client, left, right):
    print("robot_left with left speed", -int(left), "and right speed", right)
    mqtt_client.send_message("watch_turn", [-int(left), right])


# turns the robot right by turning right base motor backwards and left base motor forwards
def send_right(mqtt_client, left, right):
    print("robot_right with left speed", left, "and right speed", -int(right))
    mqtt_client.send_message("watch_turn", [left, -int(right)])


def send_forward(mqtt_client, left, right):
    print("robot_forward with left speed", left, "and right speed", right)
    mqtt_client.send_message("watch_move", [left, right])


def send_back(mqtt_client, left, right):
    print("robot_back with left speed", -int(left), "and right speed", -int(right))
    mqtt_client.send_message("watch_move", [-int(left), -int(right)])


def stop(mqtt_client):
    mqtt_client.send_message("stop_robot")
    print("robot_stop")


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
