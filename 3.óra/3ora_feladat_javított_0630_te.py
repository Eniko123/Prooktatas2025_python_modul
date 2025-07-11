def szorzat():
    """
    Ez a függvény megadja két szám szorzatát.
    """

    a = int(input("Adj meg egy számot: "))
    b = int(input("Adj meg egy másik számot: "))

    print(a*b)


def kisebb_dupla():
    """
    Ez a függvény megadja két szám közül a kisebb dupláját.
    """

    a = int(input("Adj meg egy számot: "))
    b = int(input("Adj meg egy másik számot: "))

    if a > b:
        print (b*2)
    else:
        print (a*2)


def paros_paratlan():
    """
    Ez a függvény eldönti, hogy egy függvény páros vagy páratlan.
    """

    a = int(input("Adj meg egy számot: "))

    if a % 2 == 0:
        print("A szám páros")
    else:
        print("A szám páratlan")


def nagyobb_triplazva():
    """
    Ez a függvény megadja két szám közül a nagyobbat triplázva.
    """

    a = int(input("Adj meg egy számot: "))
    b = int(input("Adj meg egy másik számot: "))

    if a > b:
        print(a * 3)
    else:
        print(b * 3)
