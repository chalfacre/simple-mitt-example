#!/usr/bin/env python3

# publisher
import paho.mqtt.client as mqtt
from Tkinter import *

MOTOR    = "MOTOR_CONTROL"
AUTO     = "AUTONOMOUS"
FORWARD  = "FORWARD"
BACKWARD = "BACKWARD"
LEFT     = "LEFT"
RIGHT    = "RIGHT"
STOP     = "STOP"

# This is the Publisher

def key_input(event):
    print 'Key:', event.char
    key_press = event.char
    sleep_time = 0.030

    if key_press.lower() == 'w':
        print "Sending FORWARD"
        client.publish(MOTOR, FORWARD);
    elif key_press.lower() == 's':
        client.publish(MOTOR, BACKWARD);
    elif key_press.lower() == 'a':
        client.publish(MOTOR, LEFT);
    elif key_press.lower() == 'd':
        client.publish(MOTOR, RIGHT);
    elif key_press.lower() =='q':
        client.publish(MOTOR, STOP);
        client.disconnect();
    elif key_press.lower() == 'e':
        client.publish(MOTOR, AUTO);
    
        

client = mqtt.Client()
client.connect("localhost",1883,60)
print ("Connected to localhost")
root = Tk()
frame = Frame(root, width=100, height=100)
frame.bind('<KeyPress>', key_input)
frame.pack()
frame.focus_set()
root.mainloop()

