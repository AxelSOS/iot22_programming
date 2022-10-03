# List comprehensions

sentence = "Övning på list comprehensions"

my_list = sentence.split()

print(my_list)

#[6, 2, 4, 14]

output_list = []
for word in my_list:
    output_list.append(len(word))
    
print(output_list)

##############

# Skapa en ny lista med (uttryck) för varje element i en annan lista
word_lengths = [ len(word) for word in my_list ]
print(word_lengths)


all_words = [ word for word in my_list ]
print(all_words)

[ print(word) for word in my_list ]

# En lista med alla ord som har fler än 3 tecken

longer_than_three = [ word for word in my_list if len(word) > 3]
print(longer_than_three)

longer_than_three_b = []
for word in my_list:
    if len(word) > 3:
        longer_than_three_b.append(word)
