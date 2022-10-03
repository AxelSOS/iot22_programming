"""
Övningar: Datetime
 - Med hjälp av datetime-biblioteket
 - Skriv ut nuvarande datum och tid
 - Skriv ut bara tiden
 - Skriv ut vilket datum det var för 14 dagar sedan
   - Skriv ut vilken veckodag det var
 - Skriv ut antalet dagar till julafton
 
 
https://docs.python.org/3/library/datetime.html
"""

import datetime

# Skriv ut nuvarande datum och tid

now = datetime.datetime.now()
print(now)

# Skriv ut bara tiden
print(now.strftime("%H:%M:%S"))
print(f'{now.hour}:{now.minute}:{now.second}')  # Samma sak

# Vilket datum var det för 14 dagar sedan?
previous_time = now - datetime.timedelta(days=14)
print(previous_time)

print(previous_time.strftime("%A"))


weekdays = ['Måndag', 'Tisdag', 'Onsdag']
print(weekdays[previous_time.weekday()])


# Skriv antal dagar till julafton
xmas_eve_date = datetime.datetime(2022, 12, 24)
print(xmas_eve_date)
days_to_xmas = xmas_eve_date - now
print(days_to_xmas)