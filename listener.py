#Author: Gerardo Sanchez
#Date created: July 2, 2020

import paho.mqtt.client as mqtt
import time

broker_address = "127.0.0.1"

def on_message(client, userdata, message):
	print(message.topic)
	print(message.payload.decode(utf-8))

listen = mqtt.Client("Print Listener")
listen.on_message = on_message
listen.connect(broker_address)
listen.loop_start()
listen.subscribe("Game/+/+")

while True:
	time.sleep(0.05)
