import pygame
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

    def update(self, textfile): 
        land = Land.Land(self.screen, BLACK, (self.x, self.y - 100), (self.x + self.width, self.y - 100))
        land.draw(self.x, self.y, self.width, self.height)
        mytree = Tree.Tree(self.screen, BLACK)
        mytree.draw((self.x + 200, land.gety(self.x+200)), 300, 4, 0 )

        pygame.display.update()

    def clear(self): 
        self.screen.fill(WHITE)
        pygame.display.update()
