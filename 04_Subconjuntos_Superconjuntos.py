#Christian Alexis Paredes Arroyo   20110104  6E1
#En esta practica se muestra un subconjunto y superconjunto

A = {1, 2, 3, 4}   #conjunto A
B = {1, 2}        #conjunto B


if B.issubset(A):  #Se compara para saber si B es subconjunto de A
    print("B en un subconjunto\n")
elif B.issuperset(A):  #Se compara para saber si B es superconjunto de A
    print("B en un superconjunto\n")
else:
    print("B no es subconjunto ni superconjunto de A\n")


if A.issubset(A):   #Se compara para saber si A es subconjunto de A
    print("A en un subconjunto")
if A.issuperset(A):   #Se compara para saber si A es superconjunto de A
    print("A en un superconjunto")
else:
    print("B no es subconjunto ni superconjunto de A")
#se puede confirmar que A es un conjunto y superconjunto de A
