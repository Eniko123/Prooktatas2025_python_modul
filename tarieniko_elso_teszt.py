def elso_feladat():
    """"
    Ez a függvény 1-10ig képes befogadni számokat, és megszámolni, melyik számból hányat kapott.
    """

    bemenet = input("Adj meg egy egész számot 1-10ig")
    pontok = []

    while bemenet != "":
        pontok.append(int(bemenet))
        bemenet = input("Adj meg egy egész számot 1-10ig")

    szamlalo = [0] * 10    #Ez 10db számláló, amiknek indexe 0-9

    for c in pontok:
        szamlalo[c-1] += 1  # A számot az egyel ksiebbi indexű számlálóhoz adom.


    for i in range(10):
        print(f' {i+1} : {szamlalo[i]} db.')



def masodik_feladat():
    """"
    Ez a függvény eldönti, hogy egy év szökőév-e vagy sem.
    """

    evszam = int(input("Ajd meg egy évszámot, amiről eldöntenéd szükőév-e: "))

    if (evszam % 4 == 0 and evszam % 100 != 0) or (evszam % 400 == 0):
        print("Ez az év szökőév.")
    else:
        print("Ez az év nem szökőév.")



def harmadik_feladat():
    """
    Ez a függvény átlagot számol egy listából és kiszűti azokat amenyek az átlagnál kisebbek.
    """

    szamok = [24, 31, 22, 43, 10, 84, 38, 44, 84, 56, 67, 51, 56, 84, 31, 65, 69, 83, 39]
    szum = 0
    db = 0
    for x in szamok:
        szum += x
        db += 1
    atlag = szum / db
    szurt = []
    for x in szamok:
        if x < atlag:
            szurt.append(x)
    print(szurt)

def atlag(szamok):
   return sum(szamok)/len(szamok)

def szures(szamok, atlag):
    szurt = []
    for x in szamok:
        if x < atlag:
            szurt.append(x)
    return szurt

def alap():
    szamok = [24, 31, 22, 43, 10, 84, 38, 44, 84, 56, 67, 51, 56, 84, 31, 65, 69, 83, 39]

    atl = atlag(szamok)
    szrs = szures(szamok, atl)

    print(f'Az adott számsorozatban az alábbi elemek kisebbek mint az átlag: {szrs}')



def negyedik_feladat(szo, pozicio, uj_betu):
    """
    Ez a függvény módosít egy stringet a megadott paraméterek alapján
    """

    return szo[:pozicio] + uj_betu + szo[pozicio + 1:]

def string_mod():
    szo = "papa"
    pozicio = 1
    uj_betu = "i"

    muvelet = negyedik_feladat(szo, pozicio, uj_betu)

    print(muvelet)














