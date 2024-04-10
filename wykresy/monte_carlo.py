# pi = (4*T) / R
#T= ilosc kropek w kole
#R= ilosc wszystkich kropek 
# kolo = pi*r2

import random

ile = int(input("ile: "))
T = 0

for _ in range(ile):
    x = random.randint(-10000, 10000) / 10000
    y = random.randint(-10000, 10000) / 10000

    if x**2 + y**2 <= 1:
        T += 1
    
    z= 4 * T / ile

print(z)