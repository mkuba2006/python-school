# metoda Newtona Rapsona

def znajdz(pole):
    a = 1.0
    b = pole

    while abs(a - b) >= 0.000001:
        a = (a + b) / 2.0
        b = pole / a

    return (a + b) / 2.0


pole = float(input("Podaj liczbe: "))

print(znajdz(pole))

