import numpy as np
# import timeit


# def soma1 ():
#     lista =  list(range(1,2000))
#     print(lista)
#     return lista

# # soma1()
# time = timeit.timeit(soma1, number=10)
# print('função1', time)

# def soma():
#     aleatorio1 =  np.random.randint(1,10,(5,10))
#     soma2  =  np.sum(aleatorio1)
#     return soma2

# time = timeit.timeit(soma, number=10)
# print('função2', time)

lista = [1,5,7,5,6,2]

ar = np.array(lista)
print(ar)

# função zeros

zeros = np.zeros(10)
print(zeros)

# função um

uns = np.ones(5)
print(uns)

# arange()

sequencia = np.arange(0,10,2)
print(sequencia)

# lineares

lineares = np.linspace(0,1,100)
print(lineares)

# exemplo ações cálculos aritiméticos

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a-b)
print(a*b)
print(a/b)

print(np.sqrt(a))
print(np.sin(b))
print(np.cos(a))
print(np.tan(a*b))

# estatistica

print(np.mean(a))
print(np.var(b))
print(np.std(a+b))

# reshape

ar = np.arange(27).reshape((3,3,3))
print(ar)

a = np.array([1,2,3,5,70,20,60,5])
filtro = a > 10
print(a[filtro])


juntar = np.concatenate((a,b))
print(juntar)