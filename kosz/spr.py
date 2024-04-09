arr= [
    [1,1,1],
    [1,2,3],
    [1,2,3],
]

all =[]
for row in arr:
    for i in row:
        all.append(i)


def sor(all):
    for i in range(len(all)):
        for j in range(len(all) - i - 1):
            if all[j] < all[j + 1]:
                pom = all[j + 1]
                all[j + 1] = all[j]
                all[j] = pom
    print(all)
sor(all)





















def row_col(arr):
    row_arr= []
    col_arr= []

    for row in arr:
        suma_w_row=0
        for el in row:
            suma_w_row += el
        row_arr.append(suma_w_row)

    print('------')
    columny = list(zip(*arr))
    for col in columny:
            suma_w_col=0
            for el in col:
                suma_w_col += el
            col_arr.append(suma_w_col)
    
    for i in range(len(row_arr)):
         if row_arr[i] == col_arr[i] :
              print("tak")
              break
         else:
            print("nie")
            break



# row_col(arr)