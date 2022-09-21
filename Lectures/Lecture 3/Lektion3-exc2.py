# Givet radien, räkna ut arean på en cirkel.
import math

# Gör en funktion
def area(radius):
    # area = pi * radius^2
    area = math.pi * (radius**2)
    print(f"r = {radius}")
    print(f"area = {area}")
    
area(1.1)


####

import random

def play():
    # Slumpa fram ett tal mellan 1 och 10
    random_number = random.randint(1, 10)

    # Låt användaren gissa några gånger
    for num_guesses in range(3):
        # Be användaren skriva in ett tal
        guess = int(input("Your guess: "))

        # Skriv ut om gissningen är rätt eller fel
        if guess == random_number:
            print("You won!")
            break
        else:
            print("Wrong!")
        
    print("The number was:", random_number)

####

# Anropa spelet genom att skriva ett kommando
def menu():
    keep_going = True

    while keep_going:
        # Ta emot text från användaren
        user_command = input("Command: ").lower()
        
        # Check for exit command
        if user_command == "exit":
            keep_going = False
            
        elif user_command == "play":
            play()


menu()