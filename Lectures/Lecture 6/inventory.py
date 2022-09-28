# Skapa en klass "Inventory" som kan hålla saker
# Skapa en metod för att lista innehållet

class Inventory:
    """Class to hold items in an inventory.
    Inventories have a name and contents."""
    
    def __init__(self, my_name):
        self.name = my_name
        self.contents = []
    
    def store(self, item):
        """Store an item in the inventory"""
        
        self.contents.append(item)
    
    def list_contents(self):
        """List all contents in the inventory"""
        
        print(f"The {self.name} contains:")
        
        # Om inventory är tom ska den skriva ut det
        if self.contents == []:
            print("  Nothing")
            
        # Om det finns saker ska vi lista dem sak för sak
        else:
            for thing in self.contents:
                print(f"  {thing}")
        
        print()  # Lägg till en tom rad på slutet

if __name__ == '__main__':
    # Skapa en ny instans av typen Inventory
    player_inv = Inventory("Treasure Chest")
    
    # Först är den tom
    player_inv.list_contents()
    
    # Vi lägger till några saker och listar innehållet igen
    player_inv.store("Wooden Coins")
    player_inv.store("Cursed Diamond Ring")
    player_inv.store("Mug O' Grog")
    player_inv.list_contents()
    