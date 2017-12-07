from Tkinter import *
import pygame
import Canvas

#colors
WHITE = (255, 255, 255)

class Menu: 
    def __init__(self, canvas): 
        self.win = Tk()
        self.canvas = canvas

        #variable options for the program
        self.colored = IntVar()
        self.ground = IntVar()
        self.tree_num = IntVar()

        Checkbutton(self.win,  variable=self.colored).grid(row=1, column=0)
        Checkbutton(self.win, variable=self.ground).grid(row=2, column=0)
        Scale(self.win, variable=self.tree_num, orient=HORIZONTAL, from_=0, to=10).grid(row=3, column=0)
        Button(self.win, text="ENTER", command=self.submit_callback).grid(row=4, column=0, columnspan=2)

        #label the options
        Label(self.win, text="Options").grid(row=0, column=0, columnspan=2)
        Label(self.win, text="Colored?").grid(row=1, column=1)
        Label(self.win, text="Ground?").grid(row=2, column=1)
        Label(self.win, text="Number of trees").grid(row=3, column=1)
        
    
    def submit_callback(self): 
        #write options to file
        myfile = open("options.txt", "w")
        myfile.write(str(self.colored.get()) + "\n")
        myfile.write(str(self.ground.get()) + "\n")
        myfile.write(str(self.tree_num.get()) + "\n")
        myfile.close()

        #fill the canvas the canvas
        self.canvas.clear()
        self.canvas.update(myfile) 

def main():
    pygame.init()
    #make screen
    size = (1074, 818)
    screen = pygame.display.set_mode(size)
    screen.fill(WHITE)
    pygame.display.update()

    canvas = Canvas.Canvas(screen, WHITE, (25, 25), 1024, 768)
    menu = Menu(canvas)
   
    mainloop()
if __name__ == "__main__": main()
