import pygame
class Canvas: 
    def __init__(self, screen, color, corner1, width, height):
        self.x = corner1[0] 
        self.y = corner1[1] + height
        self.width = width
        self.height = height          

        pygame.draw.rect(screen, (0,0,0), (corner1[0], corner1[1], width, height), 1)

        
