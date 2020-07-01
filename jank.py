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

<<<<<<< HEAD
game.nextcard = random.rand(52)

no_winner = True

game()
=======
Game.stack.nextcard = random(54)
Game.stack = []
no_winner = False

suites = ['Clubes', 'Hearts','Spades','Diamonds']
for i in range(13):
    suite = suites[i]
    for j in range(4):
        if i == 1:
            Game.stack.append( 'Ace' + ' of ' + suite)
        elif i < 10:
            Game.stack.append( str(j) + ' of ' + suite)
        elif i == 10:
            Game.stack.append( 'Bubbe' + ' of ' + suite)
        elif i == 11:
            Game.stack.append( 'Queen' + ' of ' + suite)
        elif i == 12:
            Game.stack.append( 'King' + ' of ' + suite)
Game.stack.append('Black Jank')
Game.stack.append('Red Jank')

>>>>>>> fd8d39ccc7ccb67b8cd67dbb069ccebf5316d23b
while no_winner:
    game()
    time.sleep()
