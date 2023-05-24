from turtle import *

class ascii_art:

    def __init__(self):
        self.desc = ""

    def draw_square(self):
        print ("---------")
        print("|         |")
        print("|         |")
        print("|         |")
        print("|         |")
        print ("---------")
        pass

    def draw_triangle(self):
        for i in range(10):
            print("*" * i)
        
    def draw_circle():
        pass

if __name__ == '__main__':
    art = ascii_art()
    art.draw_triangle()
    art.draw_square()



