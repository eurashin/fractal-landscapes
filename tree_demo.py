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
for i in range(4):
    mytree.draw(((i+1) * (800/5), 600 + (random.randrange(-100,100))), 250, 4, 0)

myland = Land.Land(screen, BLACK, (0, 400), (800, 400), 100, 100, 0.5)
myland.draw()
        
while not done: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
    pygame.display.update()

pygame.quit()
