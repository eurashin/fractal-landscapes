from Tkinter import *
import pygame
import Canvas
from PIL import ImageTk, Image
import tkFont
from tkColorChooser import askcolor

#colors
WHITE = (255, 255, 255)
COLOR_NUM = 6
class Menu: 
    def __init__(self, canvas): 
        self.win = Tk()
        self.canvas = canvas

        #variable options for the program
        self.type = IntVar()
        #custom variables
        self.ground = IntVar()
        self.flower_tree_num = IntVar()
        self.basic_tree_num = IntVar()
        self.pine_num = IntVar()
        self.colors = [(0,0,0) for i in range(COLOR_NUM)]
        self.button_colors = [0 for i in range(COLOR_NUM)]

        #titles
        title_font = tkFont.Font(size=22)
        label_font = tkFont.Font(size=16)
        text_font = tkFont.Font(size=14)
        Label(self.win, text="Options", font=title_font).grid(row=0, column=0, columnspan = 12)

        #overall design options
        Label(self.win, text="Landscape type", font=label_font).grid(row=1, column=0, columnspan=12)
        Radiobutton(self.win, width=16, height=2, variable=self.type, font=text_font, indicatoron=0, text="Black and White", value=3, command=self.custom_callback).grid(row=2, column=0, columnspan=6)
        Radiobutton(self.win, width=16, height=2, variable=self.type, font=text_font, indicatoron=0, text="Custom", value=4, command=self.custom_callback).grid(row=2, column=6, columnspan=6)
       
        #ground options
        Label(self.win, text="Land", font=label_font).grid(row=3, column=0, columnspan=12)
        Label(self.win, text="Ground?", font = text_font).grid(row=4, column=5)
        Checkbutton(self.win, variable=self.ground).grid(row=4, column=6)
        Label(self.win, text="Color", font=text_font).grid(row=5, column=5)
        self.button_colors[0] = Button(self.win, command=lambda: self.getcolor(0), state=DISABLED)
        self.button_colors[0].grid(row=5, column=6)

        #tree options
        Label(self.win, text="Trees", font=label_font).grid(row=6, column=0, columnspan=8)
        Label(self.win, text="Branched", font=text_font).grid(row=7, column=0, columnspan=4)
        basic_img = ImageTk.PhotoImage(Image.open("basic-tree.png"))
        basicl = Label(self.win, image = basic_img)
        basicl.image = basic_img
        basicl.grid(row=8, column=0, rowspan=2, columnspan=4)
        self.button_colors[1] = Button(self.win, command=lambda: self.getcolor(1), state=DISABLED)
        self.button_colors[1].grid(row=10, column=0, columnspan=4)
        Scale(self.win, variable=self.basic_tree_num, orient=HORIZONTAL, from_=0, to=10).grid(row=11, column=0, columnspan=4)
        
        
        Label(self.win, text="Flowering", font=text_font).grid(row=7, column=4, columnspan=4)
        flower_img = ImageTk.PhotoImage(Image.open("flower-tree.png"))
        flowerl = Label(self.win, image = flower_img)
        flowerl.image = flower_img
        flowerl.grid(row=8, column=4, rowspan=2, columnspan=4)
        self.button_colors[2] = Button(self.win, command=lambda: self.getcolor(2), state=DISABLED)
        self.button_colors[2].grid(row=10, column=4, columnspan=2)
        self.button_colors[3] = Button(self.win, command=lambda: self.getcolor(3), state=DISABLED)
        self.button_colors[3].grid(row=10, column=6, columnspan=2)
        Scale(self.win, variable=self.flower_tree_num, orient=HORIZONTAL, from_=0, to=11).grid(row=11, column=4, columnspan=4)
        
       
        Label(self.win, text="Pine", font=text_font).grid(row=7, column=8, columnspan=4)
        pine_img = ImageTk.PhotoImage(Image.open("pine.png"))
        pinel = Label(self.win, image = pine_img)
        pinel.image = pine_img
        pinel.grid(row=8, column=8, rowspan=2, columnspan=4)
        self.button_colors[4] = Button(self.win, command=lambda: self.getcolor(4), state=DISABLED)
        self.button_colors[4].grid(row=10, column=8, columnspan=2)
        self.button_colors[5] = Button(self.win, command=lambda: self.getcolor(5), state=DISABLED)
        self.button_colors[5].grid(row=10, column=10, columnspan=2)
        Scale(self.win, variable=self.pine_num, orient=HORIZONTAL, from_=0, to=11).grid(row=11, column=8, columnspan=4)
        #submit button
        Button(self.win, text="ENTER", font = label_font, height = 2, width = 15, command=self.submit_callback).grid(row=20, column=0, columnspan=12)
    
    def custom_callback(self):
        if(self.type.get() == 4): #user can choose colors 
            for i in range(COLOR_NUM): 
                self.button_colors[i].config(state = "normal", bg="#000000")
        else: 
            for i in range(COLOR_NUM):
                self.colors[i] = (0,0,0)
                self.button_colors[i].config(state = "disabled", bg="#ffffff")

    def getcolor(self, index): 
        prev_color = self.colors[index]
        self.colors[index] = askcolor()[0]
        if(self.colors[index] == None): #if cancelled
            self.colors[index] = prev_color 
        self.button_colors[index].config(bg = "#%02x%02x%02x"%(self.colors[index][0],self.colors[index][1],self.colors[index][2]))



    def submit_callback(self): 
        #write options to file
        myfile = open("options.txt", "w")
        #ground
        myfile.write(str(self.ground.get()) + "\n")
        myfile.write("%d %d %d\n"%(self.colors[0][0], self.colors[0][1], self.colors[0][2]))
        #trees
        myfile.write(str(self.basic_tree_num.get()) + "\n")
        myfile.write("%d %d %d\n"%(self.colors[1][0], self.colors[1][1], self.colors[1][2]))
        myfile.write(str(self.flower_tree_num.get()) + "\n")
        myfile.write("%d %d %d\n"%(self.colors[2][0], self.colors[2][1], self.colors[2][2]))
        myfile.write("%d %d %d\n"%(self.colors[3][0], self.colors[3][1], self.colors[3][2]))
        myfile.write(str(self.pine_num.get()) + "\n")
        myfile.write("%d %d %d\n"%(self.colors[4][0], self.colors[4][1], self.colors[4][2]))
        myfile.write("%d %d %d\n"%(self.colors[5][0], self.colors[5][1], self.colors[5][2]))
        myfile.close()

        #fill the canvas the canvas
        self.canvas.clear()
        self.canvas.update("options.txt") 

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
