import turtle
import time

class drawing:
    def __init__(self):
        self.mammal = turtle.Turtle()
        pass

    def triangle(self):
        self.mammal.forward(50)
        self.mammal.right(120)
        self.mammal.forward(50)
        self.mammal.right(120)
        self.mammal.forward(50)
        self.mammal.right(120)
        pass

    def square(self):
        pass

    def circle(self):
        for i in range (50):
            self.mammal.right(10)
            self.mammal.forward(10)
        

    def diamond(self):
        pass

    def move(self, x: int = 0, y: int = 0):
        self.mammal.penup()
        self.mammal.goto(x,y)
        self.mammal.pendown()


if __name__ == '__main__':
    d = drawing()
    d.move(-50,50)
    d.triangle()
    d.move(50,50)
    d.circle()
    d.move(-50,-50)
    d.diamond()
    d.move(50,-50)
    d.square()
    turtle.done()
    time.sleep(10)
    
