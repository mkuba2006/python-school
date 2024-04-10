p = int(input("p:"))
q = int(input("q:"))
E = float(input("E:"))
s=(p+q)/2

def F(x):
    return x**2 - x - 3


while F(p) != 0 and F(q) != 0 and q-p>=E:
    s=(p+q)/2
    if F(p) * F(s) > 0:
        p=s
    else:
        q=s


if F(p)==0:
    print(p)
if F(q)==0:
    print(q)
print(s)
