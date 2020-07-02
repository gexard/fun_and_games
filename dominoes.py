# Author: Gerardo Sanchez
# Date Created: July 2, 2020

import paho.mqtt.client as mqtt
import time
from numpy import random

broker_address = "127.0.0.1"
pub = mqtt.Client("Game Publisher")
pub.connect(broker_address)

def on_message(client, userdata, message):
    if message.topic == "Game/AddPlayer":
        Game.players.append(message.payload.decode('utf-8'))
    elif message.topic == "Game/Winner":
        Game.no_winner = False
    elif message.topic == "Game/EndTurn":
        Game.nextTurn()
    for player in Game.players:
        if message.topic == "Game/" + player + "/DrawPiece":
            Game.nextPiece()

listen = mqtt.Client("Game Listener")
listen.on_message = on_message
listen.connect(broker_address)
listen.loop_start()

listen.subscribe("Game/+")

def CreatePieces():
    pieces = []
    n = 7
    for l in range(n):
        for r in range(n-l):
            pieces.append((l,n-1-r))
    return pieces

class Game:

    def __init__(self):
        self.pieces = CreatePieces()
        self.nextpiece = 'none'
        self.players = []
        self.currentplayer = 0
        self.no_winner = True

    def nextPiece(self):
        l = len(self.pieces)
        r = random.rand(l)
        self.nextpiece = self.pieces[r]
        del self.pieces[r]
        pub.publish("Game/Pieces/NextPiece",self.nextpiece)

    def nextTurn(self):
        self.currentplayer += 1
        if self.currentplayer > len(self.players):
            self.currentplayer = 0
        pub.publish("Game/Players/Turn",self.currentplayer)

game=Game()
while game.no_winner:
    time.sleep(0.1)
