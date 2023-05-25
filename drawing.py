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
        
    def square(self):
        self.mammal.forward(50)
        self.mammal.right(90)
        self.mammal.forward(50)
        self.mammal.right(90)
        self.mammal.forward(50)
        self.mammal.right(90)
        self.mammal.forward(50)

    def circle(self, i: int):
         x = int(720/i)
         for i in range (x):
            self.mammal.right(i)
            self.mammal.forward(i)
        
    def diamond(self): 
        self.mammal.right(100)
        self.mammal.forward(90)
        self.mammal.right(-70)
        self.mammal.forward(90)
        self.mammal.right(-100)
        self.mammal.forward(76)
        self.mammal.left(70)
        self.mammal.forward(110)
        self.mammal.left(115)
        self.mammal.forward(55)
        

    def move(self, x: int = 0, y: int = 0):
        self.mammal.penup()
        self.mammal.goto(x,y)
        self.mammal.pendown()


if __name__ == '__main__':
    d = drawing()
    d.move(-50,50)
    d.triangle()
    d.move(50,50)
    d.circle(50)
    d.move(100,70)
    d.diamond()
    d.move(-50.-50)
    d.square()
    turtle.done()
    time.sleep(10)
    
