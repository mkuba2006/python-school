# monte carlo

import random

def pi(n):
    n0 = 0
    for i in range(n):
        x = -1 + 2 * (random.random())
        y = -1 + 2 * (random.random())
        if x**2 + y**2 <= 1:
            n0 += 1
    return 4 * (n0 / n)

n = int(input("Liczba punktow: "))
print("Przyblizenie pi:", pi(n))