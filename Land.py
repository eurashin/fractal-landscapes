import pygame
import random
import math
import fractal_tools
import pygame_tools

class Land: 
    def __init__(self, screen, color, point1, point2, canvas_height): 
        self.screen = screen
        self.color = color
        self.num_steps = 100
        self.terrain = [0 for i in range(self.num_steps)]
        self.displacement = 100
        self.roughness = 0.5
        self.point1 = point1
        self.point2 = point2
        self.array = [[0,canvas_height] for i in range(self.num_steps)]

    def draw(self, canvas_x, canvas_y, canvas_width, canvas_height):
        fractal_tools.random_koch(0, self.num_steps-1, self.displacement, self.roughness, self.terrain) 
        self.array = pygame_tools.draw_lines(self.terrain, self.screen, self.color, self.point1, self.point2, 4) 

        #insert endpoints for fill
        self.array.insert(0, [canvas_x, canvas_y])
        self.array.insert(len(self.array), [canvas_x + canvas_width, self.array[len(self.array)-1][1]])
        self.array.insert(len(self.array), [canvas_x + canvas_width, canvas_y])
        pygame.draw.polygon(self.screen, self.color, self.array)


    def gety(self, x): 
        width = abs(self.point1[0] - self.point2[0]) #length of x
        increment = width/self.num_steps; 

        index = x/increment
        
        if(index > 0 and index < len(self.array)):
            y = self.array[index][1]
        else: 
            y = 0
        
        return(y+9)
