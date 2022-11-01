
if __name__ == '__main__':
    #                   11111111
    #         012345678901234567
    #my_str = "Hello Python Exam!"

    #print(my_str[4:-8])  # List Slicing


    #         0        1       2       3       4        5       6        7       8         9
    names = ['Alice', 'Maja', 'Vera', 'Alma', 'Selma', 'Elsa', 'Lilly', 'Ella', 'Astrid', 'Wilma']

    print(names[start:end:step])

    # Ta alla namnen, gör en ny lista med bara de två första bokstäverna
    #new_names = [n[0:2] for n in names]
    #print(new_names)

    """
    # Med for-loop
    new_list = []
    for n in names:
        if n.endswith('a'):
            new_list.append(n.upper())

    print(new_list)

    # Med list comprehension
    new_list2 = [n.upper() for n in names if n.endswith('a')]
    print(new_list2)
    """