arr = [2,6,3,1,6,8,12]
n = len(arr)

for i in range(1, n):
    pom = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > pom:
        arr[j + 1] = arr[j] 
        j -= 1
    arr[j + 1] = pom 

print(arr)