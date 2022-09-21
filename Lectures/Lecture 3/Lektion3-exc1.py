# Övning: Hitta största talet i en lista: [1, 9, 3, 4, 13, 5, 4]

my_list = [-9, -3, -4, -13, -5, -4, -1]

largest_number = my_list[0]

for num in my_list:
    if num > largest_number:
        largest_number = num

print("Largest number:", largest_number)


####

# Övning: Skapa ett spel

import random

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
