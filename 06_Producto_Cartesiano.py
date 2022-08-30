#Christian Alexis Paredes Arroyo   20110104  6E1
#En esta practica se muestra el uso del producto cartesiano


A = {"azul", "rojo", "morado", "verde"}  #conjunto A
B = {"casa", "carro"}                #conjunto B
C = {(x, y) for x in A for y in B}  #producto cartesiano

print(C)  #imprimimos el resultado del producto cartesiano
