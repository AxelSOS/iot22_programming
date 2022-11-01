
def add_numbers(*args):
    my_sum = 0

    for a in args:
        my_sum += a

    return my_sum


def print_kwargs(**kwargs):
    print(type(kwargs))


def sum_all_values_in_a_list(my_list):
    print(type(my_list))
    return sum(my_list)


if __name__ == '__main__':
    print(sum_all_values_in_a_list([1, 4, 6, 8]))

    """
    print(add_numbers(1, 2, 3, 4, 10))

    print_kwargs(a=1, b=2, c=3)

    person_list = [
        {'name': 'Andreas', 'age': 37},
        {'name': 'Johan', 'age': 62}
    ]

    for person in person_list:
        print(type(person))
        print(person['name'])
        print(person['age'])
    """