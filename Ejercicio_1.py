#Ejercicio 1: Calcular el número mayor de una lista sin usar max
#Cree un programa que reciba una lista de números y
#devuelva el número mayor sin usar la función max()

entrada = input("Ingrese números separados por espacios: ")

lista = [int(numero) for numero in entrada.split()]
print(lista)

if lista: #Este if es para verificar si la lista no esta vacia
    mayor = lista[0]
    for numero in lista:
        if numero > mayor:
            mayor = numero
    print("El número mayor es:", mayor)
else:
    print("La lista está vacía")