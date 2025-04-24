import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk

dados = pd.read_csv('dados_atividade_2.csv')


janela = tk.Tk()
janela.geometry('500x400')
btn_pizza = tk.Button(janela, text='Gráfico de Pizza')
btn_dispersao = tk.Button(janela, text='Gráfico de Dispersão')
btn_barras = tk.Button(janela, text='Gráfico de Barras')
btn_linha = tk.Button(janela, text='Gráfico de Linha')
btn_estatistica = tk.Button(janela, text='Estatísticas')
btn_pizza.pack()
btn_dispersao.pack()
btn_barras.pack()
btn_linha.pack()
btn_estatistica.pack()

def grafico_pizza():
    dados = pd.read_csv('dados_atividade_2.csv')
    vendedor = dados['vendedor']
    vendas = dados['vendas']
    plt.pie(vendas, labels=vendedor, autopct='%1.1f%%')
    plt.title('Gráfico de Pizza')
    plt.show()

def grafico_dispersao():
    dados = pd.read_csv('dados_atividade_2.csv')
    vendedor = dados['vendedor']
    vendas = dados['vendas']
    plt.scatter(vendas, vendedor)
    plt.title('Gráfico de Dispersão')
    plt.xlabel('Vendas')
    plt.ylabel('vendedor')
    plt.show()

def grafico_barras():
    dados = pd.read_csv('dados_atividade_2.csv')
    vendedor = dados['vendedor']
    vendas = dados['vendas']
    plt.bar(vendedor, vendas)
    plt.title('Gráfico de Barras')
    plt.xlabel('vendedores')
    plt.ylabel('Vendas')
    plt.xticks(rotation=45)
    plt.show()

def grafico_linha():
    dados = pd.read_csv('dados_atividade_2.csv')
    vendedor = dados['vendedor']
    vendas = dados['vendas']
    plt.plot(vendedor, vendas, marker='o')
    plt.title('Gráfico de Linha')
    plt.xlabel('vendedores')
    plt.ylabel('Vendas')
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()

def mostrar_estatistica():
    media = dados['vendas'].mean()
    mediana = dados['vendas'].median()
    desvio_padrao = dados['vendas'].std()
    descricao = dados['vendas'].describe()
    estatisticas = f'Média: {media}\nMediana: {mediana}\nDesvio Padrão: {desvio_padrao}\n\nDescrição:\n{descricao}'
    estatisticas_label = tk.Label(janela, text=estatisticas)
    estatisticas_label.pack()

btn_pizza.config(command=grafico_pizza)
btn_dispersao.config(command=grafico_dispersao)
btn_barras.config(command=grafico_barras)
btn_linha.config(command=grafico_linha)
btn_estatistica.config(command=mostrar_estatistica)

janela.mainloop()