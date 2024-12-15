lista = [23, 56, 12, 7, 2, 1]
n = len(lista)


for i in range(n):
    mn_index = i
    for j in range(i + 1, n):
        if lista[j] < lista[mn_index]:
            mn_index = j
    lista[i], lista[mn_index] = lista[mn_index], lista[i]

print(lista)
