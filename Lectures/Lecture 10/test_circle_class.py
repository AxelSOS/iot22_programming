import circle_class
import math

import pytest  # Låter oss använda parameterisering

# Testa att skapa en instans av klassen
def test_create_circle():
    c = circle_class.Circle(5)
    assert c.radius == 5

# Parameterisering
# Skicka flera olika indata till testfunktionen, skapa ett test per input

# Skapa en cirkel med radie, och testa att diametern stämmer
# Skicka in en input
# Skicka in en förväntad output
@pytest.mark.parametrize("test_input,expected_output", [
    (2, 4), (4, 8), (15, 30)  # En grupp olika testdata (input, output)
])
def test_diameter(test_input, expected_output):
    c = circle_class.Circle(test_input)
    assert c.diameter() == expected_output, "Diameter didn't match!"  # Felmeddelande
