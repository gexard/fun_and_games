#Author: Gerardo Sanchez
#Date Created: July 2, 2020

import paho.mqtt.client as mqtt
import time

broker_address = "127.0.0.1"
pub = mqtt.Client("Player Publisher")
pub.connect(broker_address)

def on_message(client, userdata, message):
    if message.topic == "Game/Players/Turn":
        turn = message.payload.decode(utf-8)
        print('it is ' + str(turn) + "'s turn to play! \n")
        if turn == player.name:
            player.turn = True
    elif message.topic == "Game/Pieces/NextPiece":
        piece = message.payload.decode("utf-8")
        player.nextpieces.append(piece)
        print("you have drawn " + str(piece))
    elif message.topic == "Game/Winner":
        player.piecesinhand = False
        print(message.payload.decode(utf-8) + ' has won!!!')
    elif message.topic == "Game/L/LastPiecePlayed":
        self.game.append(message.payload.decode(utf-8))
    elif message.topic == "Game/R/LastPiecePlayed":
        self.game.insert(0,message.payload.decode(utf-8))

listen = mqtt.Client("Player Listener")
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

class Player:

    def __init__(self):
        self.hand = []
        self.turn = False
        self.piecesinhand = True
        self.game = []
        self.piecetoplay = ()
        self.nextpieces = []
        self.side = ''
        self.name = input('Player Name: \n')
        pub.publish("Game/AddPlayer", self.name)

    def drawpiece(self,n):
        print('Drawing ' + str(n) + ' pieces')
        pub.publish('Game/' + self.name + '/DrawPieces',n)
        time.sleep(n+2)
        self.hand.append(self.nextpieces)
        print("Your current hand is: " + str(self.hand))


    def playpiece(self):
        print(self.hand)
        self.piecetoplay = input('What piece do you want to play? \n')
        self.side = input('Which side do you want to play it? (L or R)\n')
        if self.side == 'L':
            pub.publish("Game/L/LastPiecePlayed",self.piecetoplay)
        elif self.side == 'R':
            pub.publish("Game/R/LastPiecePlayed",self.piecetoplay)

player=Player()
input("Are you ready to start? \n")
pub.publish("Game/Start", payload=None)
player.drawpiece(7)
while player.piecesinhand:
    if player.turn:
        abletoplay = input("Enter 'y' if you can play a piece \n")
        if abletoplay == 'y':
            player.playpiece()
        else:
            player.drawpiece(1)
        if len(player.hand) == 0:
            player.piecesinhand = False
            pub.publish('Game/Winner',player.name)
    time.sleep(0.1)
pub.publish("Game/Winner", player.name)
