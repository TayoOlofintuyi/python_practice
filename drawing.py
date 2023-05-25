import turtle

class drawing:
    def __init__(self):
        self.mammal = turtle.Turtle()
        pass

    def triangle(self):
        pass
    def square(self):
        pass
    def circle(self):
        pass
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
        pass

if __name__ == '__main__':
    d = drawing()
    d.diamond()
    turtle.done()