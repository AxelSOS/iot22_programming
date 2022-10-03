# Exempel på en "Man"-klass som ärver från "Person"-klassen

class Person:
    # Exempel på "type-annotation" i Python
    # Hjälp användaren på traven genom att säga vilka typer de olika fälten ska ha
    def __init__(self, name: str, birthyear: int = 1990):
        self.name = name
        self.birthyear = birthyear
        
    @classmethod
    def from_age(cls, name: str, age: int):
        """Return a Person object, constructed from Age
        """
        return cls(name, 2022-age)
    
    # __str__ anropas när man gör str(obj) eller print(obj)
    def __str__(self):
        return f' Name: {self.name}, Birthyear: {self.birthyear}'
        

class Man(Person):
    gender = 'Male'
    
    def __str__(self):
        # Använd Persons __str__ för att bygga vidare
        return super().__str__() + f', Gender: {self.gender}'
        
    
person1 = Person('Jessica', 1991)
# När vi har implementerat __str__ i klassen så kan vi använda print().
# Annars används pythons standard-__str__ som inte är så snygg
print(person1)

man1 = Man('John', 1985)
print(man1)

man2 = Man.from_age('Jim', 28)
print(man2)



"""
print("Man1:")
man1 = Man('John', 1985)
print(man1.name, man1.birthyear)
print(isinstance(man1, Man))
print(isinstance(man1, Person))

print()

print("Man2:")
man2 = Man.from_age('Jim', 28)
print(man2.name, man2.birthyear)
print(isinstance(man2, Man))
print(isinstance(man2, Person))

print()

print("Person1:")
person1 = Person('Jessica', 1991)
print(person1.name, person1.birthyear)
print(isinstance(person1, Man))
print(isinstance(person1, Person))

print(person1)
"""