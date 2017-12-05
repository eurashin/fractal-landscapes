import pygame
import random
import math
import fractal_tools
import pygame_tools

class Land: 
    def __init__(self, screen, color, point1, point2): 
        self.screen = screen
        self.color = color
        self.num_steps = 100
        self.terrain = [0 for i in range(self.num_steps)]
        self.displacement = 100
        self.roughness = 0.5
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas_x, canvas_y, canvas_width, canvas_height):
        fractal_tools.random_koch(0, self.num_steps-1, self.displacement, self.roughness, self.terrain) 
        array = pygame_tools.draw_lines(self.terrain, self.screen, self.color, self.point1, self.point2, 4) 

        #insert endpoints for fill
        array.insert(0, [canvas_x, canvas_y])
        array.insert(len(array), [canvas_x + canvas_width, array[len(array)-1][1]])
        array.insert(len(array), [canvas_x + canvas_width, canvas_y])
        pygame.draw.polygon(self.screen, self.color, array)

