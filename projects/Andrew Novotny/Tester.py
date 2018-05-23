import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com


def main():
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title("Color Tester")

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    ColorButton = ttk.Button(main_frame, text="Get Color")
    ColorButton.grid(row=0, column=0)
    ColorButton['command'] = lambda: move2(mqtt_client, 400, 400)

    root.mainloop()

left = 100
right = 100

def move2(mqtt_client, left, right):
    mqtt_client.send_message("move2", [left, right])

main()
