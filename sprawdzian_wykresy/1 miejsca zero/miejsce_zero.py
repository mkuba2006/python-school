# Znajdowanie miejsca zerowego metodą połowienia przedziałów


def f(x):
    return x**3 - 3*x**2 + 2*x - 6 # rozpatrujemy wielomian f(x) = x^3 - 3x^2 + 2x - 6




def szukaj(a, b, eps):
    if f(a) == 0.0:
        return a
    if f(b) == 0.0:
        return b
    
    srodek = (a+b)/2
    
    if abs(b-a) <= eps:
        return srodek
    if f(a)*f(srodek) < 0:
        return szukaj(a, srodek, eps)
    
    
    return szukaj(srodek, b, eps)



a = float(input("lewy koniec: "))
b = float(input("prawy koniec: "))
eps = float(input("dokładność: "))

print("miejsca:", round(szukaj(a, b, eps), 5))