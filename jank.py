# Author: Gerardo Sanchez
# Date Created: June 29, 2020

import paho.mqtt.client as mqtt
import time
from numpy import random

broker_address = "127.0.0.1"
pub = mqtt.Client("Game Publisher")
pub.connect(broker_address)

def on_message(client, userdata, message):
    if message.topic == "Game/Winner":
        Game.no_winner = False
    elif message.topic == "Game/EndTurn":
        Game.nextTurn()
    elif message.topic == "Game/Players/AddPlayer":
        Game.players.append(message.payload.decode('utf-8'))
    for player in Game.players:
        if message.topic == "Game/" + player + "/DrawCard":
            Game.nextCard()

listen = mqtt.Client("Game Listener")
listen.on_message = on_message
listen.connect(broker_address)
listen.loop_start()

listen.subscribe("Game/+")

def CreateDeck():
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

class Game:

    def __init__(self):
        self.labeleddeck = CreateDeck()
        self.deck = range(54)
        self.nextcard = "none"
        self.players = []
        self.currentplayer = 0
        self.no_winner = True

    def nextCard(self):
        l = len(self.deck)
        r = random.rand(l)
        self.nextcard = self.deck[r]
        del self.deck[r]
        pub.publish("Game/Deck/NextCard",self.nextcard)

    def shuffle(self):
        #might not keep...
        pass

    def nextTurn(self):
        self.currentplayer += 1
        if self.currentplayer > len(self.players):
            self.currentplayer = 0
        pub.publish("Game/Players/Turn",self.currentplayer)

    def Cut(self):
        pass

while True:
    game()
    time.sleep(0.1)
