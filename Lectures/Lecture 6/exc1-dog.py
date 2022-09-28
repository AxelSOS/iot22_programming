# Övning 1: Dog-klassen

class Dog:
    def __init__(self, name, age, breed, sound):
        self.name = name
        self.age = age
        self.breed = breed
        self.sound = sound
    
    def bark(self):
        print(f"{self.name} skäller: {self.sound} {self.sound}")
    
    def age_in_dog_years(self):
        return Dog.human_to_dog_years(self.age)
    
    @staticmethod
    def human_to_dog_years(years):
        return years * 7


if __name__ == '__main__':
    dog1 = Dog(name='Rufus', age=3,
               breed='Border Collie', sound='Woof')
    dog2 = Dog('Pysen', 5, 'Chihuaha', 'Bjäbb')
    
    dog1.bark()
    dog2.bark()
    
    print(dog1.age_in_dog_years())
    print(dog2.age_in_dog_years())
    
    print(Dog.human_to_dog_years(dog1.age))
    