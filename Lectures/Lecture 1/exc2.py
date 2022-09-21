# Skriv ut alla tal från 1 till 20

for num in range(1, 21, 1):
    print(num)


####

# Skriv ut alla jämna tal från 1 till 20
for num in range(1, 21):
    if num % 2 == 0:
        print(num)

# Alternativ lösning
for num in range(2, 21, 2):
   print(num)


####

# Skriv ut alla udda tal från 1 till 20

for number in range(1, 21):
    # Om "number" inte är jämt delbart med 2
    if number % 2 != 0:
        print(number)
    
    # Alternativ lösning
    if number % 2 == 1:
        print(number)

# Alternativ lösning 2
for number in range(1, 21, 2):
    print(number)


####
    
# Be användaren om tal 1
num_a = int(input("First number: "))

# Be användaren om tal 2
num_b = int(input("Second number: "))

# Om tal 2 är större än tal 1: Skriv ut "Större"
if num_b > num_a:
    print("Större")

# Om tal 1 är större än tal 2: Skriv ut "Mindre"
elif num_b < num_a:
    print("Mindre")

# Annars, skriv ut "Samma"
else:
    print("Samma")


####

age = int(input("Hur gammal är du? "))

# Skriv ut ålder i år
print(f"År: {age}")

# Konvertera ålder till andra enheter
age_months = age * 12
age_days = age * 365
age_seconds = age_days * 24 * 3600

# Skriv ut
print(f"Månader: {age_months}")
print(f"Dagar: {age_days}")
print(f"Sekunder: {age_seconds}")

# Skriva ut "True" om personen är 30 år eller äldre, annars False
if age >= 30:
    print("True")
else:
    print("False")

# Alternativ
print(age >= 30)
