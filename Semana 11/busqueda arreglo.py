# Búsqueda en Arreglo Multidimensional

# Definimos una matriz 3x3 con valores numéricos
matriz = [
    [10, 25, 30],
    [5, 12, 18],
    [7, 22, 40]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):           # Recorre las filas
        for j in range(len(matriz[i])):    # Recorre las columnas
            if matriz[i][j] == valor:
                return (i, j)  # Devuelve la posición (fila, columna)
    return None  # Si no lo encuentra


# Programa principal
print("📌 Matriz:")
for fila in matriz:
    print(fila)

# Definimos el valor a buscar (puedes cambiarlo o pedir al usuario con input)
valor_buscado = int(input("\nIngrese el valor que desea buscar en la matriz: "))

posicion = buscar_valor(matriz, valor_buscado)

if posicion:
    print(f"✅ El valor {valor_buscado} se encontró en la posición: fila {posicion[0]}, columna {posicion[1]}")
else:
    print(f"❌ El valor {valor_buscado} no se encuentra en la matriz.")
