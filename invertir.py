#Invertir el orden de una lista manualmente
def invertir_manual(lista):
    invertida = []
    #Recorrer la lista desde el ultimo elemento hasta el primero y añadirlo a la nueva lista
    for i in range(len(lista)-1, -1, -1):
        invertida.append(lista[i])
    return invertida
#Crear la lista e ir añadiendo los numeros que se ingresen
numeros = []
for i in range(6):
    valor = int(input(f"Numero {i+1}: "))
    numeros.append(valor)
print ("Original: ", numeros)
invertida = invertir_manual(numeros)
print ("Invertida: ", invertida)
#Hola Mundo #4
