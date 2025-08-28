# Ordenación de una fila de un arreglo bidimensional (matriz)

# Definimos una matriz 3x3 con valores numéricos
matriz = [
    [9, 3, 7],
    [5, 1, 8],
    [6, 4, 2]
]

# Función para aplicar Bubble Sort a una fila específica
def bubble_sort_fila(matriz, fila):
    n = len(matriz[fila])
    for i in range(n - 1):
        for j in range(n - i - 1):
            if matriz[fila][j] > matriz[fila][j + 1]:
                # Intercambio de elementos
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]

# Programa principal
print("📌 Matriz original:")
for fila in matriz:
    print(fila)

# Selección de fila (ejemplo: fila 1 → segunda fila)
fila_a_ordenar = int(input("Ingrese el número de fila a ordenar (0, 1 o 2): "))

bubble_sort_fila(matriz, fila_a_ordenar)

print("\n✅ Matriz con la fila ordenada:")
for fila in matriz:
    print(fila)
