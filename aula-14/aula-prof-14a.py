from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import pandas as pd



URL  =  'https://bea3853.github.io/PROCESSO_DATA_SCIENCE/'

headers = {'User-Agent':'Mozilla/5.0'}

response = requests.get(URL)

soup = BeautifulSoup(response.text,'html.parser')

# print(soup)

nome = []
preco = []
avaliacao = []

for dado in soup.find_all('div', class_='produto'):
    nome.append(dado.find('h2').text)
    preco.append(float(dado.find('span', class_='preco').text.replace('R$','').replace('.','').replace(',','.')))
    avaliacao.append(float(dado.find('span', class_ = 'avaliacao').text))

    
# print(avaliacao)

# df
df  = pd.DataFrame({
    'Modelos':nome,
    'Preço':preco,
    'Avaliação':avaliacao
})

df.to_csv('tabela.csv', index=False)

df  =  pd.read_csv('tabela.csv')

# verificar se existem dados faltantes:

df.isnull().sum()


# limpeza - remover dados duplicados
df['Modelos'][4] = 'Apple'
# print(df)

df = df.drop_duplicates()

# print(df)
df = df[df['Avaliação']>4]

# print(df)

# print(df.describe())


df['Modelos'] = df['Modelos'].str.split().str[0]


# print(df)


# preco medio por marca 
df.describe()
# print()

preco_media  =  df.groupby('Modelos')['Preço'].mean().sort_values()

print('valores media :',preco_media)



# visualização 


plt.figure(figsize=(10,6))
plt.hist(df['Preço'], bins = 20, color='green', edgecolor = 'black')
plt.grid(True)
plt.show()


plt.figure(figsize=(10,6))
preco_media.plot(kind = 'bar', color = 'red')
plt.xlabel('Marca')
plt.ylabel('Valores')
plt.grid(True)
plt.xticks(rotation = 50)
plt.show()


plt.figure(figsize=(10,6))
plt.scatter(df['Preço'], df['Avaliação'], color = 'green')
plt.xlabel('Preço')
plt.ylabel('Avaliação')
plt.grid()
plt.show()



# insight:

# a maioria dos celulares estão na faixa de 1000 à  3000
# Poucos produtos Premiums


# A ipple tem o preço mais alto 
# Samsung e Xiomi dominam a faixa intermediaria 


# Produtos mais caros nem sempre tem a melhor avaliação 
# Boas opçoes de custo beneficio podem ser encontradasa na faixa de 1.500 à 2.500




# ação a tomade de decisão: 

# aumentar o estoque com melhor custo - beneficios (impactar aumento aumento de vendas)
# Promoçoes estratéticas para produtos de avaliação média
# monitorar concorrentes para ajustar os custos da ipple

# proximos passos:
# aplicar ml para prever tendencias de preço 




