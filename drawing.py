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
         if(i > 90):
            i = 50
         x = int(360/i)
         for j in range (x + 2):
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
        

    def stickman(self):
        self.mammal.setheading(360)
        self.mammal.circle(30)
        self.mammal.right(90)
        self.mammal.forward(65)
        self.mammal.right(130)
        self.mammal.forward(70)
        self.mammal.backward(70)
        self.mammal.right(120)
        self.mammal.forward(70)
        self.mammal.backward(70)
        self.mammal.right(63)
        self.mammal.forward(65)
        self.mammal.backward(65)
        self.mammal.left(50)
        self.mammal.right(120)
        self.mammal.forward(65)

    def move(self, x: int = 0, y: int = 0):
        self.mammal.penup()
        self.mammal.goto(x,y)
        self.mammal.pendown()


if __name__ == '__main__':
    d = drawing()
    d.move(-170,50)
    d.triangle()
    d.move(10,50)
    d.circle(100)
    d.move(90,70)
    d.diamond()
    d.move(-50.-50)
    d.square()
    d.move(150,95)
    d.stickman()
    turtle.done()
    time.sleep(10)
    
