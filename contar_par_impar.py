#Guardar 10  num enteros y ver cuales son pares e impares
def contar_pares_impares():
    pares = 0
    impares = 0
    for num in numeros:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

numeros = []
for i in range(10):
    num = int(input("Numero {}: ".format(i + 1)))
    numeros.append(num)

p,i = contar_pares_impares()
print("Pares.: ",p)
print("Impares: ",i)