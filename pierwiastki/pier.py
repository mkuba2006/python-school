import math
pole = 3
a = 1
b = 3 

while abs(a**2 - pole) > 1e-5:
    print(a, b)
    a = (a + b) / 2
    b = pole / a