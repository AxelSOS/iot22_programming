import argparse


def main():
    # Hantera argument
    parser = argparse.ArgumentParser()
    parser.add_argument('--min', action='store_true')  # --min
    parser.add_argument('--max', action='store_true')  # --max
    parser.add_argument('numbers', nargs='+', type=int, help='numbers to process')  # lista med siffror
    args = parser.parse_args()

    # Skickat in min eller max?
    if args.min:
        print("Smallest value is:", min(args.numbers))

    if args.max:
        print("Largest value is:", max(args.numbers))


if __name__ == '__main__':
    main()
