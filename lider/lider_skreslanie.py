def j(arr):
    n = arr
    x = int(round(len(n)/2,0)) # 11
    print("lista: ",sorted(n),"#",len(n))
    print("min:",x+1)

    ile = 0
    jaka = 0
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
