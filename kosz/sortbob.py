el = [7, 3, 1, 2, 5]
size = len(el)

print("Before sorting:", el)

for i in range(size):
    for j in range(0, size-i-1):
        if el[j] > el[j+1]:
            el[j], el[j+1] = el[j+1], el[j]

print("After sorting:", el)