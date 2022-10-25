import pprint

my_magic_number = 254.3


# Funktion som beräknar arean av en kvadrat
def area(base):  # "area" är en variabel som pekar på funktionen
    return base * base


# Funktion som beräknar omkretsen av en kvadrat
def circumference(base):
    return base * 4


# Tester
def run():
    print("Area(5) == 25:", area(5) == 25)
    print("Circumference(5) == 20:", circumference(5) == 20)


if __name__ == '__main__':
    run()
    
    pprint.pprint(globals())
