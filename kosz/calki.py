x=[0]
druga=[]
trzecia=[]
DOsumy=[]
suma=0


for i in range(4):
    x.append(x[i]+4)
x.append(0)

for i in range(5):
    d = int((x[i]+x[i-1])/2)
    druga.append(d)

for i in range(5):
    trzecia.append(2*pow(druga[i],2)+3*druga[i]+1)


for i in range(5):
    DOsumy.append(4*trzecia[i])

for i in DOsumy:
    suma+=i

print(x)
print(druga)
print(trzecia)
print(DOsumy)
print(suma-DOsumy[0])