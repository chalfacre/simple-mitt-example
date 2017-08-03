#!/usr/bin/env python3

import paho.mqtt.client as mqtt

MOTOR    = "MOTOR_CONTROL"
AUTO     = "AUTONOMOUS"
FORWARD  = "FORWARD"
BACKWARD = "BACKWARD"
LEFT     = "LEFT"
RIGHT    = "RIGHT"
STOP     = "STOP"

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe(MOTOR)

def on_message(client, userdata, msg):
  if msg.payload.decode() == AUTO:
    print("Autonomous mode")
  elif msg.payload.decode() == FORWARD:
  	print("Forward")
  elif msg.payload.decode() == BACKWARD:
  	print("Backward")
  elif msg.payload.decode() == LEFT:
  	print("Left")
  elif msg.payload.decode() == RIGHT:
  	print("Right")
  elif msg.payload.decode() == STOP:
  	print("Stop")
  else:
  	print ("Invalid Key")
    #client.disconnect()
    
client = mqtt.Client()
client.connect("localhost",1883,60)

client.on_connect = on_connect
client.on_message = on_message


client.loop_forever()
