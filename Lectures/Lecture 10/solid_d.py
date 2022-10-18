# Bröd
# Kakor
# Pizza


# Bagare

class FoodInterface:
    def bake(self):
        pass
    def eat(self):
        pass

class Bread(FoodInterface):
    def bake(self):
        print("Baking bread!")
    
    def eat(self):
        print("Eating bread!")


class Cookie(FoodInterface):
    def bake(self):
        print("Baking cookie!")
    
    def eat(self):
        print("Eating cookie!")
        


class Baker:
    # "food" är ett object av typen FoodInterface
    @staticmethod
    def bake(food):
        food.bake()


def bake_all_foods():
    baker = Baker()
    bread = Bread()
    cookie = Cookie()
    
    baker.bake(bread)
    baker.bake(cookie)

bake_all_foods()

