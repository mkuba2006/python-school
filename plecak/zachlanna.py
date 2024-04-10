import random

dl = 4
tab = []
def stworz_tablice(dl):
    for i in range(dl):
        row = []
        for j in range(dl):
            liczba = random.randint(1,7)
            row.append(liczba)
        row.append(0)
        tab.append(row)
        print(row)
        row = []
stworz_tablice(dl)

tab.append([0,0,0,0,0])
print([0,0,0,0,0])
suma = tab[0][0]


w=0
k=0
z=[]
n = len(tab)
print("n:",2*n-2)


for i in range(1, 2*n-2):
    if tab[w+1][k] > tab[w][k+1]:
        suma += tab[w+1][k]
        z.append(tab[w+1][k])
        w += 1
    else:
        suma += tab[w][k+1]
        z.append(tab[w][k+1])
        k +=  1
    
print(suma)
print(z)