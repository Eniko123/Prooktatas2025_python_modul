def elso_feleadat():
    datum1 = datetime.datetime(2025, 12, 12)
    napok_szama = 5
    uj_datum = datum1 + datetime.timedelta(days=napok_szama)
    print(uj_datum)

import random
def masodik_feladat():
    print(random.randint(1,100))

import random
import datetime
def harmadik_feladat():
    kezdo = datetime.datetime(2000, 1, 1)
    veg = datetime.datetime(2025, 12, 31)

    napok_kozott = (veg - kezdo).days
    random_days = random.randint(0, napok_kozott)
    random_datum = kezdo + datetime.timedelta(days=random_days)
    print(random_datum)

import random
def negyedik_feladat():
    names = ["Alice", "Bob", "Charlie", "Diana"]
    print(random.choice(names))

import datetime
def otodik_feldat():
    datum1 = datetime.datetime(2025, 12, 12)
    datum2 = datetime.datetime.now()
    kulonbseg = datum1 - datum2
    print(kulonbseg.days)

import random
def hatodik_feladat():
    counter = 0
    numbers = []
    while counter < 10:
        numbers.append(random.randint(1,50))
        counter += 1
    print(numbers)

import datetime
def hetedik_feladat():
    ev, honap, nap = 2025, 7, 13
    try:
        valid_date = datetime.datetime(ev, honap, nap)
        print("Valida data")
    except:
        print("Invalid data")

import random
def nyolcadik_feladat():
    items = ["apple", "banana", "cherry", "date"]
    random.shuffle(items)
    print(items)


import datetime
def kilencedik_feladat():
    eltolas = datetime.timedelta(days = 3, hours = 4, minutes = 30)
    uj_ido = datetime.datetime.now() + eltolas
    print(uj_ido)

import datetime
def tizedik_feladat():
    datum1 = datetime.datetime(2025, 12, 12 )
    datum2 = datetime.datetime.now()
    kulonbseg = datum1-datum2
    print(kulonbseg.days)

import random
def tizenegyedik_feladat():
    print(random.uniform(1.0,10.0))

import random
def tizenkettedik_feladat():
    print(random.randint(50,100))

import random
def tizenharmadik_feladat():
    items = [1, 2, 3, 4, 5]
    random.shuffle(items)
    print(items)

import random
def tizennegyedik_feladat():
    colors = ["red", "blue", "green", "yellow"]
    minta = random.choice(colors)
    print(minta)

import random
def tizenötödik_feladat():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    minta = random.sample(numbers, 3)
    print(minta)

import datetime
def tizenhatodik_feladat():
    datum = datetime.datetime.now()
    print(datum.strftime('%Y-%m-%d %H:%M'))

import datetime
def tizenhetedik_feladat():
    datum_str = '2024-11-11'
    datum_obj = datetime.datetime.strptime(datum_str, '%Y-%m-%d')
    print(datum_obj)

import datetime
def tizennyolcadik_feladat():
    birth_date = datetime.datetime(1990, 5, 15)
    print(birth_date.strftime('%Y-%m-%d'))

import random
def tizenkilencedik_feladat():
    list = []
    counter = 0
    while counter < 5:
        list.append(random.random())
        counter += 1
    print(list)


import random
def huszadik_feladat():
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack"]
    random.shuffle(names)
    csapat1 = names[:5]
    csapat2 = names[5:]
    print(f'Első csapat emberei: {csapat1}. a második csapat emberei {csapat2}')

def main():
    elso_feleadat()
    masodik_feladat()
    harmadik_feladat()
    negyedik_feladat()
    otodik_feldat()
    hatodik_feladat()
    hetedik_feladat()
    nyolcadik_feladat()
    kilencedik_feladat()
    tizedik_feladat()
    tizenegyedik_feladat()
    tizenkettedik_feladat()
    tizenharmadik_feladat()
    tizennegyedik_feladat()
    tizenötödik_feladat()
    tizenhatodik_feladat()
    tizenhetedik_feladat()
    tizennyolcadik_feladat()
    tizenkilencedik_feladat()
    huszadik_feladat()

main()
