def j(arr):
    n = arr
    x = int(round(len(n)/2,0)) # 5
    print("lista: ",sorted(n),"#",len(n))
    print("min:",x+1)

    nowa = sorted(arr)
    print(nowa)

    ile = 0
    jaka = 0
    for i in range(len(n)):
        obecna = nowa[i];
        ile_obecna = 0
        for j in range(len(n)):
            if nowa[j] == obecna:
                ile_obecna +=1
            else:
                ile_obecna -=1
            print(obecna,'=',ile_obecna)

        if ile_obecna > ile:
            ile = ile_obecna
            jaka = obecna

    if ile > 0:
        print(jaka,": ", ile,"razy (jest liderem)")
    else:
        print("nie ma lidera")



a= [1,3,7,4,5,5,5,5,5,5] # 10
j(a)