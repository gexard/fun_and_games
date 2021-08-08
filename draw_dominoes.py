import turtle

class square:
    
    def __init__(self, x, y, dots, size):
        self.x = x
        self.y = y
        self.size = size

    def draw_square(self, turtle):
        turtle.goto(self.x - self.size - 1, self.y - self.size - 1)
        turtle.fillcolor("white")
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(2 * (size - 1))
            turtle.left(90)
        turtle.end_fill()

    def draw_dot(self, x, y):
        turtle.goto(self.x + x, self.y + y)
        turtle.fillcolor("black")
        turtle.begin_fill()


class Game:

    def __init__(self):
        self.screen = turtle.Screen()
        self.artist = turtle.Turtle()
        self.artist.up()
        self.artist.hideturtle()
        self.piece = square(0,0,1,50)
        self.screen.title("Dominoes")
        self.screen.bgcolor("blue")

game = Game()
while True:
    pass
