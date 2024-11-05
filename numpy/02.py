# Operacoes aritmeticas com arrays

import numpy as np 

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

soma = a + b        
produto = a * b     
subtracao = a - b   

print('Soma:', soma)
print('Produto:', produto)
print('Subtração:', subtracao)

# Operacao com um valor escalar
multiplicacao_por_escalar = a * 2
print('Multiplicação por escalar:', multiplicacao_por_escalar)