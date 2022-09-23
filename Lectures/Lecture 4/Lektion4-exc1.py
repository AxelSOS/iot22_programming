# 1. Skriv en funktion som ger tillbaka produkten av alla tal man ger den (multiplikation)
def my_product(*args):
    product = 1  # Variabeln håller produkten av alla värden
    
    # Multiplicera varje tal med vår framräknade produkt
    for a in args:
        product *= a
    
    # Returnera svaret
    return product

print(my_product(2, 4))
print(my_product(2, 4, 2))
print(my_product(1, 0, 2))
print(my_product(2, 1, 2, -2))


####
# 2. Skriv en funktion som tar en lista och ger tillbaka en ny lista utan dubbletter
# remove_duplicates([1, 1, 2, 3, 3, 4, 4, 5, 6, 7, 7, 4, 2])
# [1, 2, 3, 4, 5, 6, 7]
####
def remove_duplicates(duplicate_list):
    return list(set(duplicate_list))

print(remove_duplicates([2, 3, 3, 4, 4, 5, 6, 7, 7, 1, 1, 4, 2]))


####
# 3. Skriv en funktion som givet två tal kollar om det första talet är jämt delbart med det andra talet
# Ex: is_divisible(6, 3)  # True
# Ex: is_disisible(6, 4)  # False
####
def is_divisible(num, divisor):
    return num % divisor == 0

print(is_divisible(6, 3))
print(is_divisible(6, 4))
print(is_divisible(5, 3))
print(is_divisible(5, 1))


####
# 4. Skriv en funktion som kollar om ett givet tal är ett primtal eller ej
####
def is_prime(num):
    # Börja med num, loopa tills 2. Om något är jämt delbart med vårt tal så är det inte ett primtal.
    count = num - 1
    
    while count > 2:
        if is_divisible(num, count):
            return False
        
        count -= 1
    
    return True
        

print(is_prime(7))  # True
print(is_prime(8))  # False
print(is_prime(11))  # True
print(is_prime(25))  # False
print(is_prime(2))  #
print(is_prime(1))  #


####
# 5. Skriv en funktion som givet a: en lista med tal och b: ett tal, ger tillbaks
# en lista som innehåller alla tal från a som är jämt delbara med b
# Ex: get_divisible_list([1, 2, 3, 4, 5, 6], 3)  # [3, 6]
####
def get_divisible_list(in_list, num):
    # Skapa en returvariabel
    retval = []
    
    # Loopa över alla tal i listan
    for a in in_list:
        # Kolla om talet är jämt delbart med "num"
        # Om det är det: Lägg till i en returlista
        if is_divisible(a, num):
            retval.append(a)
    
    # Skicka tillbaka listan
    return retval

print(get_divisible_list([1, 2, 3, 4, 5, 6], 3))  # [3, 6]
print(get_divisible_list([1, 2, 3], 4))  # []
print(get_divisible_list([1, 2, 3, 4], 1))  # [1, 2, 3, 4]


####
# 6. Skriv en funktion som givet en dict med namn och poäng, ger tillbaka det namnet som har högst poäng
# Ex: points = {'Adam': 65, 'Bertil': 72, 'Caesar': 81, 'David': 77}
# get_winner(points)  # Caesar
####
def get_winner(players):
    # Spara högsta värdet vi sett hittills
    winning_score = None
    winning_player = None
    
    # Loopa igenom alla spelare
    for player_name, player_score in players.items():
        # Om det är första spelaren vi kollar på, spara resultatet
        if (winning_score is None):
            winning_score = player_score
            winning_player = player_name
        
        # Om nästa spelare har högst resultat, spara spelarens information
        elif player_score > winning_score:
            winning_score = player_score
            winning_player = player_name
        
    # Returnera den vinnande spelaren
    return winning_player

    # Vi kan även returnera både namn och poäng:
    # return winning_player, winning_score

points = {'Adam': 65, 'Bertil': 72, 'Caesar': 81, 'David': 77}

print(get_winner(points))

# Om vi skickar tillbaks både namn och poäng:
# winners_name, winners_score = get_winner(points)
# print("Winner's name: ", winners_name, ". Winner's score: ", winners_score, sep='')
