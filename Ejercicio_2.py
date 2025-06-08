#Ejercicio 2: Escriba un programa que solicite un número al usuario y
#muestre la tabla de multiplicar del 1 al 10 de ese número.

numero = int(input("Por favor, ingrese un número: "))

print(f"\nTabla de multiplicar del {numero}:")
print("-" * 20)

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")