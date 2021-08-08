# Author: Gerardo Sanchez
# Date Created: May 1, 2021

from numpy import random

class piece:
    """a single piece."""

    def __init__(self, l, r):
        self.left = l
        self.right = r

def CreatePieces(n):
    pieces = []
    for l in range(n):
        for r in range(n-l):
            pieces.append(piece(l,n-1-r))
    return pieces

class Game:

    def __init__(self):
        self.pieces = CreatePieces(7)
        self.remainingpieces = CreatePieces(7)
        self.no_winner = True

    def nextPiece(self):
        l = len(self.remainingpieces)
        if l > 0:
            c = True
            p = 0
            while c:
                r = random.randint(0,len(self.pieces))
                if self.pieces[r] in self.remainingpieces:
                    c = False
            del self.remainingpieces[r]
        else:
            print('The pile ran out of pieces!')

    def nextTurn(self):

class Player:

    def __init__(self):
        self.hand = []
        self.vhand =[]
        self.turn = False
        self.piecesinhand = True
        self.piecestodraw = True
        self.game = []
        self.piecetoplay = ()
        self.wait = True
        self.nextpieces = []
        self.name = input('Player Name: \n')
        self.drawpiece(7)

    def drawpiece(self,n):
        print('Drawing ' + str(n) + ' pieces')
        pub.publish('Game/DrawPieces', n)
        self.wait = True
        while self.wait:
            time.sleep(0.1)
        for i in range(n):
            self.hand.append(self.nextpieces[i])
            self.vhand.append(self.pieceref[self.nextpieces[i]])
        print("Your current hand is: " + str(self.vhand))


    def playpiece(self):
        print('Your pieces are: ')
        print(self.vhand)
        p = int(input('What piece do you want to play? (Enter its position)\n'))
        side = input('Which side do you want to play it? (L or R)\n')
        if side == 'L':
            pub.publish("Game/LLastPiecePlayed",self.hand[p])
        elif side == 'R':
            pub.publish("Game/RLastPiecePlayed",self.hand[p])
        del self.hand[p]
        self.turn = False
        pub.publish("Game/EndTurn", payload=None)

    def abletoplay(self):
        pass

class Bots:

    def __init__(self,n):
        for i in n:
            self.bots.append()


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


game = Game()
player = Player()
num_of_bots = input('How many bots? \n')
bots = Bots(num_of_bots)
while game.no_winner:
    time.sleep(0.1)
