"""Crie dois arrays: um contendo os valores de 1 a 10 e outro contendo os valores de 10 a 1. Realize as seguintes operações e exiba o resultado:

Soma dos arrays
Subtração dos arrays
Multiplicação dos arrays
Divisão dos arrays"""

import numpy as np

array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
array2 = np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

soma = array1.sum() + array2.sum()
print('Soma total dos elementos:', soma)

subtracao = array1 - array2
print('Diferença entre os arrays:', subtracao)

multiplicacao = array1 * array2
print('Multiplicação elemento a elemento:', multiplicacao)

divisao = array1 / array2
print('Divisão elemento a elemento:', divisao)