import sys


def multi_divide(a, b, c):
    return a / b / c


def main():
    print(type(sys.argv))
    print(sys.argv)

    for i, arg in enumerate(sys.argv):
        print(f'Argument: {i} - {arg}')

    with open(sys.argv[1]) as file:
        print(file.readlines())


if __name__ == '__main__':
    # print(multi_divide(10, 5, 2))
    # print(multi_divide(10, 5, 0))

    main()
