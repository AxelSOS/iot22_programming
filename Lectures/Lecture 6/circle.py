import math

class Circle:
    # Init används för att fylla klassinstanser med initiala värden
    def __init__(self, my_radius=None):
        self.radius = my_radius

    # Metod som beräknar arean av en cirkel
    def area(self):
        """Calculate the area of a circle"""
        
        return math.pi * (self.radius**2)


if __name__ == '__main__':
    c1 = Circle(5)
    c2 = Circle(8)

    print(c1.radius)
    print(c2.radius)

    print(c1.area())
    print(c2.area())
