import argparse


def wordcount():
    # Hantera argument
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help='input file')
    args = parser.parse_args()

    # Öppna en fil
    with open(args.file) as file:
        # Räkna antalet ord
        # Alt 1:
        nbr_words = 0
        for line in file.readlines():
            nbr_words += len(line.split())

        # Alt 2:
        print("Antal ord:", len(file.read().split()))

    # Alt 1: Utskrift
    print("Antal ord:", nbr_words)


if __name__ == '__main__':
    wordcount()
