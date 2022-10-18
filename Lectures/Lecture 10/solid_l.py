"""
class Animal:
    def __init__(self, name, nbr_legs):
        self.name = name
        self.nbr_legs = nbr_legs
    
    def leg_count(self):
        pass
    
class Cat(Animal):
    def cat_leg_count(self):
        return self.nbr_legs
    
class Dog(Animal):
    def dog_leg_count(self):
        return self.nbr_legs

class Mouse(Animal):
    def mouse_leg_count(self):
        return self.nbr_legs

class Snake(Animal):
    def snake_leg_count(self):
        return self.nbr_legs

class Sparrow(Animal):
    def sparrow_leg_count(self):
        return self.nbr_legs

animals = [
    Cat("cat", 4),
    Dog("dog", 4),
    Mouse("mouse", 4),
    Snake("snake", 0),
    Sparrow("sparrow", 2)
    ]

def animal_leg_count(animals):
    for animal in animals:
        if isinstance(animal, Cat):
            print(animal.cat_leg_count())
        if isinstance(animal, Dog):
            print(animal.dog_leg_count())
        if isinstance(animal, Mouse):
            print(animal.mouse_leg_count())
        if isinstance(animal, Snake):
            print(animal.snake_leg_count())
        if isinstance(animal, Sparrow):
            print(animal.sparrow_leg_count())

animal_leg_count(animals)
"""

class Animal:
    def __init__(self, name, nbr_legs):
        self.name = name
        self.nbr_legs = nbr_legs
    
    def leg_count(self):
        return self.nbr_legs
    
class Cat(Animal):
    pass
    
class Dog(Animal):
    pass

class Mouse(Animal):
    pass

class Snake(Animal):
    pass

class Sparrow(Animal):
    pass

animals = [
    Cat("cat", 4),
    Dog("dog", 4),
    Mouse("mouse", 4),
    Snake("snake", 0),
    Sparrow("sparrow", 2)
    ]

def animal_leg_count(animals):
    for animal in animals:
        print(animal.leg_count())
        

animal_leg_count(animals)
