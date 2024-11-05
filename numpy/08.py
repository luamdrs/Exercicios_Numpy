# Operações básicas de agregação

import numpy as np

# array 2D
array = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

soma_total = array.sum()
print('Soma total:', soma_total)

media_total = array.mean()
print('Média total:', media_total)

maximo = array.max()
minimo = array.min()
print('Máximo:', maximo)
print('Mínimo:', minimo)


# Agregacoes por eixo

# soma de cada coluna (eixo 0)
soma_colunas = array.sum(axis=0)
print('\nSoma de cada coluna:', soma_colunas)

# media de cada linha (eixo 1)
media_linhas = array.mean(axis=1)
print('Média de cada linha:', media_linhas)


# Funções estatisticas adicionais

# desvio padrão (std)
desvio_padrao = array.std()
print('\nDesvio Padrão:', desvio_padrao)
# variância (var)
variancia = array.var()
print('Variância:', variancia)