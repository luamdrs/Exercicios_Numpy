# Operações lógicas e filtragem de dados

import numpy as np

array = np.array([10, 15, 20, 25, 30])

maior_que_20 = array[array > 20]
print('Valores maiores que 20:', maior_que_20)

pares = array[array % 2 == 0]
print('Valores pares:', pares)