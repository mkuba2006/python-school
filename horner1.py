# def horner(wsp, x):
#     wynik = 0
#     for i in wsp:
#         wynik = wynik * x + i
#         print(wynik)
#     return wynik

# wsp = input("Podaj współczynniki wielomianu: ").split()

# for i in range(len(wsp)):
#     wsp[i] = int(wsp[i])

# x = int(input("wartość wielomianu: "))

# print(wsp)
# print(f"Wartość wielomianu o współczynnikach {wsp} w punkcie {x} wynosi", horner(wsp, x))






wspolczynniki = input("podaj czcynniki:").split()
x = int(input('podaj x:'))
wsp = []
for i in wspolczynniki:
    wsp.append(int(i))

wynik = 0

for i in wsp:
    wynik = wynik*x + i

print(wynik)



























