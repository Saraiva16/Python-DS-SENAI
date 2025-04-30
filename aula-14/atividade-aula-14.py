from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import requests


url = 'https://tabelatest.netlify.app/'
resposta = requests.get(url).text
soup = BeautifulSoup(resposta, 'html.parser')

# print(soup)

idade  = [linha.find_all('td')[1].text for linha in soup.find_all('tr')[1:]]
# print(idade)

idades = [int(i) for i in idade ]
print(idade)

cidade = [linha.find_all('td')[2].text for linha in soup.find_all('tr')[1:]]
# print(cidade)


e_mails = [linha.find_all('td')[3].text for linha in soup.find_all('tr')[1:]]
print(e_mails)

nomes =  [linha.find_all('td')[0].text for linha in soup.find_all('tr')[1:]]
print(nomes)

# dicionario 


organizacao_dados = ({
 'idades':idades,
 'cidades':cidade,
 'nomes': nomes,
 'e-mail':e_mails

})

df =  pd.DataFrame(organizacao_dados)
print(df)
df.to_csv('tabela_dados.csv')

df =  pd.read_csv('tabela_dados.csv')

# print(df.describe())
# print(df.info())
# print(df.head())

# dados cadastrados 

media  =  df.groupby('cidades')['idades'].median().sort_values(ascending=False)
print(media)

idade = df.groupby('nomes')['idades'].median().sort_values(ascending=False)
print(idade)


email = df.groupby('e-mail')['idades'].median().sort_values(ascending=False)
print(email)



plt.figure(figsize=(10,6))
plt.bar(df['cidades'], df['idades'], color ='red')
plt.ylabel('IDADES')
plt.xlabel('CIDADES')
plt.show()

plt.figure(figsize=(10,6))
plt.hist(df['idades'], bins= 20, color ='red')
plt.ylabel('IDADES')
plt.xlabel('CIDADES')
plt.show()


plt.figure(figsize=(10,6))
plt.scatter(df['cidades'], df['idades'], color ='blue')
plt.ylabel('IDADES')
plt.xlabel('CIDADES')
plt.show()


plt.figure(figsize=(10,6))
plt.pie(df['idades'], labels=df['cidades'], autopct='%1.1f%%', colors =['blue','red','yellow','pink', 'green'])
plt.ylabel('IDADES')
plt.xlabel('CIDADES')
plt.show()


