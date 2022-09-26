# Öppna en fil för läsning
filename = "shakespear_quotes.txt"

with open(filename) as file:
    # OBS: Kör endast ett av dessa block åt gången.
    
    # Läs hela filen
    contents = file.read()
    print(type(contents))  # Contents är ett sträng-block
    print(contents)
    
    # Läs rad för rad
    print(file.readline())
    print(file.readline())
    print(file.readline())
    print(file.readline())
    
    # Loopa över varje rad
    for line in file:
        print(type(line))  # Varje rad är en sträng
        print(line, end='')  # Skriv ut raden
