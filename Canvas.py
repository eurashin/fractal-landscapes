import pygame
import numpy
import Tree
import math
import Land
import random
import Canvas

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (30, 86, 36)

class Canvas: 
    def __init__(self, screen, color, corner1, width, height):
        self.x = corner1[0] 
        self.screen = screen
        self.y = corner1[1] + height
        self.width = width
        self.height = height          

        pygame.draw.rect(screen, (0,0,0), (corner1[0], corner1[1], width, height), 1)

    def update(self,  textfile): 
        myfile = open(textfile, "r")
   
        #get info
        is_land = int(myfile.readline())
        colorls = myfile.readline().split()
        color_land = (int(colorls[0]), int(colorls[1]), int(colorls[2]))
        
        num_basic = int(myfile.readline())
        colorls = myfile.readline().split()
        color_basic = (int(colorls[0]), int(colorls[1]), int(colorls[2]))
        
        num_flower = int(myfile.readline())
        colorls = myfile.readline().split()
        color_flower_bark = (int(colorls[0]), int(colorls[1]), int(colorls[2]))
        colorls = myfile.readline().split()
        color_flowers = (int(colorls[0]), int(colorls[1]), int(colorls[2]))
        
        num_pine = int(myfile.readline())
        colorls = myfile.readline().split()
        color_pine_bark = (int(colorls[0]), int(colorls[1]), int(colorls[2]))
        colorls = myfile.readline().split()
        color_pine = (int(colorls[0]), int(colorls[1]), int(colorls[2]))
       
        ranperm = [0 for i in range(num_basic)] + [1 for i in range(num_flower)] + [2 for i in range(num_pine)]
        ranperm = numpy.random.permutation(ranperm)
        increment = self.width/(num_flower + num_basic + num_pine + 1)
        #draw land
        if(is_land == 1):
            #draw land
            land = Land.Land(self.screen, color_land, (self.x, self.y - 100), (self.x + self.width, self.y - 100), self.height) 
            land.draw(self.x, self.y, self.width, self.height)
            place = self.x+increment
            for i in range(num_basic + num_flower + num_pine):
                if(ranperm[i] == 0): 
                    #draw basic trees
                    mytree = Tree.Tree(self.screen, color_basic)
                    mytree.draw((place, land.gety(place)), 300, 4, 0, 0, (0,0,0))
                elif(ranperm[i] == 1):  
                    #draw flower trees
                    mytree = Tree.Tree(self.screen, color_flower_bark)
                    mytree.draw((place, land.gety(place)), 300, 4, 0, 1, color_flowers)
                else: #pine trees 
                    mytree = Tree.Tree(self.screen, color_pine_bark)
                    mytree.draw((place, land.gety(place)), 400, 4, 0, 2, color_pine)
                
                place = place + increment
                    
                
        else:
            place = self.x+increment
            for i in range(num_basic + num_flower + num_pine): 
                if(ranperm[i] == 0): 
                    #draw basic trees
                    mytree = Tree.Tree(self.screen, color_basic)
                    mytree.draw((place, self.height), 200, 4, 0, 0, (0,0,0))
                elif(ranperm[i] == 1):
                    #draw flower trees
                    mytree = Tree.Tree(self.screen, color_flower_bark)
                    mytree.draw((place, self.height), 300, 4, 0, 1, color_flowers)
                else:
                    #pine trees
                    mytree = Tree.Tree(self.screen, color_pine_bark)
                    mytree.draw((place, self.height), 400, 4, 0, 2, color_pine)
                    
                place = place + increment
            

        pygame.display.update()

    def clear(self): 
        self.screen.fill(WHITE)
        pygame.display.update()
