import tkinter
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

import mqtt_remote_method_calls as com

class computer(object):
    def __init__(self):
        pass

    def respond(self):
        print('That was fun, lets play again!')


def main():
    # DONE: 2. Setup an mqtt_client.  Notice that since you don't need to receive any messages you do NOT need to have
    # a MyDelegate class.  Simply construct the MqttClient with no parameter in the constructor (easy).
    mqtt_client = com.MqttClient(computer())  # Delete this line, it was added temporarily so that the code we gave you had no errors.
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title("MQTT Remote")

    main_frame = ttk.Frame(root, padding=100, relief='raised')
    main_frame.grid()

    photo = Image.open("dog.png")
    lime = ImageTk.PhotoImage(photo)
    label = Label(root, image=lime)
    label.grid(row=1, column=2)

    forward_button = ttk.Button(main_frame, text="Play Fetch")
    forward_button.grid(row=2, column=1)
    forward_button['command'] = lambda: Fetch(mqtt_client)

    root.mainloop()



def Fetch(mqtt_client):
    print("Fetch")
    mqtt_client.send_message("bo_project")

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()



