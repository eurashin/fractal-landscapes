import pygame
import Tree
import math
import Land
import random
import Canvas
import pygame

pygame.init()



size = (1100, 1000)
screen = pygame.display.set_mode(size)
screen.fill(WHITE)

canvas = Canvas.Canvas(screen, WHITE, (50, 50), 1000, 900)
land = Land.Land(screen, BLACK, (canvas.x, canvas.y - 100), (canvas.x + canvas.width, canvas.y - 100))
land.draw(canvas.x, canvas.y, canvas.width, canvas.height)
mytree = Tree.Tree(screen, BLACK)
mytree.draw((canvas.x + 200, canvas.y - 100), 300, 4, 0 )

done = False
while not done: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
    pygame.display.update()

pygame.quit()
