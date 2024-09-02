#matriz 3x3
matriz=[
    [3, 4, 5],
    [1, 2, 6],
    [9, 7, 8]
]

#Búsqueda de un valor específico en la matriz
valor_buscado=8
def buscar_valor (matriz, valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == valor_buscado:
                return i, j

valor_buscado=8
print(buscar_valor(matriz, valor_buscado))
if valor_buscado == valor_buscado:
    print("valor encontrado en la poción", buscar_valor(matriz, valor_buscado))
else:
    print("valor no encontrado")
