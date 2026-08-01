#Sumar los numeros de una lista manual y con sum()
def sumar_lista(lista):
    suma = 0
    #sumar manualmente los numeros 
    for num in lista:
        suma += num
    return suma

numeros = []
#Crear la lista e ir añadiendo los numeros que se ingresen
for i in range(5):
    valor = int(input(f"Ingrese numero {i+1}: "))
    numeros.append(valor)
    
total = sumar_lista(numeros)
#sumados usando la funcion prederminada
total_sum = sum(numeros)
print("Suma con bucle: ", total)
print("Suma con sum(): ", total_sum)
#Hola mundo #2
