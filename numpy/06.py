# Acessando elementos em arrays unidimensionais

import numpy as np

arr = np.array([5, 10, 15, 20, 25])
print(arr[0])  # Acessa o 1º elemento
print(arr[-1]) # Acessa o último elemento


# Fatiamento em arrays unidimensionais
print(arr[1:4])    # entre ind. 1 e 3
print(arr[:3])     # inicio ao ind. 2
print(arr[::2])    # pula de 2 em 2
print(arr[::-1])   # array invertido

# Indexação e fatiamento em arrays multidimensionais
matriz = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

print(matriz[0, 1])
print(matriz[1:, :2])

# Modificando elementos com indexação e fatiamento
arr = np.array([10, 20, 30, 40, 50])
arr[2:4] = [100, 200]
print(arr)

# atribuindo novos valores a arrays multidimensionais
matriz = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matriz[0:2, 1:3] = [[100, 200], [300, 400]]
print(matriz)

# indexação booleana
arr = np.array([10, 20, 30, 40, 50])
filtro = arr > 20
print(arr[filtro])
print(arr[arr % 20 == 0])  # elementos multiplos de 20
