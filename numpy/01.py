# Criaçao de Arrays

import numpy as np

# criando um array a partir de uma lista
lista = [1, 2, 3, 4, 5]
array = np.array(lista)
print(array)

# arrays com valores zeros e uns
zeros = np.zeros(5)
uns = np.ones((2, 3))
print(zeros)
print(uns)

# arrays com intervalos (arange e linspace)
array_arange = np.arange(0, 10, 2)    # start, stop, step
array_linspace = np.linspace(0, 5, 5) # start, stop, num
print(array_arange)
print(array_linspace)

# arrays multidimensionais
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz)

# tipo e dimensão do array
print(array.shape)
print(matriz.shape)
print(array.dtype)