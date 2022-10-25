import sys
import argparse


def multi_divide(a, b, c):
    return a / b / c


def main_sys_argv():
    print(type(sys.argv))
    print(sys.argv)

    for i, arg in enumerate(sys.argv):
        print(f'Argument: {i} - {arg}')

    with open(sys.argv[1]) as file:
        print(file.readlines())

    # ArgParse
    # Kolla vilka växlar vi tagit emot.
    # Om vi skickar --linecount: Anropa linecount()
    # Om vi skickar --sum: Anropa sum_all_arguments()


def sum_all_arguments():
    my_sum = 0

    for num in sys.argv:
        try:
            int_num = int(num)
        except ValueError:
            continue  # Vi bryr oss inte om felet. Fortsätt.

        my_sum += int_num

    print("Summan är:", my_sum)


def linecount(filename):
    # --file filnamn.txt

    # with open(sys.argv[1]) as file:
    #     print("Antal rader:", len(file.readlines()))

    with open(filename) as file:  # Öppna filen
        print("Antal rader:", len(file.readlines()))


def main():
    parser = argparse.ArgumentParser()  # Starta "ArgParse"-systemet
    parser.add_argument('first_file', help='input file')  # Vi beskriver att vi vill ha en växel "--file"
    parser.add_argument('second_file', help='input file')  # Vi beskriver att vi vill ha en växel "--file"

    # Ta in en siffra
    # parser.add_argument('number', type=int)

    # Ta emot flera siffror
    parser.add_argument('numbers', nargs='+', type=int)

    # Lägg till en debugväxel som gör att programmet skriver ut fler saker
    parser.add_argument('--debug', '-d', action='store_true')  # args.debug blir True eller False
    parser.add_argument('--no_write_logfile', '-nf', action='store_false')  # args.no-write-logfile blir omvänd från store_true

    args = parser.parse_args()  # Tolka vad användaren har skrivit (bara en gång, sist av allt)

    print("--no_write_logfile", args.no_write_logfile)

    if args.debug:
        print("Debug mode enabled!")

    linecount(args.first_file)
    linecount(args.second_file)

    print(type(args.numbers))
    print(type(args.numbers[0]))
    print("numbers:", args.numbers)


if __name__ == '__main__':
    # print(multi_divide(10, 5, 2))
    # print(multi_divide(10, 5, 0))

    # main()

    # sum_all_arguments()

    main()


""" Övningar i ArgParse:
Skriv ett program som skriver ut antalet ord i en fil
* Ex: python wordcount.py --file shakespear_quotes.txt
* Antal ord: 96

Skriv ett program som tar en serie siffror och där man kan välja att använda
  "--max" för största värdet, eller "--min" för minsta värdet.
  
* (Hint: 'store_true' + en serie siffror)
* python main.py --min 1 2 3 4 5
  Smallest value is: 1
* python main.py --max 1 2 3 4 5
  Largest value is: 5
"""