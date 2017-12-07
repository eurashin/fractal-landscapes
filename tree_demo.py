import pygame
import Tree
import math
import Land
import random
pygame.init()

size = (800, 800)
screen = pygame.display.set_mode(size)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

done = False
screen.fill(WHITE)

pygame.draw.polygon(screen, BLACK, [(200, 300), (225,200), (200,100), (175,200)])
pygame.draw.polygon(screen, BLACK, [(200, 225), (300,200), (200,175), (100,200)])
        
while not done: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
    pygame.display.update()

pygame.quit()
