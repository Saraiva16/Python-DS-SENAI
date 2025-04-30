from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import pandas as pd

url = 'https://bea3853.github.io/PROCESSO_DATA_SCIENCE/'

headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url)

sopa = BeautifulSoup(response.text, 'html.parser')

marca = []
preco = []
avaliacao = []

for dado in sopa.find_all('div', class_='produto'):
    marca.append(dado.find('h2').text)
    preco.append(float(dado.find('span', class_='preco').text.replace('R$', '').replace('.', '').replace(',','.').strip()))
    avaliacao.append(float(dado.find('span', class_='avaliacao').text))

df = pd.DataFrame({
    'Marca': marca,
    'Preço': preco,
    'Avaliação': avaliacao
})

df.to_csv('tabela.csv', index=False)

dados = pd.read_csv('tabela.csv')

# Verificar se há dados faltantes
# if dados.isnull().values.any():
#     print("Dados faltantes encontrados.")
# else:
#     print("Nenhum dado faltante encontrado.")
# OU
# dados.isnull().sum()

# Verificar se há dados duplicados
# if dados.duplicated().any():
#     print("Dados duplicados encontrados.")
# else:
#     print("Nenhum dado duplicado encontrado.")
# OU
# dados.duplicated().sum()

df = df[df['Avaliação'] > 4.0]
# print(df)

df['Marca'] = df['Marca'].str.strip()

# Preço médio por marca
preco_medio = df.groupby('Marca')['Preço'].mean().reset_index()
# print(preco_medio)

# Visualização

# HISTOGRAMA
plt.figure(figsize=(10, 6))
plt.hist(df['Preço'], bins=20, color='blue')
plt.grid(True)
plt.show()


# BARRA
preco_medio.plot(kind='bar', x='Marca', y='Preço', color='green')
plt.title('Preço Médio por Marca')
plt.xlabel('Marca')
plt.ylabel('Preço Médio')
plt.grid(True)
plt.xticks(rotation=10)
plt.show()


# SCATTER
plt.figure(figsize=(10, 6))
plt.scatter(df['Preço'], df['Avaliação'], color='red')
plt.title('Avaliação vs Preço')
plt.xlabel('Preço')
plt.ylabel('Avaliação')
plt.grid(True)
plt.show()



# INSIGHTS
# 1. A maioria dos produtos têm valor entre R$1000 e R$3000
# 2. Poucos produtos Premium
# 3. A Apple é a marca mais cara
# 4. A maioria dos produtos tem avaliação acima de 4.0
# 5. Produtos mais caros nem sempre têm a melhor avaliação
# 6. Boas opções de custo-benefício podem ser encontradas na faixa de R$1000 a R$2000


# RECOMENDAÇÕES
# 1. Aumentar estoque com melhor custo-benefício (impactar vendas)
# 2. Promoções estratégicas para produtos com avaliação média
# 3. Monitorar concorrentes para ajustar custos da Apple


# PRÓXIMOS PASSOS:
# 1. Aplicar ML para prever preços
# 2. Analisar sazonalidade
# 3. Analisar tendências de mercado
