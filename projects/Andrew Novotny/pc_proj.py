import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com


class Computer(object):
    def __init__(self):
        pass

    def printer(self, value):
        print(value)

def main():
    mqtt_client = com.MqttClient(Computer())
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title("MQTT Remote")

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    value = tkinter.IntVar()
    check = ttk.Checkbutton(main_frame, text='Continuous?', variable=value)
    check.grid(row=4, column=0)

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


    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=2, column=1)
    # forward_button and '<Up>' key is done for your here...
    # forward_button['command'] = lambda: some_callback1(mqtt_client, left_speed_entry, right_speed_entry)
    # root.bind('<Up>', lambda event: some_callback1(mqtt_client, left_speed_entry, right_speed_entry))
    forward_button['command'] = lambda: send_forward(mqtt_client, left_speed_entry.get(), right_speed_entry.get(), value.get())
    root.bind('<Up>', lambda event: send_forward(mqtt_client, left_speed_entry.get(), right_speed_entry.get(), value.get()))

    left_button = ttk.Button(main_frame, text="Left")
    left_button.grid(row=3, column=0)
    # left_button and '<Left>' key
    left_button['command'] = lambda: send_left(mqtt_client, left_speed_entry.get(), right_speed_entry.get(), value.get())
    root.bind('<Left>', lambda event: send_left(mqtt_client, left_speed_entry.get(), right_speed_entry.get(), value.get()))

    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=3, column=1)
    # stop_button and '<space>' key (note, does not need left_speed_entry, right_speed_entry)
    stop_button['command'] = lambda: stop(mqtt_client)
    root.bind('<space>', lambda event: stop(mqtt_client))

    right_button = ttk.Button(main_frame, text="Right")
    right_button.grid(row=3, column=2)
    # right_button and '<Right>' key
    right_button['command'] = lambda: send_right(mqtt_client, left_speed_entry.get(), right_speed_entry.get(), value.get())
    root.bind('<Right>', lambda event: send_right(mqtt_client, left_speed_entry.get(), right_speed_entry.get(), value.get()))


    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid(row=4, column=1)
    # back_button and '<Down>' key
    back_button['command'] = lambda: send_back(mqtt_client, left_speed_entry.get(), right_speed_entry.get(), value.get())
    root.bind('<Down>', lambda event: send_back(mqtt_client, left_speed_entry.get(), right_speed_entry.get(), value.get()))

    # Buttons for quit and exit
    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=5, column=2)
    q_button['command'] = (lambda: quit_program(mqtt_client, False))

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=6, column=2)
    e_button['command'] = (lambda: quit_program(mqtt_client, True))


    root.mainloop()



# Arm command callbacks
def send_forward(mqtt_client, left, right, value):
    print("robot_forward")
    mqtt_client.send_message("move3", [left, right, value])

def send_back(mqtt_client, left, right, value):
    print("robot_back")
    mqtt_client.send_message("move3", [-int(left), -int(right), value])

def send_right(mqtt_client, left, right, value):
    print("robot_right")
    mqtt_client.send_message("move3", [left, -int(right), value])

def send_left(mqtt_client, left, right, value):
    print("robot_left")
    mqtt_client.send_message("move3", [-int(left), right, value])

def stop(mqtt_client):
    print("robot_stop")
    mqtt_client.send_message("stop_robot")

# Quit and Exit button callbacks
def quit_program(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("shutdown")
        mqtt_client.send_message("shutdown")
    mqtt_client.close()
    exit()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
