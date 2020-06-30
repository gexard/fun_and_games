# Author: Gerardo Sanchez
# Date Created: June 29, 2020

import paho.mqtt.client as mqtt
import time

broker_address = "127.0.0.1"
pub = mqtt.Client("Main Game Publisher")
pub.connect(broker_address)

def on_message(client, userdata, message):
    if message.topic == "Players/1/playcard":
        print("Card played")
    if message.topic == "Players/2/playcard":
        print("Card played")

listen = mqtt.Client("Main Game Listener")
listen.on_message = on_message
listen.connect(broker_address)
listen.lop_start()

listen.subscribe("Players/+")

def game():

    funkyrule1 = 1
    nextcard = 2
    pub .publish("Mainstack/nextcard",stack.nextcard)

stack.nextcard = random(52)

no_winner = False

while no_winner:
    game()
    time.sleep()
