import math

class Circle:
    # Init används för att fylla klassinstanser med initiala värden
    def __init__(self, my_radius=None):
        self.radius = my_radius
        
    # Klassmetod för att skapa cirklar från diameter
    # Kan ta in argument
    # @classmethod säger till python att vi vill skapa nya instanser med denna metod
    @classmethod
    def from_diameter(cls, diameter):
        # cls() anropar klassens __init__-metod
        # __init__ returnerar en instans
        # return gör att vi skickar den instansen till vår anropare
        return cls(diameter / 2)

    # Metod som beräknar arean av en cirkel
    def area(self):
        """Calculate the area of a circle"""
        
        return math.pi * (self.radius**2)


if __name__ == '__main__':
    c1 = Circle(5)
    c2 = Circle(8)
    
    c3 = Circle.from_diameter(12)

    print(c1.radius)
    print(c2.radius)
    print(c3.radius)

    print(c1.area())
    print(c2.area())
    print(c3.area())
