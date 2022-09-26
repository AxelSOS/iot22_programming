filename = "shakespear_quotes.txt"

# Övning 1
count = 1

with open(filename) as file:
    # Loopa över varje rad
    for line in file:
        print(f"{count}: {line}", end='')  # Skriv ut raden
        count += 1


# Övning 1, alt
with open(filename) as file:
    # Loopa över varje rad
    for count, line in enumerate(file):
        print(f"{count+1}: {line}", end='')  # Skriv ut raden


# Övning 2
def linecount(input_file):
    linecounter = 0

    with open(input_file) as file:
        for line in file:
            linecounter += 1
            
    return linecounter

print(linecount("shakespear_quotes.txt"))


# Övning 3

def wordcount(input_file):
    #word_list = []
    count = 0
    
    with open(input_file) as file:
        for line in file:
            wordlist = line.split()
            count += len(wordlist)
            
    return count

print(wordcount("shakespear_quotes.txt"))
