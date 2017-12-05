import pygame
import pygame_tools
import fractal_tools
import random
import math

class Tree: 
    def __init__(self, screen, color): 
        self.screen = screen
        self.color = color
    
    def perfect_branch(self, center, length, thickness, start_theta, theta): #the start theta defines the current planes rotation
        length = length * 0.66
        thickness = thickness * 0.9
        if(length > 30): 
            right_theta = start_theta - theta
            left_theta = start_theta + theta

            #draw left and right branch
            right_point = (center[0] + length * math.cos(right_theta), center[1] - length * math.sin(right_theta))
            left_point = (center[0] + length * math.cos(left_theta), center[1] - length * math.sin(left_theta))

            pygame.draw.line(self.screen, self.color, center, right_point, int(thickness))
            pygame.draw.line(self.screen, self.color, center, left_point, int(thickness))
            
            #continue branch left and right
            self.perfect_branch(right_point, length, thickness, right_theta, theta)        
            self.perfect_branch(left_point, length, thickness, left_theta, theta)       

    def random_branch(self, center, length, thickness, start_theta): #the start theta defines the current planes rotation
        thickness = float(thickness * 0.8)
        num_branch = random.randrange(2,4)
        for i in range(num_branch): #randomize the number of branches 
            if(length > 2): 
                length = length * float(random.randrange(50, 80)) / 100
                theta = (float(random.randrange(50,100))/100 *  math.pi/4)
                random_bin = random.randrange(0, 2)
                if(random_bin == 1): 
                    new_theta = start_theta - theta
                else: 
                    new_theta = start_theta + theta
                
                #draw branch
                new_point = (center[0] + length * math.cos(new_theta), center[1] - length * math.sin(new_theta))
                if(length > 30): 
                    array = [0 for i in range(30)] 
                    fractal_tools.random_koch(0, 29, 5, 0.5, array)
                    pygame_tools.draw_lines(array, self.screen, self.color, center, new_point, thickness)

                else: 
                    pygame.draw.line(self.screen, self.color, center, new_point, int(thickness))
                #continue branch left and right
                self.random_branch(new_point, length, thickness, new_theta)       


    def draw(self, center, length, thickness, theta):
        #first branch is always straight up (trunk)
        if(theta == 0): #randomize tree
            trunk_length = length * float(random.randrange(40, 100)) / 100

            two_variation = (float(random.randrange(70, 120))/100 * 3)
            branch_trunk = float((trunk_length * 2)/ two_variation) #branches along top half of trunk
            branchless_trunk = trunk_length - branch_trunk
            num_branch = random.randrange(2, 5)
            increment = float(branch_trunk) / num_branch #place branches along trunk on this increment
            for i in range(num_branch): 
                #50% to 100% of placement
                percent = float(random.randrange(50, 100)) / 100
                placement = branchless_trunk + (increment * i * percent)
                #place random branching along spot on trunk
                branch_center = (center[0], center[1] - placement)
                self.random_branch(branch_center,placement, thickness, (math.pi/2))

            
            #top of the tree
            new_center = (center[0], center[1] - trunk_length)
            #draw a rickety trunk
            array = [0 for i in range(30)] 
            fractal_tools.random_koch(0, 29, 5, 0.5, array)
            pygame_tools.draw_lines(array, self.screen, self.color, center, new_center, thickness)
            self.random_branch(new_center, branch_trunk, thickness, (math.pi/2)) 
        else: #perfect tree
            new_center = (center[0], center[1] - length)
            pygame.draw.line(self.screen, self.color, center, new_center, thickness)
            self.perfect_branch(new_center, length, thickness, (math.pi/2), theta) 





