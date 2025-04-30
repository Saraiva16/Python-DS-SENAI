from bs4 import BeautifulSoup
import requests


url = 'https://gratuitos.netlify.app/'

requ = requests.get(url)
site = BeautifulSoup(requ.text, 'html.parser')
# print(site)
dados =  site.find('div', class_ = ['table-responsive', 'table table-sm bg-light text-left'])


if dados:
    tags = dados.find_all('tr')
    for n in tags:
        print(n.text)

# lista = []

# for n in dados:
#     d = site.find_all('td')
#     print(d)













