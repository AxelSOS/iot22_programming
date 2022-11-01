
def has_duplicates(my_list):
    return len(set(my_list)) != len(my_list)

def check_if_yahtzee(dice_list):
    return len(set([1, 2, 2, 6, 6])) == 1


if __name__ == '__main__':
    a = set([1, 2, 3])
    b = {3, 4, 5}

    c = {3, 3, 4, 4, 5, 5}
    # print(c)


    # Ta en lista, skriv en funktion som ger tillbaka True eller False
    # beroende på om den har dubletter eller inte

    print(has_duplicates([1, 2, 3, 4, 5]))
    print(has_duplicates([1, 2, 5, 4, 5]))

    print(3 in [1, 2, 3, 4, 5])  # Finns 3 i listan?
