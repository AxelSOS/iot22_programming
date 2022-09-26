import os
import pprint

print(os.getcwd())  # Sökväg till nuvarande katalogen

pprint.pprint(os.listdir())  # Lista innehållet i nuvarande katalog

# os.mkdir("temp") # Skapa en katalog

# os.listdir() # Tar även en katalog som valfri input
# os.mkdir('temp')  # Skapa katalogen "temp"
# os.rename('fil', 'nyfil')  # Döper om en fil eller mapp
# os.remove('fil')  # Tar bort en fil
# os.rmdir('mapp')  # Tar bort en tom mapp
# os.path.join('path1', 'path2')  # Slår ihop två sökvägar


# import pathlib
# pathlib.Path().cwd() / resolve()
# Finns även motsvarande metoder för resten av os. Se dokumentationen.
