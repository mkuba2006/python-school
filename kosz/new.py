import random
arr =[]
for i in range(10):
    arr.append(random.randint(-50,100))
print(min(arr))
print(max(arr))