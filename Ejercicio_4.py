#Ejercicio 4: Escriba un programa que solicite ingresar el nombre de varios
#estudiantes y su nota, y lo almacene en un diccionario. Al final, muestra los
#datos almacenados.

estudiantes = {}

while True:
    nombre = input("Ingrese el nombre del estudiante (o fin para terminar): ")
    if nombre.lower() == "fin":
        break

    while True:
        try:
            nota = float(input("Ingrese la nota del estudiante: "))
            if 0 <= nota <= 100:
                break
            else:
                print("La nota debe estar entre 0 y 100.")
        except ValueError:
            print("Por favor ingrese un numero")

    estudiantes[nombre] = nota

print(estudiantes)