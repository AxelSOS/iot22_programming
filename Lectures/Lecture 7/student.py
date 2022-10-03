# Klass: Person
# - Förnamn
# - Efternamn
# - Födelseår

class Person:
    def __init__(self, firstname, lastname, birthyear):
        self.firstname = firstname
        self.lastname = lastname
        self.birthyear = birthyear

class Employee(Person):
    pass

# Klass: Student
# - Student-id
# - Student-email

class Student(Person):
    def __init__(self, firstname, lastname, birthyear, student_id, student_email):
        super().__init__(firstname, lastname, birthyear)
        
        self.student_id = student_id
        self.student_email = student_email
    
    # En klass-metod som skapar en Person, men med ålder (år) istället för födelseår
    @classmethod
    def from_age(cls, firstname, lastname, age, student_id, student_email):
        return cls(firstname, lastname, birthyear=2022-age, student_id, student_email)


if __name__ == '__main__':
    s1 = Student('Andreas', 'Nilsson Ström', 1985, 1, 'andreas.nilssonstrom@kyh.se')
    s2 = Student.from_age('Ivar', 'Andersson', 41, 2, 'ivar.andersson@kyh.se')
    
    print(f"{s1.firstname}: Email - {s1.student_email}, Birthyear: {s1.birthyear}")
    print(f"{s2.firstname}: Email - {s2.student_email}, Birthyear: {s2.age}")
        