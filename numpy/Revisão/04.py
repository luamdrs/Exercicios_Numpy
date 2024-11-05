'''Crie um array de 50 números aleatórios entre 0 e 1. Calcule e exiba a média, o desvio padrão, o valor mínimo e o valor máximo do array.'''

import numpy as np

arr = np.random.rand(50)

media = arr.mean()
desvio_padrao = arr.std()
valor_minimo = arr.min()
valor_maximo = arr.max()

print('Média:', media)
print('Desvio padrão:', desvio_padrao)
print('Valor mínimo:', valor_minimo)
print('Valor máximo:', valor_maximo)