# Övning 1: Employee-klassen

class Employee:
    def __init__(self, name, email, phone, salary, birth_year):
        self.name = name
        self.email = email
        self.phone = phone
        self.salary = salary
        self.birth_year = birth_year
    
    def salary_after_taxes(self):
        output_salary = self.salary
        
        output_salary *= 0.7
        
        if self.salary > 46200:
            # Räkna ut hur mycket vi ligger över den statliga gränsen
            amount_over_limit = self.salary - 46200

            # Räkna ut hur mycket extra skatt som ska betalas
            extra_taxes = amount_over_limit * 0.2
            
            # Minska lönen med den extra skatten
            output_salary -= extra_taxes
        
        return output_salary


if __name__ == '__main__':
    #in_salary = int(input("Skriv in din lön: "))
    
    e1 = Employee('Filip', 'filip@company.com', '010-23456',
                  38000, 1993)
    e2 = Employee('Johan', 'johan@company.com', '010-34567',
                  51500, 1979)
    
    print(e1.salary_after_taxes())
    print(e2.salary_after_taxes())


