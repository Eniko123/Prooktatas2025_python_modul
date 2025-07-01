def szorzat():
    a = int(input("Adj meg egy számot: "))
    b = int(input("Adj meg egy másik számot: "))

     if not isinstance(a, int) or not isinstance(b, int):
        print ("Csak egész számokat fogad el!")
     return: a * b

def kisebb_dupla():
    a = int(input("Adj meg egy számot: "))
    b = int(input("Adj meg egy másik számot: "))

    if a > b:
        print (b*2)
    else:
        print (a*2)


def paros_paratlan():
    a = int(input("Adj meg egy számot: "))

    if a % 2 == 0:
        print("A szám páros")
    else:
        print("A szám páratlan")

paros_paratlan()
    a = int(input("Adj meg egy számot: "))
    b = int(input("Adj meg egy másik számot: "))

    if a > b:
        print(a * 3)
    else:
        print(b * 3)


