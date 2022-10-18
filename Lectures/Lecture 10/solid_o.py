# Exempel på dålig kod

"""
class Animal:
    def __init__(self, name):
        self.name = name
    
        
animals = [
    Animal("cat"),
    Animal("dog"),
    Animal("mouse")
    ]


def animal_sound(animals):
    for animal in animals:
        if animal.name == "cat":
            print("meow")
            
        elif animal.name == "dog":
            print("woof")
            
        elif animal.name == "mouse":
            print("squeek")


animal_sound(animals)
"""

class Animal:
    def __init__(self, name):
        self.name = name
        
    def make_sound(self):
        pass
    
class Cat(Animal):
    def make_sound(self):
        return "meow"
    
class Dog(Animal):
    def make_sound(self):
        return "woof"

class Mouse(Animal):
    def make_sound(self):
        return "squeek"

class Snake(Animal):
    def make_sound(self):
        return "hisssss"

animals = [
    Cat("cat"),
    Dog("dog"),
    Mouse("mouse"),
    Snake("snake")
    ]

# Denna metod fungerar nu bättre enligt Open-Closed-principen:
# Vi behöver inte förändra den för att bygga ut antalet djur
def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())


animal_sound(animals)
