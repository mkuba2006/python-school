# metoda trapezów
# obliczenie pola ograniczonego wykresem funkcji, osią 0x i prostymi p,q 

def F(x):
    return -x**3 - x**2 + 1

def oblicz(p, q, n):
    dl = (q - p) / n
    s = 0
    for i in range(1, n):
        s += abs(F(p + i*dl))
    return dl/2 * (abs(F(p)) + abs(F(q)) + 2*s)

p = float(input("podaj [p]: "))
q = float(input("podaj [q]: "))
n = int(input("liczba trapezow n: "))

print("pole:", oblicz(p, q, n))