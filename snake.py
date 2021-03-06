import random
import turtle
import time
import os

class square:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def drawself(self,turtle):
        turtle.goto(self.x - 9, self.y -9)
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(18)
            turtle.left(90)
        turtle.end_fill()

class food:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.state = "ON"

    def changelocation(self):
        self.x = random.randint(0,20)*20 - 200
        self.y = random.randint(0,20)*20 - 200
        if (self.x, self.y) in game.snake.currentbody:
            self.changelocation()

    def drawself(self,turtle):
        if self.state == "ON":
            turtle.goto(self.x - 9, self.y -9)
            turtle.begin_fill()
            for i in range(4):
                turtle.forward(18)
                turtle.left(90)
            turtle.end_fill()

    def changestate(self):
        if self.state == "ON":
            self.state = "OFF"
        else:
            self.state = "ON"

class border:

    def __init__(self):
        self.border = []
        self.bordercordinates = []
        self.drawborder()

    def drawborder(self):
        for i in range(23):
            for j in range(23):
                if i==22 or i==0 or j==0 or j==22:
                    self.border.append(square(i*20-220,j*20-220))
                    self.bordercordinates.append((i*20-220,j*20-220))

    def drawself(self, turtle):
        for segment in self.border:
            segment.drawself(turtle)

class snake:

    def __init__(self):
        self.headposition = [20, 0]
        self.body = [square(-20,0), square(0, 0), square(20,0)]
        self.currentbody = [(-20,0),(0,0),(20,0)]
        self.nextX = 1
        self.nextY = 0
        self.crashed = False
        self.nextposition = [self.headposition[0] + 20*self.nextX,
                             self.headposition[1] + 20*self.nextY]

    def moveOneStep(self):

        if (self.nextposition[0], self.nextposition[1]) in self.currentbody:
            self.crashed = True
        elif (self.nextposition[0], self.nextposition[1]) in game.border.bordercordinates:
            self.crashed = True
        else:
            self.body.append(square(self.nextposition[0], self.nextposition[1]))
            self.currentbody.append((self.nextposition[0], self.nextposition[1]))
            del self.body[0]
            del self.currentbody[0]
            self.headposition[0], self.headposition[1] = self.body[-1].x, self.body[-1].y
            self.nextposition = [self.headposition[0] + 20*self.nextX,
            self.headposition[1] + 20*self.nextY]

    def moveup(self):
        if self.nextY != -1:
            self.nextX = 0
            self.nextY = 1

    def moveleft(self):
        if self.nextX != 1:
            self.nextX = -1
            self.nextY = 0

    def moveright(self):
        if self.nextX != -1:
            self.nextX = 1
            self.nextY = 0

    def movedown(self):
        if self.nextY != 1:
            self.nextX = 0
            self.nextY = -1

    def eatFood(self):
        self.body.append(square(self.nextposition[0], self.nextposition[1]))
        self.currentbody.append((self.nextposition[0], self.nextposition[1]))
        self.headposition[0], self.headposition[1] = self.body[-1].x, self.body[-1].y
        self.nextposition = [self.headposition[0] + 20*self.nextX,
                             self.headposition[1] + 20*self.nextY]

    def drawself(self, turtle):
        for segment in self.body:
            if segment.x == self.headposition[0] and segment.y == self.headposition[1] :
                turtle.fillcolor("red")
                segment.drawself(turtle)
                turtle.fillcolor("green")
            else:
                segment.drawself(turtle)

class Game:

    def __init__(self):
        self.screen = turtle.Screen()
        self.artist = turtle.Turtle()
        self.artist.up()
        self.artist.hideturtle()
        self.border = border()
        self.snake = snake()
        self.food = food(100, 0)
        self.counter = 0
        self.commandpending = False
        self.screen.bgcolor("blue")
        self.screen.title("Snake")
        self.artist.fillcolor("green")
        self.pause = False
        self.score = 0

    def nextFrame(self):
        while not self.snake.crashed:
            game.screen.listen()
            game.screen.onkey(game.snakedown, "Down")
            game.screen.onkey(game.snakeup, "Up")
            game.screen.onkey(game.snakeleft, "Left")
            game.screen.onkey(game.snakeright, "Right")
            game.screen.onkey(game.pausepressed, "space")
            turtle.tracer(0)
            self.artist.clear()
            if (self.snake.nextposition[0], self.snake.nextposition[1]) == (self.food.x, self.food.y):
                self.snake.eatFood()
                self.score += 1
                self.food.changelocation()
            else:
                self.snake.moveOneStep()
            self.food.changestate()
            self.food.drawself(self.artist)
            self.snake.drawself(self.artist)
            self.artist.fillcolor("red")
            self.border.drawself(self.artist)
            self.artist.fillcolor("green")
            turtle.clear()
            turtle.tracer(0)
            turtle.hideturtle()
            turtle.color("white")
            turtle.penup()
            turtle.setposition(300,300)
            turtle.write("Score: " + str(self.score), False, align = "right", font = ("Arial", 14, "normal"))
            turtle.update()
            self.commandpending = False
            time.sleep(0.1)

    def snakeup(self):
        if not self.commandpending:
            self.snake.moveup()
            self.commandpending = True

    def snakedown(self):
        if not self.commandpending:
            self.snake.movedown()
            self.commandpending = True

    def snakeleft(self):
        if not self.commandpending:
            self.snake.moveleft()
            self.commandpending = True

    def snakeright(self):
        if not self.commandpending:
            self.snake.moveright()
            self.commandpending = True

    def pausepressed(self):
        self.pause = True
        while self.pause == True:
            unpause = self.screen.textinput("Game Paused","Press r to resume ")
            if unpause == 'r':
                self.pause = False

    def highscore(self):
        highscores = open("highscores.csv")
        newhighscores = open("newhighscores.csv",'w+')
        newhighscore = False
        print('Top 10 Highscores: \n')
        n=0
        for line in highscores:
            comma = False
            i = 0
            highscore = ''
            while comma == False:
                if line[i]==' ':
                    comma = True
                else:
                    highscore = highscore + line[i]
                i+=1
            if self.score > int(highscore) and newhighscore == False:
                newhighscore = True
                player_name = game.screen.textinput('You have scored a new high!','Enter your name below')
                newhighscores.write(str(self.score) + ' , ' + player_name + '\n')
                newhighscores.write(line)
                print(str(self.score) + ' , ' + player_name + '  <-- NEW!!!\n')
                print(line)
            elif n<9:
                newhighscores.write(line)
                print(line)
            n += 1
        if newhighscore == True:
            os.remove("highscores.csv")
            os.rename("newhighscores.csv","highscores.csv")
        else:
            os.remove("newhighscores.csv")



game = Game()
play = 'y'
while play == 'y':
    game.nextFrame()
    game.highscore()
    play = game.screen.textinput("GAME OVER!","Enter y to play again.")
    game.snake.__init__()
    game.food.changelocation()
    game.score = 0
#game.screen.mainloop()
