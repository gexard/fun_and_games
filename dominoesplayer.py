#Author: Gerardo Sanchez
#Date Created: July 2, 2020

import paho.mqtt.client as mqtt
import time

broker_address = "127.0.0.1"
pub = mqtt.Client("Player Publisher")
pub.connect(broker_address)

def on_message(client, userdata, message):
    if message.topic == "Game/Turn":
        turn = message.payload.decode('utf-8')
        print('it is ' + str(turn) + "'s turn to play! \n")
        if turn == player.name:
            player.turn = True
    elif message.topic == "Game/NoMorePieces":
        player.piecestodraw = False
        print("There are no more pieces to draw!")
    elif message.topic == "Game/NextPiece":
        piece = message.payload.decode("utf-8")
        player.nextpieces.append(piece)
    elif message.topic == "Game/Winner":
        player.piecesinhand = False
        print(message.payload.decode('utf-8') + ' has won!!!')
    elif message.topic == "Game/RLastPiecePlayed":
        player.game.append(message.payload.decode('utf-8'))
        print(player.game)
    elif message.topic == "Game/LLastPiecePlayed":
        player.game.insert(0,message.payload.decode('utf-8'))
        print(player.game)

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
        self.piecestodraw = True
        self.game = []
        self.piecetoplay = ()
        self.nextpieces = []
        self.side = ''
        self.name = input('Player Name: \n')
        pub.publish("Game/AddPlayer", self.name)

    def drawpiece(self,n):
        print('Drawing ' + str(n) + ' pieces')
        pub.publish('Game/' + self.name + 'DrawPieces',n)
        time.sleep(1)
        self.hand.append(self.nextpieces)
        print("Your current hand is: " + str(self.hand))


    def playpiece(self):
        print('Your pieces are: \n')
        print(self.hand)
        self.piecetoplay = input('What piece do you want to play? \n')
        self.side = input('Which side do you want to play it? (L or R)\n')
        if self.side == 'L':
            pub.publish("Game/LLastPiecePlayed",self.piecetoplay)
        elif self.side == 'R':
            pub.publish("Game/RLastPiecePlayed",self.piecetoplay)
        self.turn = False
        pub.publish("Game/EndTurn", payload=None)

    def abletoplay(self):
        pass

player=Player()
player.drawpiece(7)
input("Are you ready to start? \n")
pub.publish("Game/Start", payload=None)
time.sleep(1)
while player.piecesinhand:
    if player.turn:
        abletoplay = input("Enter 'y' if you can play a piece \n")
        if abletoplay == 'y':
            player.playpiece()
        elif player.piecestodraw:
            player.drawpiece(1)
        else:
            print('It seems you cannot play :(\n')
            self.turn = False
            pub.publish("Game/EndTurn", payload=None)
        if len(player.hand) == 0:
            player.piecesinhand = False
            pub.publish('Game/Winner',player.name)
        player.nextpieces = []
    time.sleep(0.1)
pub.publish("Game/Winner", player.name)
