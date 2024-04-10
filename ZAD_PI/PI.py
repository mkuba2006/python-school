import math
ile_w_kraw = 0
ile_w_okr = 0
n=0
arr=[]

arr_1000 = []
arr_5000 = []
pz_all=0
r=200 #promien


with open("C:/Users/3C_17/Desktop/Python/ZAD_PI/punkty.txt","r") as plik:
    a = plik.readlines()
    for i in a:
        arr.append(i.split())

for i in arr: # (123, 142)
        a=200 #ws a
        b=200 #ws b
        n =len(arr)
        x=int(i[0])
        y=int(i[1])

        wzor = pow(x-a,2) + pow(y-b,2)
        if wzor == 40000:
            ile_w_kraw+=1
        if wzor < 40000:
            ile_w_okr+=1
        if wzor > 40000:
             pz_all += 1
        
print('---------------')
print("W krawedzi: ",ile_w_kraw)
print("W okregu: ",ile_w_okr)
print("W kwadracie: ",n)
print('---------------')































#zad 2
pole_kwadratu = 40000
#dla 1000

ile_dla_1000_w_kole=0
poza = 0

for i in range(0,len(arr)):
     if i<1000:
          arr_1000.append(arr[i])

for i in arr_1000:

    xx=int(i[0])
    yy=int(i[1])
    wzor = pow(xx-a,2) + pow(yy-b,2)

    if wzor <= 40000:
        ile_dla_1000_w_kole += 1
    else:
        poza+=1

#print(ile_dla_1000_w_kole)
# print("poza:", poza)
wz = (4* ile_dla_1000_w_kole) /(poza+ ile_dla_1000_w_kole)
#print("1000:",wz)




#dla 5000

ile_dla_5000_w_kole=0
poza = 0

for i in range(0,len(arr)):
     if i<5000:
          arr_5000.append(arr[i])

for i in arr_5000:

    xx=int(i[0])
    yy=int(i[1])
    wzor = pow(xx-a,2) + pow(yy-b,2)

    if wzor <= 40000:
        ile_dla_5000_w_kole += 1
    else:
        poza+=1

#print(ile_dla_5000_w_kole)
# print("poza:", poza)
wz = (4* ile_dla_5000_w_kole) /(poza+ ile_dla_5000_w_kole)


#print(wz)
s = ile_w_kraw + ile_w_okr
wz = (4* s) /(pz_all+ s)
#print("all:",wz)