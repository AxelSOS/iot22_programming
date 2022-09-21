# En funktion som lägger ihop 2 tal
def my_add(first_number, second_number):
    # Addera två tal
    # Skicka tillbaka resultatet
    print("Received input:", first_number, second_number)
    return (first_number + second_number)

# En funktion som skriver ut en hälsning
def say_hello():
    print("Hello!")

print(my_add(4, 2))
print(my_add(2, 78))
print(my_add(23, 6))
print(my_add(24, 0))
say_hello()
say_hello()
say_hello()


# Måste man definiera alla funktioner högst upp?
# Kan man anropa funktioner i andra funktioner?