import pygame
import Tree
import math
import Land
import random
import Canvas

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (30, 86, 36)


size = (1500, 1000)
screen = pygame.display.set_mode(size)
screen.fill(WHITE)

canvas = Canvas.Canvas(screen, WHITE, (50, 50), 1000, 900)
land = Land.Land(screen, BLACK, (canvas.x, canvas.y - 100), (canvas.x + canvas.width, canvas.y - 100))
land.draw(canvas.x, canvas.y, canvas.width, canvas.height)
mytree = Tree.Tree(screen, BLACK)
mytree.draw((canvas.x + 200, canvas.y - 100), 200, 4, 0 )

done = False
        
while not done: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
    pygame.display.update()

pygame.quit()
