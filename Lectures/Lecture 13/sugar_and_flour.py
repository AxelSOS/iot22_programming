class Flour:
    # Klassen har en init-metod som initierar datan
    def __init__(self, volume):
        self.volume = volume

    # En metod för att konvertera en enhet till en annan
    # Använder ingen information från klassen.
    @staticmethod
    def volume_to_weight(volume):
        return volume * 0.5

class Sugar:
    # Klassen har en init-metod som initierar datan
    def __init__(self, volume):
        self.volume = volume
        Sugar.volume_to_weight(self.volume)

    # En metod för att konvertera en enhet till en annan
    # Använder ingen information från klassen.
    @staticmethod
    def volume_to_weight(volume):
        return volume * 0.99


# Två funktioner som konverterar en enhet till en annan
def volume_to_weight_flour(volume):
    return volume * 0.5

def volume_to_weight_sugar(volume):
    return volume * 0.99


# Vi kan anropa våra vanliga funktioner
print(volume_to_weight_flour(4))
print(volume_to_weight_sugar(4))

# Eller göra samma sak med de statiska metoderna vi har i klasserna
print(Flour.volume_to_weight(4))
print(Sugar.volume_to_weight(4))
