# test_circle.py
import circle
import math

import pytest  # För att kunna testa exceptions

def test_area():
    assert circle.area(1) == math.pi
    assert circle.area(2) == math.pi * 2**2
    
    # Ibland vill vi testa att saker inte funkar: Kastar exceptions
    
    with pytest.raises(ValueError):
        circle.area(-1)

def test_diameter():
    input_list = [1, 2, 3, 4]
    expected_output_list = [2, 4, 7, 8]
    
    # Zip: Iterera över båda listorna samtidigt
    for input_val, expected_out in zip(input_list, expected_output_list):
        assert circle.diameter(input_val) == expected_out
