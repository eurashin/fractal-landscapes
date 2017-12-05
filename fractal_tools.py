import math
import random
#returns randomized koch curve
def random_koch(left, right, displacement, roughness, array):
    if((left + 1) == right):
        return
    mid = int((left + right)/2)
    change  = ((random.random() * 2) - 1) * displacement
    array[mid] = ((array[left] + array[right])/2 + change)
    displacement = displacement * roughness
   
    random_koch(left, mid, displacement, roughness, array)
    random_koch(mid, right, displacement, roughness, array)
