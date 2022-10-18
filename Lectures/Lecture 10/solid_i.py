"""
class Shape:
    def draw_square(self):
        pass
    
    def draw_rectangle(self):
        pass
    
    def draw_circle(self):
        pass
    
    def draw_triangle(self):
        pass
    
    
class Circle(Shape):
    def draw_square(self):
        pass
    
    def draw_rectangle(self):
        pass
    
    def draw_circle(self):
        pass


class Square(Shape):
    def draw_square(self):
        pass
    
    def draw_rectangle(self):
        pass
    
    def draw_circle(self):
        pass
    

class Rectangle(Shape):
    def draw_square(self):
        pass
    
    def draw_rectangle(self):
        pass
    
    def draw_circle(self):
        pass


my_shape = Circle()
my_shape.draw_rectangle()
"""

class Shape:
    def draw(self):
        raise NotImplementedError
    
    
class Circle(Shape):
    def draw(self):
        print("Drawing a circle")


class Square(Shape):
    def draw(self):
        pass
    

class Rectangle(Shape):
    def draw(self):
        pass
    

class Triangle(Shape):
    def draw(self):
        pass


shape1 = Circle()
shape1.draw()

#shape2 = Shape()
#shape2.draw()