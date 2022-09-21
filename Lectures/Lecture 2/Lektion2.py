
text = "This is a few words"
print("The text is this long:", len(text))

# ==
# !=
# >
# <
# in

if "IS A" in text:
    print("True")
else:
    print("False")
    
user_text = "123"

if user_text.isdecimal():
    int(user_text)
else:
    print("Skriv in siffror!")


####

# Be användaren skriva in två stränar
text_one = input("Text 1: ")
text_two = input("Text 2: ")

# Om de är lika långa, skriv ut "Lika långa!"
if len(text_one) == len(text_two):
    print("Lika långa!")

# Om de har samma innehåll, skriv ut "Samma!"
if text_one == text_two:
    print("Samma!")

####

count = 1

while count <= 10:
    print("The number is:", count)
    # print(" ... Incrementing count")
    
    count += 1
    
print("Done!")
print("Count:", count)


####

# Be användaren om ett nummer
# Konvertera till ett heltal (integer)
stars = int(input("Antal: "))

# Börja med en stjärna
# Skriv ut ökande antal stjärnor
star_count = 1

while star_count <= stars:
    print("*" * star_count)
    
    star_count += 1


####

# Random number generation

import random

random_number = random.randint(1, 10)
print("Slumpad siffra:", random_number)

random_float = random.uniform(1.1, 2.2)
print("Slumpat decimaltal:", random_float)

my_list = ["äppel", "päron", "banan"]
random_item = random.choice(my_list)
print(random_item)

####

my_string = "Här är några ord"

str_split = my_string.split()

# Börja med första ordet
# Skriv ut vartannat ord

index = 0

# Loopa över listan och indexera
while index < len(str_split):
    print(str_split[index])
    index += 2


# Börja med sista ordet
# Skriv ut orden i omvänd ordning
index = len(str_split) - 1

# ['Här', 'är', 'några', 'ord']
#    0     1        2       3
# len == 4

#print(index)
#print(str_split[index])

while index >= 0:
    print(str_split[index])
    index -= 1


import random

# Be användaren om två tal
first_number = int(input("Tal 1: "))
second_number = int(input("Tal 2: "))

# Slumpa fram ett tal mellan de två talen
random_number = random.randint(first_number, second_number)

# Skriv ut
print("Random number:", random_number)

# Här lägger vi till en kommentar i slutet.

