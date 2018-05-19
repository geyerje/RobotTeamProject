import tkinter
from tkinter import ttk
import time


def Main():
    value = 0
    root = tkinter.Tk()
    root.title("MQTT Remote")

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()


    check = ttk.Checkbutton(main_frame, text='Use Metric', variable=value,
                                onvalue= 1, offvalue= 0)
    check.grid(row=0, column = 0)

    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=2, column=1)
    # forward_button and '<Up>' key is done for your here...
    # forward_button['command'] = lambda: some_callback1(mqtt_client, left_speed_entry, right_speed_entry)
    # root.bind('<Up>', lambda event: some_callback1(mqtt_client, left_speed_entry, right_speed_entry))
    forward_button['command'] = lambda: wumbo(value)

    root.mainloop()


def wumbo(value):
    print(value)

Main()