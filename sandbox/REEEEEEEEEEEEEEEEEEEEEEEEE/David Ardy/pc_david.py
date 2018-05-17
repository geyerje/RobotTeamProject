# class RobotDelegate(object):
#     def __init__(self):
#         self.robot = robo.Snatch3r()
#
#     def blah(self):
#         self.robot


import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com


def main():
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title("MQTT Remote")

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()
    
    root.mainloop()
