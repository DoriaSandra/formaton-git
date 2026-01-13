def liste(nbre):
    return liste(range(1, nbre+1))

nbre=int(input("entrer un nombre"))
lis=liste(nbre)
print(liste(nbre))
