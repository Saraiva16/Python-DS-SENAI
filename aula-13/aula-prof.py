import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

url =  'https://bea3853.github.io/site_teste_2/'

dados = requests.get(url)
# print(dados)
site = BeautifulSoup(dados.text,'html.parser')
# print(site)
valores_site = site.findAll('span')
nome = site.findAll('h1')
# print(nome)

valores = []
nomes = []
v = []
valores_novos = []
for i in valores_site:
    valores.append(i.text)
    valores_novos = [valor.replace('R$','').strip() for valor in valores]
    valores_novos = [valor2.replace(',','.').strip() for valor2 in valores_novos]
for novos_dados in valores_novos:
        v.append(float(novos_dados))


for x in nome:
      nomes.append(x.text)
    #   print(nomes)
nomes.remove('PRODUTO DA LOJA')

print(nomes)
print(v)


# fig, ax = plt.subplots(10,6)

plt.bar(nomes,v, label = a , color ='red')

plt.yticks(v)

plt.show()






