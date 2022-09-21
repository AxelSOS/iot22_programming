# Repetition av indexering av listor

#fruits = ["apple", "orange", "pear", "banana"]

#print(fruits[-1])  # Sista elementet i listan
#print(fruits[-2])  # Näst sista elementet

#print(fruits)
#print(fruits[0:2]) # Element 0 och 1
#print(fruits[1:3]) # Element 1 och 2

#some_fruits = fruits[1:3]  # Gör en ny variabel med bara några element
#print(some_fruits)  # Skriv ut den nya listan
#print(some_fruits[0])  # Skriv ut första elementet i nya listan

#print(fruits[1:])  # Skriv ut från första elementet till slutet av listan
#print(fruits[:2])  # Skriv ut från listans start till andra elementet
#print(fruits[:])  # Använder vi inga index får vi ut hela listan


# [start:end]  # Slice syntax
# [start:end:step]  # Extended slice syntax - skippa element i listan
# print(fruits[::2])  # Varannat element

"""
# Kopior av listor ändras inte när originalet ändras
print(fruits)

some_fruits = fruits[0:2]
print(some_fruits)

fruits[0] = "grapefruit"
print(fruits)

print(some_fruits)

some_fruits[0] = "pineapple"
print(fruits)

print(some_fruits)
"""

# Slå ihop listor
# my_list = ['A', 'B', 'C']
# my_list += [1, 2, 3]

# print(my_list)


#print(fruits)

#for fruit in fruits:
    #print(fruit)
    
#for index in range(len(fruits)):
#    print(f"index: {index}, fruit: {fruits[index]}")


# Enumerate - numrera elementen i en lista
#for index, fruit in enumerate(fruits):
#    print("index:", index, "fruit:", fruit)

####

# zip() låter oss loopa över flera listor samtidigt

#fruits = ["apple", "orange", "pear", "banana"]
#prices = [24, 20, 15, 39]

# fruit: apple, price: 24 kr
# fruit: orange, price: 20 kr
# fruit: pear, price: 15 kr
# fruit: banana, price: 39 kr

#for fruit, price in zip(fruits, prices):
    #print("fruit:", fruit, ", price:", price)

#print("pineapple" not in fruits)


####
"""
# While keep_going-mönstret

keep_going = True

while keep_going:
    # logik här...
    
    # Ta emot text från användaren
    user_command = input("Command: ").lower()
    
    # Check for exit command
    if user_command == "exit":
        keep_going = False
        
    elif user_command == "play":
        pass
"""


# Avbryta en loop innan allt är klart
for num in range(10):
    if num == 7:
        break
    
    print(num)
