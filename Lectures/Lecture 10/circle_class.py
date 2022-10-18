import math


MAX_RADIUS = 100


class NegativeRadiusError(ValueError):
    """Raised when the input is negative"""


class RadiusTooBigError(ValueError):
    """Raised when radius is too big"""


class Circle:
    """Class to handle creation and math with circles

    More text here...

    """
    def __init__(self, radius):
        # Don't Repeat Yourself:
        # Lägg felhanteringen centralt istället, så slipper vi skriva den i varje metod: area, diameter osv.
        
        if radius < 0:
            raise NegativeRadiusError('can only use "non-negative" radius')
        
        if radius > MAX_RADIUS:
            raise RadiusTooBigError("radius 'needs' to be smaller than", MAX_RADIUS)
        
        self.radius = radius
        
    def area(self):    
        # Calculate the area of the circle
        return math.pi * self.radius ** 2
    
    def diameter(self):
        return self.radius * 2

"""
# Mata in en radie
# Hantera felen på olika sätt:
#  r < 0: Allvarligt logikfel någonstans i koden
#         Rapportera till programmerare
#  r > 100: Mata in ett nytt tal

try:
    # läs in radie från användare.
    # skapar cirkel
except ValueError as e:
    # Gör något
except Exception as e:
    # Katastrof. Avsluta programmet.
"""
