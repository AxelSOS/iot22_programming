import math

# Funktion som beräknar arean av en cirkel
def area(radius):
    """Calculate the area of a circle
    
    Arguments:
    radius: radius of the circle"""
    
    return math.pi * (radius**2)


# Funktion som beräknar omkretsen av en cirkel
def circumference(radius):
    """Calculate the circumference of a circle"""
    return math.pi * 2 * radius

# Funktion som beräknar diametern av en cirkel
def diameter(radius):
    """Calculate the diamater of a circle"""
    return radius * 2


# print("__name__ från circle.py:", __name__)  # "Dunder"

def main():
    # Tester av funktionerna
    print("Tests:")
    print("Area(1) == Pi:", area(1) == math.pi)
    print("Circumference(2) == math.pi * 2 * 2:", circumference(2) == math.pi * 2 * 2)
    print("Diameter(5) == 10:", diameter(5) == 10)


if __name__ == '__main__':
    main()
