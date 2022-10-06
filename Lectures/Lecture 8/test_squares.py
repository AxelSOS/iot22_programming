# test_squares.py

import math

def test_sqrt():
    num = 25
    
    # Jämför det faktiska värdet med det förväntade värdet
    assert math.sqrt(num) == 5.0  # Nånting ska bli True


def test_equals():
    assert 1 == 1
    

def test_square():
    num = 7
    assert num * num == 49