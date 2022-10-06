import math

# ValueError : Ett värde är fel
# AttributeError : Du har använt funktionens definition
#                  på helt fel sätt
# IndexError: Kollar utanför en listas längd


def area(radius):
    if not isinstance(radius, int):
        raise TypeError("radius must be an integer")
    if radius < 0:
        raise ValueError("can only use non-negative radius")
    
    return math.pi * radius ** 2


result = None
try:
    print(area("Hej"))
except ValueError as e:
    print(f"ValueError: {e}")
except TypeError as e:
    print(f"TypeError: {e}")
    

"""
while True:
    result = None
    try:
        #num = area(int(input("Enter a radius: ")))
        result = f"  Area: {num}"
    except ValueError as e:
        result = f"  Oops, error: {e}!"
        
    print(result)


while True:
    try:
        num = int(input("Enter a number: "))
        print(f"You wrote: {num}")
    except ValueError:
        print(f"Oops, please write a number!")
"""
