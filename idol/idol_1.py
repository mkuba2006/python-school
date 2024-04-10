import random

def policz_sume(arr):
    print(arr)
    czy = False
    max = 0
    for x in arr:
        ile = arr.count(x)
        if(ile >1):
            czy = True
            max = ile
    if(czy):
        print("jest",max, "tych samych sum")



rows = 3
table = []
sumy = []
liczby = []


for i in range(rows):
    row = []
    suma=0
    for j in range(rows):
        rand = random.randint(0, 9)
        row.append(rand)
        suma += rand
        liczby.append(rand)
    
    sumy.append(suma)
    row.sort()
    table.append(row)
    print(row,"suma:",suma)
    suma=0



def na_kolumny(table):
    columny = []
    for i in range(len(table)):
        columna = []
        for j in range(len(table)):
            columna.append(table[j][i])
        columny.append(sorted(columna))
    return columny







# print(sumy)
# print(liczby)
policz_sume(sumy)
wynik = na_kolumny(table)
policz_sume(wynik)