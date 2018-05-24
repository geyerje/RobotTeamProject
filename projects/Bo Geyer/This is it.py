import tkinter
from tkinter import ttk
from tkinter import messagebox

import mqtt_remote_method_calls as com


def main():
    # DONE: 2. Setup an mqtt_client.  Notice that since you don't need to receive any messages you do NOT need to have
    # a MyDelegate class.  Simply construct the MqttClient with no parameter in the constructor (easy).
    mqtt_client = com.MqttClient()  # Delete this line, it was added temporarily so that the code we gave you had no errors.
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title("MQTT Remote")

    main_frame = ttk.Frame(root, padding=300, relief='raised')
    main_frame.grid()

    forward_button = ttk.Button(main_frame, text="Play Fetch")
    forward_button.grid(row=2, column=1)
    # forward_button and '<Up>' key is done for your here...
    # forward_button['command'] = lambda: some_callback1(mqtt_client, left_speed_entry, right_speed_entry)
    # root.bind('<Up>', lambda event: some_callback1(mqtt_client, left_speed_entry, right_speed_entry))
    forward_button['command'] = lambda: Fetch(mqtt_client)

    stop_button = ttk.Button(main_frame, text="Give treat")
    stop_button.grid(row=3, column=1)
    # stop_button and '<space>' key (note, does not need left_speed_entry, right_speed_entry)
    stop_button['command'] = lambda: Give_treat(mqtt_client)

    root.mainloop()


def Fetch(mqtt_client):
    print("Fetch")
    mqtt_client.send_message("Bo_Project")

def Give_treat(mqtt_client):
    print("Good boy")
    mqtt_client.send_message("Give_treat")


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()