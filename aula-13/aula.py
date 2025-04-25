import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = 'https://bea3853.github.io/site_teste_2/'

dados = requests.get(url)
# print(dados)

site = BeautifulSoup(dados.text, 'html.parser')
# print(site)

valores_site = site.find_all('span')
nome = site.find_all('h1')

nomes = []
valores = []
nome = []
v = []
valores_novos = []

for i in valores_site:
    valores.append(i.text)
    valores_novos = [valores.replace('R$', '') for valores in valores]
    valores_novos = [valores.replace(',', '.') for valores in valores_novos]
    valores_novos = [valores.replace(' ', '') for valores in valores_novos]
for novos_dados in valores_novos:
    v.append(float(novos_dados))


for x in nomes:
    nomes.append(x.text)


print(nomes)
print(v)

fig, ax = plt.subplots(10,6)
plt.bar(nomes, v)
plt.yticks(rotation=90)
plt.show()