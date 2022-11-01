import sys
import argparse

def main_sys_argv():
    print(sys.argv)
    print(len(sys.argv))

    for i, arg in enumerate(sys.argv):
        print(f"Argument: {i} - {arg}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="input file")
    args = parser.parse_args()

    with open(args.file) as my_file:
        print(my_file.readlines())


if __name__ == '__main__':
    main()
