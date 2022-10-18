# Exempel på dålig kod
"""
class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price
    
    # Bryter mot principen för att vi behöver förändra koden för att bygga ut systemet
    # med fler kundtyper
    def give_discount(self):
        if self.customer = 'fav':
            return self.price * 0.8
        
        if self.customer = 'vip':
            return self.price * 0.7
"""

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        return self.price * 0.8
    

class VIPDiscount(Discount):
    def give_discount(self):
        return self.price * 0.7
    

class FamilyDiscount(Discount):
    def give_discount(self):
        return super().get_discount() * 2
