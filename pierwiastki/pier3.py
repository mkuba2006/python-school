def sprawdz(num):
    a = 1
    b = num
    while abs(a - b) >= 0.000001:
        a, b = (a + b) / 2, num / a

    return (a + b) / 2

num = int(input("x:"))
print(sprawdz(num))