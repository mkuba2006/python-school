# metoda Newtona Rapsona

def znajdz(P):
    a = 1.0
    b = P

    while abs(a - b) >= 0.000001:
        a = (a + b) / 2.0
        b = P / a

    return (a + b) / 2.0


x = float(input("Podaj liczbe: "))

print(znajdz(x))

