# Exempel på instanser av klassen "Str"

my_var = "Hejsan"
my_var2 = "Hej igen"

print(type(my_var))

print(my_var.upper())


# Skapa en tom klass "Circle"
class Circle:
    pass

# Skapa instanser av klassen
c1 = Circle()
c2 = Circle()

# Lägg till värden i attributet radius
c1.radius = 5
c2.radius = 8

# Skriv ut attributet för de två instanserna
print(c1.radius)
print(c2.radius)


# Om vi i stället vill använda Circle från modulen vi
# skrivit i circle.py.

import circle as cs

# Krockar inte med Circle ovanför, för vi säger att den ska
# använda Circle från circle-modulen.
my_circle = cs.Circle(5)

print(my_circle.radius)  # Kolla på attriutet radius som sätts av init
print(my_circle.area())  # Använd metoden area()
