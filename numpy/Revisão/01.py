# Crie um array com 20 números aleatórios entre 1 e 100. Em seguida, transforme esse array em uma matriz 4x5.

import numpy as np

array = np.random.randint(1, 101, size=20)
print('Array original de 20 números aleatórios:')
print(array)

matriz_4x5 = array.reshape(4, 5)
print('Resultado ~ Matriz 4x5:')
print(matriz_4x5)