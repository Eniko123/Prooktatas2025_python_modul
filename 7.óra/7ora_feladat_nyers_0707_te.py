def elso_feladat():
    honapok_dic = {
        "január": 31,
        "február": 28,
        "március": 31,
        "április": 30,
        "május": 31,
        "június": 30,
        "július": 31,
        "augusztus": 31,
        "szeptember": 30,
        "október": 31,
        "november": 30,
        "december": 31
    }

    kerdes = int(input("Add meg a hónap sorszámát amelyik hossza érdekel: "))

    print(f'A kért hónap {honapok_dic[kerdes - 1]} db napból áll')



def masodik_feladat():
    szoveg = input("Kérlek adj meg egy szöveget: ")

    eredmeny = {
        'betu': 0,
        'szamjegy': 0,
        'egyeb': 0
    }

    for i in szoveg:
        if i.isalpha():
            eredmeny['betu'] += 1
        if i.isdigit():
            eredmeny['szamjegy'] += 1
        else:
            eredmeny['egyeb'] += 1

    print(eredmeny)



def negyedik_feladat()
    stat = {}

    for i in faj_lista:
        if '.' in fajl:
            kiterjesztes = faj.rspslit('.', 1)[-1].lower

            if kiterjesztes in stat:
                stat[kiterejsztes] += 1
            else
                stat[kiterejsztes] = 1

    print(stat)