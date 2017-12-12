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

mytree = Tree.Tree(screen, BLACK)
mytree.draw((200, 500), 400, 4, 0, 2, (0,0,0))
        
while not done: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
    pygame.display.update()

pygame.quit()
