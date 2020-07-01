# Author: Gerardo Sanchez
# Date Created: June 29, 2020

import paho.mqtt.client as mqtt
import time
from numpy import random

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
listen.loop_start()

listen.subscribe("Players/+")

class Game:

    def __init__(self):
        self.stack =

    funkyrule1 = 1
    nextcard = 2
    pub.publish("Mainstack/nextcard",game.nextcard)

game.nextcard = random.rand(52)

no_winner = True

game()
while no_winner:
    game()
    time.sleep()
