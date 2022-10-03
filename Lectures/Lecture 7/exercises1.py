my_list = [1, 25, 0, -2, -7, 14]

# [-2, -7]
new_list = [ num for num in my_list if num < 0 ]
print(new_list)

def get_divisible_list(in_list, dividend):
    # för varje tal i listan, kolla är talet jämt delbart med "dividend"
    # om det är det, lägg till talet på en ny lista
    
    div_list = [ num for num in in_list if num % dividend == 0 ]
    return div_list


#3. Gör en funktion som returnerar:
# En lista (med list comprehensions) som innehåller alla ord längre än 5 tecken

#           .             .             .
my_str = "Detta är några tecken i en sträng"

def longer_than_five(my_string):
    return [ word for word in my_string.split() if len(word) > 5 ]

print(longer_than_five(my_str))

"""

1. Givet listan: [1, 25, 0, -2, -7, 14]
    Gör en lista med alla tal som är mindre än 0

2. Funktion: Givet en lista och ett tal X, returnera en lista med alla tal som är jämt delbara med X

3. Gör en funktion som returnerar:
    En lista (med list comprehensions) som innehåller alla ord längre än 5 tecken

4.
Gör en klass som representerar en glass-smak
Gör en klass som representerar en skål
- Skålen ska kunna innehålla flera skopor glass av olika smaker

5.
Gör en databas för filmer
- Olika typer av personer som arbetar på en film
  (Skådespelare, regissörer, ...)
- Filmer
  - innehåller en eller flera personer i olika roller
  - Har titel, release-datum, med mera
  - Har genre, IMDB-poäng
  
Utskrift:
    - Skriv ut om en film har ett betyg högre än X
    - Skriv ut alla skådespelare i en film
    - Lista alla filmer med betyg högre än X
    
"""