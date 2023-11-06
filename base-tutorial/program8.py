nombres = ["Juan","Maria","Pedro","Ana","Luis"]
#
nombres.insert(2, "Emilio")
#
for nombre in nombres:
    print(nombre)
#
#
#
suma = 0
i = 0
numeros = [5, 4, 3, 2, 1]
numeros.append(6)
#
#print(numeros[0])
#
while (i < len(numeros)):
    suma = suma + numeros[i]
    i = i + 1
#
print("La suma de los elementos es:",suma)