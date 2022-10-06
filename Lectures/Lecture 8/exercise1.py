# Skapa en lista
my_list = [1, 2, 3, 4, 5]

# Skriv ut listan för användaren
print(f"The list is {my_list}")

# Låt användaren välja ett element ur listan
while True:
    index = None
    try:
        index = int(input("Write index: "))
        print(f"Element at index {index} is: {my_list[index]}")
    except IndexError as ie:
        print(f"  IndexError: {ie}")
    except ValueError as ve:
        print(f"  ValueError: {ve}")
   
"""
# Låt användaren välja ett element ur listan
while True:
    index = None
    try:
        index = int(input("Write index: "))
    except ValueError as e:
        print(f"  ValueError: {e}")
    
    if not index:
        continue  # Börja om loopen högst upp igen
    
    try:
        print(f"Element at index {index} is: {my_list[index]}")
    except IndexError as e:
        print(f"  IndexError: {e}")
"""
"""
Write index: H
  Error: invalid literal for int() with base 10: 'H'
"""

# Om fel: Skriv ut vad användaren gjorde för fel
