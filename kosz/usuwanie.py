n= [1,1,2,5,3,6,8,4,5,6,6,6,6,6,6,6,6,6,6]
x=[]
for i in n:
    if i not in x:
        x.append(i)
print(sorted(x))
print(sorted(n))



def j(a, x):

    for i in x:
        x= a.count(i)
        print(i,":",x,"razy")
    print('------------------------')




j(n,sorted(x))