a = [
    [0, 0, 1, 1, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
]

def idol(a):
    n=len(a)
    kandydat = 0
    jest_kandydat = False
    while kandydat < n and not jest_kandydat:
        i = 0
        a[kandydat][kandydat] = False
        while i < n and not a[kandydat][i]:
            i += 1
        if i == n:
            jest_kandydat = True
        else:
            kandydat += 1
        
    if jest_kandydat == False:
        return -1
    
    i=0
    a[kandydat][kandydat] = True
    while i < n and a[i][kandydat]:
        i +=1
    if i == n:
        return kandydat
    else:
        return -1
    
print(idol(a))