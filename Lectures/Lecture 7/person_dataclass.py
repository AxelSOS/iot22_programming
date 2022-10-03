# Implementera våra person-klasser, fast med dataclass istället

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    birthyear: int = 1990

    @classmethod
    def from_age(cls, name: str, age: int):
        """Return a Person object, constructed from Age
        """
        return cls(name, 2022-age)
     

@dataclass
class Man(Person):
    gender = 'Male'


person1 = Person('Jessica', 1991)
print(person1)

man1 = Man('John', 1985)
print(man1)

man2 = Man.from_age('Jim', 28)
print(man2)