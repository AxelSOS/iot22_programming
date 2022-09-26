# En funktion som skriver en rad till en loggfil

def write_to_log(logtext, filename="logfile.txt"):
    with open(filename, mode="x") as file:
        file.write(logtext + "\n")


write_to_log("Running my program", "test.txt")
