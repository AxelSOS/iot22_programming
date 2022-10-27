class PlayingCard:
    def __init__(self, color, value):
        # Validera color
        if color not in ["Hearts", "Diamonds", "Spades", "Clubs"]:
            raise ValueError("Color is only allowed to be one of:" +
            "Hearts, Diamonds, Spades, Clubs.")
        
        # Validera value
        #if value not in range(1, 14):
        if value < 1 or value > 13:
            raise ValueError("Value must be between 1 and 13.")
        
        self.color = color
        self.value = value
    
    @classmethod
    def ace_of_hearts(cls):
        return cls("Hearts", 1)
    
    def __str__(self):
        return str(self.value) + " of " + self.color
