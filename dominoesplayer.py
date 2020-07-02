#Author: Gerardo Sanchez
#Date Created: July 2, 2020

import paho.mqtt.client as mqtt
import time

broker_address = "127.0.0.1"
pub = mqtt.Client("Player Publisher")
pub.connect(broker_address)

def on_message(client, userdata, message):
    if message.topic == "Game/Players/Turn":
        player.turn = True

listen = mqtt.Client("Player Listener")
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

class Player:

    def __init__(self):
        self.hand = []
        self.turn = False
        self.piecesinhand = True
        self.piecetoplay = ()
        self.side = ''
        self.name = input('Player Name: \n')
        pub.publish("Game/AddPlayer",self.name)

    def hand(self):


    def playpiece(self):
        print(self.hand)
        self.piecetoplay = input('What piece do you want to play? \n')
        self.side = input('Which side do you want to play it? (L or R)\n')
        if self.side == 'L':
            pub.publish("Game/L/LastPiecePlayed",self.piecetoplay)
        elif self.side == 'R':
            pub.publish("Game/R/LastPiecePlayed",self.piecetoplay)

player=Player()
while player.piecesinhand:
    if player.turn:
        player.playpiece()
    time.sleep(0.1)
pub.publish("Game/Winner", player.name)
