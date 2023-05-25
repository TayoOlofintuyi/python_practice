
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
        
    def draw_circle(self):
        #for i in range(5):
            #x = 25 - (i * i)
            #print("*" * x)
        print("  _____")
        print(" /     \ ")
        print("(       )")
        print(" \     /")
        print("  ***** ")      

    def draw_diamond(self):
        print ("    *")
        print ("  *****")
        print (" *******")
        print ("*********")
        print (" *******")
        print ("    *")
        pass


if __name__ == '__main__':
    art = ascii_art()
    art.draw_triangle()
    art.draw_square()
    art.draw_diamond()
    art.draw_circle()



