'''Dado o array np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55]), filtre e exiba apenas os elementos que são divisíveis por 10. Em seguida, substitua todos os valores maiores que 30 por zero.'''

import numpy as np

array = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55])

divisiveis_por_10 = array[array % 10 == 0]
print('Valores divisíveis por 10:', divisiveis_por_10)

maiores_que_30 = array[array > 30]

array[array > 30] = 0
print('Array após substituição de valores maiores que 30 por zero:', array)