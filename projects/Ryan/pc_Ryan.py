import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com


class Delegate(object):
    def __init__(self):
        pass

    def reach(self):
        print('The soda has been delivered')

    def reach2(self):
        print("The soda reached the destination and was not delivered")


def main():
    mqtt_client = com.MqttClient(Delegate())
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title("MQTT Remote")

    main_frame = ttk.Frame(root, padding=50, relief='raised')
    main_frame.grid()

    value = tkinter.IntVar()
    check = ttk.Checkbutton(main_frame, text='Deliver?', variable=value)
    check.grid(row=4, column=0)

    close_button = ttk.Button(main_frame, text="Close")
    close_button.grid(row=2, column=1)
    # forward_button and '<Up>' key is done for your here...
    # forward_button['command'] = lambda: some_callback1(mqtt_client, left_speed_entry, right_speed_entry)
    # root.bind('<Up>', lambda event: some_callback1(mqtt_client, left_speed_entry, right_speed_entry))
    close_button['command'] = lambda: send_close(mqtt_client)

    start_button = ttk.Button(main_frame, text="Start")
    start_button.grid(row=3, column=0)
    # left_button and '<Left>' key
    start_button['command'] = lambda: send_start(mqtt_client, value.get())

    open_button = ttk.Button(main_frame, text="open")
    open_button.grid(row=4, column=1)
    # back_button and '<Down>' key
    open_button['command'] = lambda: send_open(mqtt_client)

    # Buttons for quit and exit
    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=5, column=2)
    q_button['command'] = (lambda: quit_program(mqtt_client, False))

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=6, column=2)
    e_button['command'] = (lambda: quit_program(mqtt_client, True))

    root.mainloop()


def send_close(mqtt_client):
    print("robot_forward")
    mqtt_client.send_message("arm_close")


def send_open(mqtt_client):
    print("robot_back")
    mqtt_client.send_message("arm_open")


def send_start(mqtt_client, value):
    print("robot_left")
    mqtt_client.send_message("ryan_start", [value])


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
