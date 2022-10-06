# circle.py
import math

def area(radius):
    if radius < 0:
        raise ValueError("can only use non-negative radius")
    
    return math.pi * radius ** 2
    #return math.pi

def diameter(radius):
    return radius * 2
    #return 4

