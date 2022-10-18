import math

class NegativeRadiusError(ValueError):
    """Raised when the input is negative"""
    
class RadiusTooBigError(ValueError):
    """Raised when radius is too big"""

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        if self.radius < 0:
            raise NegativeRadiusError("can only use non-negative radius")
        
        if self.radius > 100:
            raise RadiusTooBigError("radius needs to be smaller than 100.")
    
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
