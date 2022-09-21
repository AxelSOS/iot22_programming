# Skriv ut alla tal från 1 tom 100
for num in range(1, 101):
    # Om talet är 42, skriv ut ...
    if num == 42:
        print("Answer to the Ultimate Question of Life, the Universe, and Everything")
    
    # Om båda, Skriv ut FizzBuzz
    # elif (num % 3 == 0) and (num % 5 == 0):
    if num % 15 == 0:
        print("FizzBuzz")
    
    # Om talet är jämt delbart med 3, skriv ut Fizz
    if num % 3 == 0:
        print("Fizz")
    
    # om talet är jämt delbart med 5, skriv ut Buzz
    if num % 5 == 0:
        print("Buzz")

    # Annars, skriv ut talet
    else:
        print(num)
