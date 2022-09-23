####
# Default-argument
####

# En funktion som skriver ut en hälsning
def say_hello(name="Andreas"):
    # Om inget namn anges, så används "Andreas"
    print(f"Hello, {name}!")
    

say_hello()  # Hello Andreas
say_hello("Kurt")  # Hello Kurt

# Exempel från förra gången
import math

# Om inget anges använder den radien 1.0
def area(radius=1.0):
    # Fungerar med alla datatyper
    return math.pi * radius**2

print(area())  # 1.0
print(area(1.1))


####
# Argument efter position, efter namn
####

def greet(name, greeting):
    print(greeting, name)
    
# Argument efter position. Första argumentet = första värdet, andra = andra...
greet("Erland", "Hejsan")

# Keyword arguments låter anroparen bestämma sin egen ordning
greet(name="Erland", greeting="Hejsan")
greet(greeting="Hejsan", name="Erland")

# Några argument kan ha default-värden
def add_numbers(a, b, c=0, d=0):
    print(f'{a=}')
    print(f'{b=}')
    print(f'{c=}')
    print(f'{d=}')
    return sum([a, b, c, d])

print(add_numbers(1, 2, d=6))
print(add_numbers(d=5, b=2, c=4, a=1))


####
# Tvinga användare att använda keyword-stilen på argumenten
####

# Allt som kommer efter argumentet '*' är keyword-argument
def dangerous_function(*, file, command):
    print(f'Running command {command} on file {file}')

# dangerous_function('Remove', 'C:\\Temp\\betyg.xls')  # Detta ger ett fel
dangerous_function(command='Remove', file='C:\\Temp\\betyg.xls')

# Allt som kommer efter argumentet '*' är keyword-argument
# Allt som kommer innan går att använda efter position
def dangerous_function2(greeting, *, file, command):
    print(f'{greeting}. Running command {command} on file {file}')

dangerous_function2('Hello', command='Remove', file='C:\\Temp\\betyg.xls')


####
# Funktioner som tar in godtyckligt antal argument
####

def print_all_args(*args):  # "*" innan namnet
    print(type(args))  # Argumentet "args" är av typen "tuple"
    print(args)
    print("Length:", len(args))
    
    for a in args:  # Vi kan loopa över tupler
        print(a)
    
    print()


# Anropa funktionen med olika många argument
print_all_args(1, 2, 3)
print_all_args('Hejsan')
print_all_args('Hejsan', 'Alla')
print_all_args()
print_all_args([1,2,3])
print()
print()

# Exempel: Säg "greeting" till alla namn
# 1: Argument efter position
# 2: Positions-argument med tuple
def greet_all_names(greeting, *names):
    for name in names:
        print(greeting, name)

greet_all_names("Hejsan", "Adam", "Bertil", "Caesar", "David")
print()
print()


####
# Godtyckligt antal keyword-argument
####

def print_all_args(**kwargs):
    print(kwargs)
    print(type(kwargs))
    
    for key, value in kwargs.items():
        print(f'{key} = {value}')

print_all_args(arg1="Adam", arg2=11, arg3=4.4)


####
# Dictionaries

postnummer = {
    'guldheden': 41323,
    'säve': 21746,
    'landvetter': 43350,
    'malmö': [1, 2, 3]
    }

print(postnummer.get('säve'))
print(postnummer['säve'])
print()

print(postnummer.keys())  # Hämta alla nycklar
print('säve' in postnummer.keys())
print('lund' in postnummer)  # Samma sak som .keys()
print()

print(postnummer.values())  # Hämta alla värden
print()

print(postnummer.items())  # Hämta alla key-value-par
print()

for stad, kod in postnummer.items():
    print(f'{stad} = {kod}')
