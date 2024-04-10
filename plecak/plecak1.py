import math
items=[
    {"nr": 1,"waga": 2,"wart": 3},
    {"nr": 2,"waga": 3,"wart": 10},
    {"nr": 3,"waga": 5,"wart": 15},
    {"nr": 4,"waga": 4,"wart": 11},
    {"nr": 5,"waga": 2,"wart": 4},
]


def podziel(waga,wart):
    return round(wart/waga,2)


def storz(items):
    n = len(items)
    for i in range(n):
        for j in range(n - i - 1):
            if items[j]["iloraz"] < items[j + 1]["iloraz"]:
                pom = items[j + 1]
                items[j + 1] = items[j]
                items[j] = pom

#----------------------------------------------------------------------------------------------------------------#

maks_waga = 17
maks_wart=0
nowa_tab=[]

for i in range(len(items)):
    nowa_tab.append(
    {
        "nr": i,
        "waga": items[i]["waga"],
        "wart": items[i]["wart"],
        "iloraz": round(items[i]["wart"]/items[i]["waga"],2),#lub podziel(waga,wart)
    })



storz(nowa_tab)


for item in nowa_tab:
    warosc_jednego = round(item["wart"]/item["waga"],2) #lub podziel(waga,wart)
    ile_wejdzie = math.floor(maks_waga/ item["waga"])
    waga_wchodzacych = ile_wejdzie * math.floor(warosc_jednego)
    maks_waga -= waga_wchodzacych
    maks_wart += ile_wejdzie * item["wart"]

    print("nr",item["nr"],'o wartości',warosc_jednego,"wejdzie:",ile_wejdzie,"razy")



print("wartosc przesortowanego plecaka:",maks_wart)