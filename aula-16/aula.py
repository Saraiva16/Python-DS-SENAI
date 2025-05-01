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


df = pd.DataFrame(organizacao_dados)

df.to_json('teste.json')

df.to_excel('teste.xlsx')

df.to_html('index.html')

df.to_markdown('i.md')


print(df.to_string())

df.to_xml('teste.xml')
