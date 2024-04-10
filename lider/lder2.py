def lider(arr):
    a=sorted(arr)
    ile=0
    x=int(len(a)/2)
    kandydat= a[x]
    for i in range(len(a)):
        if a[i] == kandydat:
            ile=ile+1
    if ile>len(a)/2:
        print(kandydat)
    else:
        print('niema')

a=[1,2,6,7,4,3,1,1,1,1,1]
lider(a)