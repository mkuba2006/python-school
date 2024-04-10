def j(arr):
    n = arr
    x = int(round(len(n)/2,0)) # 11
    print("lista: ",sorted(n),"#",len(n))
    print("min:",x+1)

    ile = 0
    jaka =0
    for i in n:
        z = n.count(i)
        if z > ile:
            jaka = i
            ile = z

    if ile > x:
        print(jaka,": ", ile,"razy (jest liderem)")
    else:
        print("nie ma lidera")
    print('------------------------')





a= [1,1,2,5,3,6,8,4,5,6,6,6,6,6,6,6,6,6,6] # 18
b= [1,3,7,4,3,5,5,5,5,5,5,5] # 12
c= [1,2,3,4,56,7,7,8] # 8 
j(a)
j(b)
j(c)