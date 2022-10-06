import circle_class
import math

# Testa att skapa en instans av klassen
def test_create_circle():
    c = circle_class.Circle(5)
    assert c.radius == 5


def test_circle_area():
    c = circle_class.Circle(2)
    assert c.area() == math.pi * 2**2
    