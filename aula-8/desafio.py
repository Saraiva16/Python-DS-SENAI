import numpy as np

# Desafio 1:
# 1. Crie um array de 20 elementos.

a = np.random.randint(0,100, size=(1,20))
# print(ar)

# 2. Extraia os primeiros 5 elementos, os últimos 5 
# elementos e os elementos das posições 5 a 10.

# fatiamento_um = ar[:5]
# print(fatiamento_um)
# fatiamento_dois = ar[5:10]
# print(fatiamento_dois)


# Desafio 2:
# 1. Crie duas matrizes 3x3.
# matriz_3_x_3 = np.arange(18).reshape(2,3,3)
# print(matriz_3_x_3)
# a = np.arange(9).reshape(1,3,3)
# print(a)
# b = np.arange(9).reshape(1,3,3)
# print(b)

# 2. Calcule o produto.
# print(a*b)

# Desafio 3:
# Criação de Arrays:

# Crie um array de 1 a 10.
# arr = np.arange(1,11)
# print(arr)
# Crie uma matriz 3x3 com valores aleatórios entre 0 e 1.
# c = np.random.rand(3,3)
# print(c)


# Desafio 4:
# Calcule a soma dos elementos do array.
# a = np.random.randint(0,100, size=(1,20))
# print(a)
# print(np.sum(a))
# # Encontre o valor máximo e mínimo do array.
# max, min = np.max(a), np.min(a)
# print(max, min)   


# Desafio 5:
# Calcule a média dos valores do array.
# media = np.mean(a)
# print(media)
# # Calcule a mediana dos valores do array.
# mediana = np.median(a)
# print(mediana)


# Desafio 6:
# Adicione 10 a todos os elementos do array.
# print(a)
# print(a+10)
# Reshape o array 1D para um array 2D (2x5).
# b = np.random.randint(0,10, size=(1,10))
# print(b)
# reshape = b.reshape(2,5)
# print(reshape)