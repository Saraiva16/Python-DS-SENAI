import requests
from bs4 import BeautifulSoup

url = 'https://gratuitos.netlify.app/'

requ = requests.get(url)
site = BeautifulSoup(requ.text, 'html.parser')


tabela = site.find('div', class_='table-responsive')


if tabela:
    tags_dentro_tabela = tabela.find_all('tr')
    for tag in tags_dentro_tabela:
        print(tag.text)
else:
    print("Tabela não encontrada.")