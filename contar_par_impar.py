#Guardar 10  num enteros y ver cuales son pares e impares
def contar_pares_impares():
    pares = 0
    impares = 0
#Aumentar cantidad si los numeros van siendo pares o impares
    for num in numeros:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

numeros = []
#Creada la lista ir añadiendo los 10 numeros enteros que el usuario ingrese
for i in range(10):
    num = int(input("Numero {}: ".format(i + 1)))
    numeros.append(num)
#Llamar la funcion e imprimir 
p,i = contar_pares_impares()
print("Pares.: ",p)
print("Impares: ",i)
#Hola Mundo #1
