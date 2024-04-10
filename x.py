import math

def f(x):
    return x*x + x + 2 

def Pole(a, b, n):
    h = (b - a) / n 
    S = (f(a) + f(b))
    for i in range(1, n):
        S += f(a + i * h)
    return S *0.5* h



a = int(input("a: "))
b = int(input("b: "))
pole = int(input("pol: "))
if a < b:
    print(round(Pole(a, b, pole), 2))
else:
    print("a musi byc mn niz b")