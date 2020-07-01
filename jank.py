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

def deck():
    deck = []
    suites = ['Clubes', 'Hearts','Spades','Diamonds']
    for i in range(13):
        suite = suites[i]
        for j in range(4):
            if i == 1:
                deck.append( 'Ace' + ' of ' + suite)
            elif i < 10:
                deck.append( str(j) + ' of ' + suite)
            elif i == 10:
                deck.append( 'Bubbe' + ' of ' + suite)
            elif i == 11:
                deck.append( 'Queen' + ' of ' + suite)
            elif i == 12:
                deck.append( 'King' + ' of ' + suite)
    deck.append('Black Jank')
    deck.append('Red Jank')
    return deck

class Player:

    def __init__():
        self.name = input("Player name: \n")

class Game:

    def __init__(self):
        self.deck = CreateStack()
        self.stacks = {}

    def nextCard():
        l = len(self.deck)
        r = random.rand(l)
        self.nextcard = self.deck[r]
        del self.deck[r]
        pub.publish("Mainstack/nextcard",game.nextcard)

    def shuffle(self):
        stuff

    def Cuts(self):
        stuff

    def CallAJank(self):
        stuff

    def CreateStack(self):
        stuff

    def KillStack(self):

    def rule1(self):
        if self.card == 'Jank':
            print('Game over')

    def cross(self):
        stuff

no_winner = True
while no_winner:
    game()
    time.sleep()
