#Ejercicio 5: Sumar ventas por producto

ventas = {
    'Producto': ['A', 'B', 'A', 'C', 'B', 'A'],
    'Cantidad': [10, 5, 7, 3, 2, 8]
}

total_por_producto = {}

#Se utiliza zip para iterar las 2 listas a la vez
for producto, cantidad in zip(ventas['Producto'], ventas['Cantidad']):
    if producto in total_por_producto:
        total_por_producto[producto] += cantidad
    else:
        total_por_producto[producto] = cantidad

print(total_por_producto)