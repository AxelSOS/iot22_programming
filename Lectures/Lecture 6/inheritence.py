class Person:
    def __init__(self, name, email, birth_year):
        self.name = name
        self.email = email
        self.birth_year = birth_year
        
    def greet(self):
        print(f"Hejsan, {self.name}")
        

# Employee är en sub-klass till person
# Employee ärver av Person
class Employee(Person):
    def __init__(self, name, email, phone, salary, birth_year):
        super().__init__(name, email, birth_year)
        
        self.phone = phone
        self.salary = salary
    
    @staticmethod
    def deduct_taxes(amount_before_taxes):
        output_salary = amount_before_taxes
        
        output_salary *= 0.7
        
        if amount_before_taxes > 46200:
            # Räkna ut hur mycket vi ligger över den statliga gränsen
            amount_over_limit = amount_before_taxes - 46200

            # Räkna ut hur mycket extra skatt som ska betalas
            extra_taxes = amount_over_limit * 0.2
            
            # Minska lönen med den extra skatten
            output_salary -= extra_taxes
        
        return output_salary
    
    def salary_after_taxes(self):
        return self.deduct_taxes(self.salary)


class HourlyEmployee(Employee):
    def __init__(self, name, email, phone, hourly_salary, birth_year):
        super().__init__(name, email, phone, None, birth_year)
        
        self.hourly_salary = hourly_salary
        self.worked_hours = 0
    
    def salary_after_taxes(self):
        # Innan denna anropas så måste man sätta "worked_hours"
        
        return self.deduct_taxes(self.hourly_salary * self.worked_hours)


if __name__ == '__main__':
    #in_salary = int(input("Skriv in din lön: "))
    
    e1 = Employee('Filip', 'filip@company.com', '010-23456',
                  38000, 1993)
    e2 = Employee('Johan', 'johan@company.com', '010-34567',
                  51500, 1979)
    
    print(f"{e1.name} får lön: {e1.salary_after_taxes()} kr")
    print(f"{e2.name} får lön: {e2.salary_after_taxes()} kr")
    
    print(f"Employee 1 heter {e1.name}")

    p1 = Person('Petter', 'petter@gmail.com', 1981)
    p1.greet()

    e1.greet()
    
    he1 = HourlyEmployee('Martin', 'martin@company.com', '010-76543',
                  220, 2002)

    he1.greet()
    he1.worked_hours = 100
    print(he1.salary_after_taxes())