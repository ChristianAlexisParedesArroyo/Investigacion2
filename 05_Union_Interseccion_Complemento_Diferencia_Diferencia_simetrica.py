#Christian Alexis Paredes Arroyo   20110104  6E1
#En esta practica se muestran las operaciones con conjuntos de Unión, Intersección, Complemento, diferencia y diferencia simétrica


U = {1,2,3,4,5,6,7,8,9}  #conjunto universal
A = {1, 2, 3, 4, 5, 6}   #conjunto A
B = {2, 4, 6, 8, 1, 9}   #conjunto B

union = A | B  #Unión de conjuntos A y B
print(union)

interseccion = A & B  #Intersección de conjuntos A y B
print(interseccion)

complemento = U - A  #Complemento del conjunto A
print(complemento)

dif = A - B   #Diferencia de conjuntos A y B
print(dif)

dif_simetrica = A ^ B   #Diferencia simétrica de conjuntos A y B
print(dif_simetrica)

