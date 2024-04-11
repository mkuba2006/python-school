
a=10
b=500
p=a*b
licznik=0
while abs(b-a) >0.0001:
    a= ((a+b)/2)
    b=p/a
    print(b, pow(b,2))
    licznik +=1

print("licznik:", licznik)