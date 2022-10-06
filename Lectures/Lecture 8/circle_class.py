import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        if self.radius < 0:
            raise ValueError("can only use non-negative radius")
    
        return math.pi * self.radius ** 2
