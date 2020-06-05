import random
import turtle
import time

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

        if (self.nextposition[0], self.nextposition[1]) not in self.currentbody:
            self.body.append(square(self.nextposition[0], self.nextposition[1]))
            self.currentbody.append((self.nextposition[0], self.nextposition[1]))
            del self.body[0]
            del self.currentbody[0]
            self.headposition[0], self.headposition[1] = self.body[-1].x, self.body[-1].y
            self.nextposition = [self.headposition[0] + 20*self.nextX,
                                 self.headposition[1] + 20*self.nextY]
        else:
            self.crashed = True
            print("you crashed")

    def moveup(self):
        self.nextX = 0
        self.nextY = 1

    def moveleft(self):
        self.nextX = -1
        self.nextY = 0

    def moveright(self):
        self.nextX = 1
        self.nextY = 0

    def movedown(self):
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
            segment.drawself(turtle)

class Game:

    def __init__(self):
        self.screen = turtle.Screen()
        self.artist = turtle.Turtle()
        self.artist.up()
        self.artist.hideturtle()
        self.snake = snake()
        self.food = food(100, 0)
        self.counter = 0
        self.commandpending = False
        self.screen.bgcolor("blue")
        self.screen.title("Snake")
        self.artist.fillcolor("green")
        self.pause = False

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
                self.food.changelocation()
            else:
                self.snake.moveOneStep()
            self.food.changestate()
            self.food.drawself(self.artist)
            self.snake.drawself(self.artist)
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
            userinput = self.screen.textinput("Game Paused","Press r to resume ")
            if userinput == 'r':
                self.pause = False




game = Game()
time.sleep(3)
game.nextFrame()
print("GAME OVER!")
game.screen.bye()
#game.screen.mainloop()
