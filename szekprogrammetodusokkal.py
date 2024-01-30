from Szek import Szek

peldany1 = Szek("kék", 13)
peldany2 = Szek("Piros", 4)
peldany3 = Szek("Barna", 5)
print(peldany1.__str__())
print(peldany2)
print(peldany3)


def peldanyoklistaban():
    peldany1 = Szek("kék", 13)
    peldany2 = Szek("Piros", 4)
    peldany3 = Szek("Zöld", 5)
    szekek = (peldany3, peldany2, peldany1)
    return szekek


def listakiir(szekek):
    for index in range(0, len(szekek), 1):
        print(szekek[index])

#rövid verzió
listakiir(peldanyoklistaban())

#hosszú verzió
szeklista = peldanyoklistaban()
listakiir()
