import pygame
import math
def draw_lines(array, screen, color, point1, point2, thickness):
        #solve line equation
        if(point1[0] == point2[0]): #vertical line
            unit_vector = (1, 0)
        else: 
            m = (point1[1] - point2[1])/(point1[0] - point2[0])
            b = (point1[1] - (m * point1[0]))
            if(m == 0): #horizontal line
                unit_vector = (0, 1)
            else: #avoid divide by zero 
                #solve for perpendicular line equation
                pm = float(-1/m)
                pb = point1[1] - (pm * point1[0])
                #find another point on perpendicular line
                x2 = 2 
                y2 = (pm * x2) + pb
                #find the unit vector
                vector = (point1[0] - x2, point1[1] - y2)
                vector_length = math.sqrt((vector[0] * vector[0]) + (vector[1] * vector[1]))
                unit_vector = (vector[0]/vector_length, vector[1]/vector_length)

        #draw line between two points
        if(point1[0] == point2[0] or m == 0): #vert or hor
            length = math.sqrt(math.pow((point2[0] - point1[0]), 2) + math.pow((point2[1] - point1[1]), 2))
        else:
            length = abs(point2[0] - point1[0])
        
        increment = float(length / len(array))

        point_arr = [[0, 0] for i in range(len(array))]
        for i in range(len(array) - 1):
            if(point1[0] == point2[0]): #vertical
                if(point1[1] > point2[1]): #point 1 is lower
                    x =  point1[0]
                    y = (i * increment) + point2[1] 
                    x2 = point2[0]
                    y2 = (i+1) * increment + point2[1]
                else:
                    x =  point1[0]
                    y = (i * increment) + point1[1] 
                    x2 = point2[0]
                    y2 = (i+1) * increment + point1[1]

            else:
                if(point1[0] < point2[0]): 
                    x = (i * increment) + point1[0]
                    y = (m * x) + b
                    x2 = (i+1) * increment + point1[0]
                    y2 = m * x2 + b
                else: 
                    x = -((i * increment) - point1[0])
                    y = ((m * x) + b)
                    x2 = -((i+1) * increment - point1[0])
                    y2 = (m * x2 + b)


            #the array is the displacement perpendicular from the line
            scaled_v = (unit_vector[0] * array[i], unit_vector[1] * array[i])
            scaled_v2 = (unit_vector[0] * array[i+1], unit_vector[1] * array[i+1]) 
            xn = x + scaled_v[0] 
            yn = y + scaled_v[1]
            xn2 = x2 + scaled_v2[0] 
            yn2 = y2 + scaled_v2[1]

            point_arr[i][0] = xn
            point_arr[i][1] = yn
            point_arr[i+1][0] = xn2
            point_arr[i+1][1] = yn2

            pygame.draw.line(screen, color, (xn, yn),(xn2, yn2), int(thickness))
        return(point_arr)
