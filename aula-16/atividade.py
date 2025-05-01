# Crie um planilha chamada, ‘dados.xlsx’,
# Crie o script para abrir a planilha
# Crie o script para acessar o arquivo
# Crie uma Janela para mostrar os dados da Planilha 

from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import requests
import tkinter as tk

url = 'https://tabelatest.netlify.app/'
resposta = requests.get(url).text
soup = BeautifulSoup(resposta, 'html.parser')



idade  = [linha.find_all('td')[1].text for linha in soup.find_all('tr')[1:]]
idades = [int(i) for i in idade ]
cidade = [linha.find_all('td')[2].text for linha in soup.find_all('tr')[1:]]
e_mails = [linha.find_all('td')[3].text for linha in soup.find_all('tr')[1:]]
nomes =  [linha.find_all('td')[0].text for linha in soup.find_all('tr')[1:]]





organizacao_dados = ({
 'idades':idades,
 'cidades':cidade,
 'nomes': nomes,
 'e-mail':e_mails

})

def mostar_dados_planilha():
    df = pd.DataFrame(organizacao_dados)
    df.to_excel('dados.xlsx', index=False)
    dados = pd.read_excel('dados.xlsx')
    dados_mostrados.config(text=dados)

root = tk.Tk()
root.title("Dados da Planilha")
root.geometry("1000x800")

dados_mostrados = tk.Label(root, text="")
dados_mostrados.pack()

btn = tk.Button(root, text="Mostrar Dados", command=mostar_dados_planilha)
btn.pack()






root.mainloop()




