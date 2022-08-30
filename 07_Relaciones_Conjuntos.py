#Christian Alexis Paredes Arroyo   20110104  6E1
#En esta practica se muestra las relaciones de conjuntos

A={1,2,3}  #conjunto A
B={"a","b","c","d"}  #conjunto B

C = {(x, y) for x in A for y in B} #producto cartesiano de A y B

R1={(1,"d"), (3,"c")}  #Tiene relacion con el producto cartesiano de A y B

if R1.issubset(C):  
    print("Tienen relacion")
else:
    print("No tienen relacion")


R2={(1,"f"), (3,"c")}  # No tiene relacion con el producto cartesiano de A y B

if R2.issubset(C):  
    print("Tienen relacion")
else:
    print("No tienen relacion")
