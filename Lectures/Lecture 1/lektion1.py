####
# Kommentarer och utskrift
####

# Det här är en kommentar
print("Hello World!")  # Kommentar efter kod

# Först skriver vi ut hej
print("hej")
# Sen skriver vi ut summan av två tal
print(1 + 2)


####
# Variabler
####
number = 42
print(number)
print(number)
print(number)

number = "Hejsan"
print(number)
print(number)
print(number)

first_number = 12
second_number = 42

print(first_number)
print(second_number)


####
# Vi kan använda variabler på samma rad som vi skriver ut text
####

color = "red"

# Tre olika sätt att skriva ut
print("The color is:", color, ".")  # Komma-separerat
print("The color is: " + color + ".")  # Plus (Båda sidor av + behöver ha samma typ!)
print(f"The color is: {color}.")  # Format-sträng


####
# Variabler forts.
####
number = 1
number = number + 3  # Vi kan återanvända variabler
number += 3  # Samma som ovan, men kortare variant
print(number)


####
# Be användaren om input
####

number = input("Enter a number: ")
print("The number was", number)

# Läs in två tal från användaren
first_number = input("Tal 1: ")
second_number = input("Tal 2: ")  # Viktigt: input() ger tillbaka strängar, inte heltal!

# Konverterar strängarna till heltal och adderar dem
number = int(first_number) + int(second_number)

# Skriv ut summan
print(f"Summan är: {number}")


####
# Villkor ("Conditionals", "If-satser")
####

num = 0

if num > 0:
    print("The number is positive!")
elif num == 0:
    print("The number is zero!")
else:
    print("The number is negative!")

print("This is always printed.")


####
# For-loopar
####

# Skriv ut alla tal mellan 1 och 5

number = 14  # Detta värde kastas bort

for number in range(1, 6):  # Här skapas variabeln "number" och sätts till olika värden
    print(f"The number is {number}")
    
print("Nu är loopen klar.")

print(f"Nu är number: {number}")  # Kan vi använda "number" efter loopen är klar?
