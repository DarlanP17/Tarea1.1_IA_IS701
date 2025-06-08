#Ejercicio 3: Cree un programa que elimine los elementos repetidos de una
#lista y devuelva una nueva lista con elementos únicos ordenados.

lista = [4, 2, 7, 4, 2, 1, 9, 7]

lista_sin_duplicados = sorted(list(set(lista)))

print(f"Lista original: {lista}")
print(f"Lista sin duplicados: {lista_sin_duplicados}")