

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


def send_left(mqtt_client, left, right):
    print("robot_left with left speed ", [-int(left), " and right speed ", right])
    mqtt_client.send_message("move", [-int(left), right])


def send_right(mqtt_client, left, right):
    print("robot_right")
    mqtt_client.send_message("move", [left, -int(right)])


main()
