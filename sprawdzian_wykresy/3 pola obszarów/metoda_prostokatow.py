# metoda prostokątów
# obliczenie pola ograniczonego wykresem funkcji, osią 0x i prostymi p,q 
def F(x):
    return x**2 - x - 3

def oblicz(p, q, n):
    dl = (q - p) / n
    s = 0
    for i in range(n):
        s += abs(F(p + dl/2 + i*dl))
    return dl * s

p = float(input("podaj [p]: "))
q = float(input("podaj [q]: "))
n = int(input("liczba prostokatow n: "))

print("pole:", oblicz(p, q, n))