import math

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
print("\n")
if a == 0:
    print("NIE kwaratowa")
else:
    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        if x2 < x1:
            x1, x2 = x2, x1
        print("2:", x1, x2)
    elif delta == 0:
        print("1:", -b/(2*a))
    else:
        print("niema")

