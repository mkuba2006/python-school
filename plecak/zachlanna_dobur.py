import random
arr= []
l = 20
for i in range(l):
    arr.append(random.randint(1, 50))

arr.sort()


pierwsza = arr[0]
max = 25
new = []


for i in arr:
    if i + pierwsza <= max:
        new.append(i)


print(new)

n = len(new)//2 +1
print(n)


ile=0
if(len(new)>1):

    for i in range(n):
        if new[i]+new[-i-1] <= max:
            if new[i] == new[-i-1]:
                ile+=0
            else:
                print(new[i],"-",new[-i-1],"=",new[i]+new[-i-1])
                ile+=1
else:
    print("brak")

print("par:",ile)