
pole = 3
a = 1
b = 3 

while abs(a**2 - pole) > 0.000001:
    print(a, b)
    a = (a + b) / 2
    b = pole / a
    
    
    
    
