#Encontrar el valor maximo y minimo de una lista
def maximo_manual(lista):
    #Si la lista esta vacia retorna 0
    if len(lista) == 0:
        return None
    maximo = lista[0]
    for num in lista [1:]:
        #Si el numero es mayor al maximo anterior, se reemplaza por el nuevo maximo
        if num > maximo:
            maximo = num
    return maximo
def minimo_manual(lista):
    if len(lista) == 0:
        return None
    minimo = lista[0]
    for num in lista :
        #Lo mismo, si es menor que el actual, lo actuliza por el nuevo minimo
        if num < minimo:
            minimo = num
    return minimo

numeros = []
for i in range(8):
    valor = int(input(f"Numero {i+1}: "))
    numeros.append(valor)
mayor_manual = maximo_manual(numeros)
menor_manual = minimo_manual(numeros)

print ("Mayor (manual): ", mayor_manual)
print ("Menor (manual): ", menor_manual)
#Hola mundo #3
