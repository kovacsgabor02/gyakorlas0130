def labakszama():
    print("Hány 4-nél több lábú szék van: ")
    db = 0
    for index in range(0, len(szekek), 1):
        if szekek[index].labszam > 4:
            db += 1

    print(db)

def pirosnegylabu():
    print("Van-e négy lábú piros szék: ")
    van = False
    for index in range(0, len(szekek), 1):
        van = True
    if van:
        print("Van")
    else:
        print("Nincs")
pirosnegylabu()

