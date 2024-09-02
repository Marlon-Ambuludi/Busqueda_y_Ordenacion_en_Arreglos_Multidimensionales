matriz=[
    [2, 5, 6],
    [3, 7, 9],
    [5, 9, 3]
]
# Ordenar una fila específica de la matriz en orden ascendente

print(matriz)

#metodo de ordenamiento buble_sort
def buble_sort(fila):
    n=len(fila)
    for i in range(n):
        for j in range(n-1, i, -1):
            if fila[j] < fila[j-1]:
                fila [j], fila[j-1] = fila[j-1], fila[j]
                print(fila)

print("matriz original")
print(matriz)
print("matriz ordenada")
buble_sort(matriz[2])
print(matriz)
