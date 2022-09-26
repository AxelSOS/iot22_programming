import circle  # Circle är en modul
from circle import area as c_area  # Döp om area-funktionen p.g.a namn-kollision
from square import area, my_magic_number
import square

import circle as c



# print("__name__ från Lektion 5.py:", __name__)

def main():
    print("Circle.area():", c.area(1.1))
    print("Circle.circumference():", circle.circumference(1.1))
    print("Circle.diameter():", circle.diameter(1.1))
    
    print(c_area(1.1))
    print(area(1.1))
    print(my_magic_number)
          
    print("Square.area():", square.area(1.1))
    print("Square.circumference():", square.circumference(1.1))

if __name__ == '__main__':
    main()
