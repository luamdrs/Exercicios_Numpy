# Manipulação de formato de Arrays
# criando e mudando a forma de um array

import numpy as np

array_1d = np.array([1, 2, 3, 4, 5, 6])
print('Array 1D original:')
print(array_1d)

array_2d = array_1d.reshape(2, 3)
print('\nArray 2D após reshaping (2 linhas, 3 colunas):')
print(array_2d)

# concatenando arrays
array_a = np.array([[1, 2], [3, 4]])
array_b = np.array([[5, 6], [7, 8]])

# concatenando verticalmente
array_vert = np.vstack((array_a, array_b))
print('\nConcatenação vertical:')
print(array_vert)

# concatenando horizontalmente
array_horiz = np.hstack((array_a, array_b))
print('\nConcatenação horizontal:')
print(array_horiz)

# divindo arrays
array = np.array([[1, 2, 3], [4, 5, 6]])

# divindo o array horizontalmente
array_hsplit = np.hsplit(array, 3)
print('\nDividindo o array em 3 colunas:')
for i, arr in enumerate(array_hsplit):
    print(f'Parte {i + 1}:')
    print(arr)

# dividindo o array verticalmente
array_vsplit = np.vsplit(array, 2)
print('\nDividindo o array em 2 linhas:')
for i, arr in enumerate(array_vsplit):
    print(f'Parte {i + 1}:')
    print(arr)