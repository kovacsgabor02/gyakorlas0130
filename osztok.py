import math


def osztok(szam):
    lista = []
    for i in range(2, int(math.sqrt(szam) + 1)):
        if szam % i == 0:
            lista.append(i)
    return lista


print(osztok(10007))


def dividewhile(szam):
    lista = []
    oszto = 2
    while oszto <= math.sqrt(szam):
        if szam % oszto == 0:
            oszto += 1
        return lista
