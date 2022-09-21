# Be om användarens namn
name = input("Skriv in namn: ")

# Be om användarens ålder
age = input("Skriv in ålder: ")

# Skriv ut meddelande
print(f"Hej {name}, du är {age} år gammal.")


####

num_1 = 3
num_2 = 6
num_3 = 7

answer = (num_1 + num_2 + num_3) / 3
print(f"Mean of {num_1}, {num_2}, {num_3}: {answer}")


####

# Be användaren om temperatur i C. Konvertera C till siffra.
temp_c = int(input("Ange temperatur i C: "))

# Konvertera till F
temp_f = temp_c * (9/5) + 32

# Skriv ut
print(f"Temperatur i Fahrenheit: {temp_f}")