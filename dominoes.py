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
        player = message.payload.decode('utf-8')
        game.players.append(player)
        print('currently playing: ' + str(game.players))
    elif message.topic == "Game/Winner":
        game.no_winner = False
        print("The winner is: " + message.payload.decode('utf-8'))
    elif message.topic == "Game/EndTurn":
        game.nextTurn()
    elif message.topic == "Game/Start":
        pub.publish("Game/Players/Turn", game.currentplayer, retain = True)
        print("The game has started! The first player is: " + game.currentplayer + "\n")
    for player in game.players:
        if message.topic == "Game/" + player + "/DrawPieces":
            for pieces in range(int(message.payload.decode('utf-8'))):
                print(player + ' is drawing a piece')
                game.nextPiece()
                time.sleep(1)

listen = mqtt.Client("Game Listener")
listen.on_message = on_message
listen.connect(broker_address)
listen.loop_start()

listen.subscribe("Game/+/+")

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
        r = random.randint(0,l)
        self.nextpiece = self.pieces[r]
        del self.pieces[r]
        print(self.nextpiece)
        pub.publish("Game/Pieces/NextPiece",self.nextpiece)

    def nextTurn(self):
        self.currentplayer += 1
        if self.currentplayer > len(self.players):
            self.currentplayer = 0
        pub.publish("Game/Players/Turn",self.players[self.currentplayer],retain=True)

game=Game()
while game.no_winner:
    time.sleep(0.1)
