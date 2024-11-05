# indexação e fatiamento de arrays
import numpy as np

arr = np.array([10, 20, 30, 40]) # indexação básica
print(arr[0])

arr = np.array([10, 20, 30, 40, 50]) # fatiamento
print(arr[1:4])

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # fatiamento em arrays multidimensionais
print(matriz[0:2, 1:3])