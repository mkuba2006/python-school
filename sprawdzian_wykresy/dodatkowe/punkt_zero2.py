# miejsce zero w przedziale [p,q]

def F(x):
    return x**2 - x - 3

def oblicz(p, q, EPS):
    s = (p + q) / 2
    while F(p) != 0 and F(q) != 0 and q - p >= EPS:
        if F(s) > 0:
            p = s
        else:
            q = s
        s = (p + q) / 2
    if F(p) == 0:
        return p
    if F(q) == 0:
        return q
    return s

p = float(input("podaj [p]:"))
q= float(input("podaj [q]:"))
EPS = float(input("podaj dokladnosc E1:")) 
print("miejsce zerowe = ", oblicz(p, q, EPS))