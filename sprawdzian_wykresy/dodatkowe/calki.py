def F (x):
    return pow(x,2) -x -3

def oblicz(p,q,n):
    dl=(q-p)/n
    s=0
    for i in range(n):
        s += abs(F(p + dl * i + dl / 2))
    return dl*s


p=int(input("p:"))
q=int(input("q:"))
n=int(input("n:"))

print("[",p,",",q,"]")
result  = oblicz(p,q,n)

print("pole:",result)