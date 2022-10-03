from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

@dataclass
class Astronaut(Person):
    primary_skill: str
    email: str


p1 = Person('Teddy Sanders', 62)
print(p1)

a1 = Astronaut(name='Mark Watney', age=42, primary_skill='Botany', email='mark.watney@nasa.gov')
print(a1)
