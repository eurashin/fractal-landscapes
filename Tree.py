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
        length = length * 0.4
        thickness = thickness * 0.9
        if(length > 2): 
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

    def random_branch(self, center, olength, thickness, start_theta): #the start theta defines the current planes rotation
        thickness = float(thickness * 0.8)
        num_branch = random.randrange(0,5)
        if(num_branch > 0): 
            interval = float(olength/(num_branch))
        else: 
            interval = 0
        spot = interval
        #make the top branch off many times
        for i in range(random.randrange(1,3)): 
            theta = (float(random.randrange(50,100))/100 *  math.pi/4)
            if(olength > 2): #stop branching
                length = olength * float(random.randrange(50, 70)) / 100
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
        for i in range(num_branch - 1): #randomize the number of branches 
            theta = (float(random.randrange(50,100))/100 *  math.pi/4)
            if(olength > 2): #stop branching
                current_center = (center[0] - spot*math.cos(start_theta), center[1] + spot*math.sin(start_theta))
                spot = spot + interval
                length = olength * float(random.randrange(50, 70)) / 100
                random_bin = random.randrange(0, 2)
                if(random_bin == 1): 
                    new_theta = start_theta - theta
                else: 
                    new_theta = start_theta + theta
                
                #draw branch
                new_point = (current_center[0] + length * math.cos(new_theta), current_center[1] - length * math.sin(new_theta))
                if(length > 30): 
                    array = [0 for i in range(30)] 
                    fractal_tools.random_koch(0, 29, 5, 0.5, array)
                    pygame_tools.draw_lines(array, self.screen, self.color, current_center, new_point, thickness)

                else: 
                    pygame.draw.line(self.screen, self.color, current_center, new_point, int(thickness))
                #continue branch left and right
                self.random_branch(new_point, length, thickness, new_theta)      

    def random_flower(self, center, olength, thickness, start_theta, color): #the start theta defines the current planes rotation
        thickness = float(thickness * 0.8)
        num_branch = random.randrange(0,5)
        if(num_branch > 0): 
            interval = float(olength/(num_branch))
        else: 
            interval = 0
        spot =interval
        #make the top branch off many times
        for i in range(random.randrange(1,3)): 
            theta = (float(random.randrange(50,100))/100 *  math.pi/4)
            if(olength > 2): #stop branching
                length = olength * float(random.randrange(50, 70)) / 100
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
                self.random_flower(new_point, length, thickness, new_theta, color)      
        for i in range(num_branch - 1): #randomize the number of branches 
            theta = (float(random.randrange(50,100))/100 *  math.pi/4)
            if(olength < 2): #stop branching, flower
                self.draw_flower(center, 4, theta, color)
            else: 
                current_center = (center[0] - spot*math.cos(start_theta), center[1] + spot*math.sin(start_theta))
                spot = spot + interval
                length = olength * float(random.randrange(50, 70)) / 100
                random_bin = random.randrange(0, 2)
                if(random_bin == 1): 
                    new_theta = start_theta - theta
                else: 
                    new_theta = start_theta + theta
                
                #draw branch
                new_point = (current_center[0] + length * math.cos(new_theta), current_center[1] - length * math.sin(new_theta))
                if(length > 30): 
                    array = [0 for i in range(30)] 
                    fractal_tools.random_koch(0, 29, 5, 0.5, array)
                    pygame_tools.draw_lines(array, self.screen, self.color, current_center, new_point, thickness)

                else: 
                    pygame.draw.line(self.screen, self.color, current_center, new_point, int(thickness))
                #continue branch left and right
                self.random_flower(new_point, length, thickness, new_theta, color)      
    
    def pine_tree(self, center, olength, thickness, start_theta, color): 
        thickness = 1
        num_branch = random.randrange(8, 10)
        interval = float(olength/(num_branch))
        spot = 0
        current_center = center
        theta = ( math.pi/6)
        new_theta = start_theta - theta
        for i in range(1, num_branch + 1): 
            length = olength * float(i)/num_branch * 0.4
            if(length > 2):
                current_center = (center[0] - spot*math.cos(start_theta), center[1] + spot*math.sin(start_theta))
                spot = spot + interval
                
                #draw branch
                new_point = (current_center[0] + (length * math.cos(new_theta)), current_center[1] - (length * math.sin(new_theta)))
                opposite_new_point = (current_center[0] + (length * math.cos(start_theta + theta)), current_center[1] - (length * math.sin(start_theta + theta)))
                
                if(length < 4): 
                    pygame.draw.line(self.screen, color, current_center, new_point, int(thickness))
                    pygame.draw.line(self.screen, color, current_center, opposite_new_point, int(thickness))
                else: 
                    pygame.draw.line(self.screen, self.color, current_center, new_point, int(thickness))
                    pygame.draw.line(self.screen, self.color, current_center, opposite_new_point, int(thickness))
                
                #continue branch left and right
                self.pine_tree(new_point, length, thickness, new_theta, color)     
                self.pine_tree(opposite_new_point, length, thickness, start_theta + theta, color)    

                                    

    def draw(self, center, length, thickness, theta, tree_type, color):
        #first branch is always straight up (trunk)
        if(theta == 0): #randomize tree
            trunk_length = length * float(random.randrange(40, 100)) / 100

            if(tree_type != 2): 
                two_variation = (float(random.randrange(70, 120))/100 * 2)
                branch_trunk = float((trunk_length)/ two_variation) #branches along top half of trunk
                branchless_trunk = trunk_length - branch_trunk
                num_branch = random.randrange(2,6)
                increment = float(branch_trunk) / num_branch #place branches along trunk on this increment
                for i in range(num_branch): 
                    #50% to 100% of placement
                    percent = float(random.randrange(50, 100)) / 100
                    placement = branchless_trunk + (increment * i * percent)
                    #place random branching along spot on trunk
                    branch_center = (center[0], center[1] - placement)
                    if(tree_type == 0):
                        self.random_branch(branch_center,placement * 0.7, thickness, (math.pi/2))
                    else:
                        self.random_flower(branch_center,placement * 0.7, thickness, (math.pi/2), color)

            
            #top of the tree
            new_center = (center[0], center[1] - trunk_length)
            #draw a rickety trunk
            array = [0 for i in range(30)] 
            fractal_tools.random_koch(0, 29, 5, 0.5, array)
            pygame_tools.draw_lines(array, self.screen, self.color, center, new_center, thickness)
            if(tree_type == 0): #basic 
                self.random_branch(new_center, branch_trunk, thickness, (math.pi/2)) 
            elif(tree_type == 1): #flowering
                self.random_flower(new_center, branch_trunk, thickness, (math.pi/2), color) 
            else: #pine
                self.pine_tree(new_center, trunk_length, thickness, (math.pi/2), color)

        else: #perfect tree
            new_center = (center[0], center[1] - length)
            pygame.draw.line(self.screen, self.color, center, new_center, thickness)
            self.perfect_branch(new_center, length, thickness, (math.pi/2), theta) 


    def draw_flower(self, center, length, angle, color): 
        ll = float(length/2)
        sl = float(length/8)
        part1 = [0 for i in range(4)]
        part2 = [0 for i in range(4)]
        part1[0] =(center[0] + ll*math.cos(angle), center[1] + ll*math.sin(angle)) 
        part1[1] =(center[0] + sl*math.cos(angle + math.pi/2), center[1] +sl*math.sin(angle + math.pi/2))
        part1[2] = (center[0] + ll*math.cos(angle + math.pi), center[1] + ll*math.sin(angle + math.pi))
        part1[3] = (center[0] + sl*math.cos(angle + math.pi*3/2), center[1] + sl*math.sin(angle + math.pi*3/2))
        part2[0] = (center[0] + sl*math.cos(angle), center[1] + sl*math.sin(angle))
        part2[1] = (center[0] + ll*math.cos(angle + math.pi/2), center[1] + ll*math.sin(angle + math.pi/2))
        part2[2] = (center[0] + sl*math.cos(angle + math.pi), center[1] + sl*math.sin(angle + math.pi))
        part2[3] = (center[0] + ll*math.cos(angle + math.pi*3/2), center[1] + ll*math.sin(angle + math.pi*3/2))

        pygame.draw.polygon(self.screen, color, part1)
        pygame.draw.polygon(self.screen, color, part2)


