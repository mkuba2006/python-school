import math
itemy= [
    {
        "nr": 1,
        "waga": 5,
        "wart": 100

    },
    {
        "nr": 2,
        "waga": 7,
        "wart": 100
    },
    {
        "nr": 3,
        "waga": 5,
        "wart": 20
    },

]

new_arr=[]


for i in itemy:
    new_arr.append({
        "nr": i["nr"],
        "waga": i["waga"],
        "wart": i["wart"],
        "roznica": i["wart"] / i["waga"]
    })
new_arr.sort(key=lambda x: x["roznica"], reverse=True)
for i in new_arr:
    print(i)


max_waga=10
for i in new_arr:
    ile_wejdze = math.floor(max_waga/i["waga"])
    if ile_wejdze >0:
        print("nr",i["nr"], "wchodzi")
        max_waga -= i["waga"]
    else:
        print("nr",i["nr"], "nie wchodzi")