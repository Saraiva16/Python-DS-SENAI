import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk

# 1. Use plt.pie() para gráfico de pizza.
# 2. Use plt.scatter() para gráfico de dispersão.
# 3. Use plt.bar() para gráfico de barras.
# 4. Use plt.plot() para gráfico de linha.
# 5. Adicione títulos, legendas e labels aos eixos.

janela = tk.Tk()
janela.geometry('500x500')
btn_pizza = tk.Button(janela, text='Gráfico de Pizza')
btn_dispersao = tk.Button(janela, text='Gráfico de Dispersão')
btn_barras = tk.Button(janela, text='Gráfico de Barras')
btn_linha = tk.Button(janela, text='Gráfico de Linha')
btn_pizza.pack()
btn_dispersao.pack()
btn_barras.pack()
btn_linha.pack()

def grafico_pizza():
    dados = pd.read_csv('dados.csv')
    mes = dados['mes']
    vendas = dados['vendas']
    plt.pie(vendas, labels=mes, autopct='%1.1f%%')
    plt.title('Gráfico de Pizza')
    plt.show()

def grafico_dispersao():
    dados = pd.read_csv('dados.csv')
    mes = dados['mes']
    vendas = dados['vendas']
    lucro = dados['lucro']
    plt.scatter(vendas, lucro)
    plt.title('Gráfico de Dispersão')
    plt.xlabel('Vendas')
    plt.ylabel('Lucro')
    plt.show()

def grafico_barras():
    dados = pd.read_csv('dados.csv')
    mes = dados['mes']
    vendas = dados['vendas']
    plt.bar(mes, vendas)
    plt.title('Gráfico de Barras')
    plt.xlabel('Meses')
    plt.ylabel('Vendas')
    plt.xticks(rotation=45)
    plt.show()

def grafico_linha():
    dados = pd.read_csv('dados.csv')
    mes = dados['mes']
    vendas = dados['vendas']
    plt.plot(mes, vendas, marker='o')
    plt.title('Gráfico de Linha')
    plt.xlabel('Meses')
    plt.ylabel('Vendas')
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()

btn_pizza.config(command=grafico_pizza)
btn_dispersao.config(command=grafico_dispersao)
btn_barras.config(command=grafico_barras)
btn_linha.config(command=grafico_linha)

janela.mainloop()




dados = pd.read_csv('dados.csv')

mes = dados['mes']
vendas = dados['vendas']
lucro = dados['lucro']

# Gráfico de pizza
# plt.pie(vendas, labels=mes, autopct='%1.1f%%')
# plt.title('Gráfico de Pizza')
# plt.show()

# Gráfico de dispersão
# plt.scatter(vendas, lucro)
# plt.title('Gráfico de Dispersão')
# plt.xlabel('Vendas')
# plt.ylabel('mes')
# plt.show()


# Gráfico de barras
# plt.bar(mes, vendas)
# plt.title('Gráfico de Barras')
# plt.xlabel('Meses')
# plt.ylabel('Vendas')
# plt.xticks(rotation=45)
# plt.show()

# Gráfico de linha
# plt.plot(mes, vendas, marker='o')
# plt.title('Gráfico de Linha')
# plt.xlabel('Meses')
# plt.ylabel('Vendas')
# plt.xticks(rotation=45)
# plt.grid()
# plt.show()




