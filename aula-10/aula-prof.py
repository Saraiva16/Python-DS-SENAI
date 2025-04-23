import matplotlib.pyplot as plt
import pandas  as pd
import tkinter as tk






dados  =  pd.read_csv('dados.csv')
df = pd.DataFrame(dados)
print(df.describe())
print(df.head())




def gerar_graficos():
    plt.figure(figsize=(10,15))


    plt.subplot(221)
    plt.pie(df['Vendas'], labels= df['Mês'],autopct='%1.1f%%')
    plt.xlabel('eixo x')
    plt.ylabel('eixo y')
    plt.title('GRAFICO DE PIZZA')


    plt.subplot(222)
    plt.scatter(df['Vendas'], df['Mês'])
    plt.xlabel('eixo x')
    plt.ylabel('eixo y')
    plt.title('GRAFICO DE DISPERSÃO')


    plt.subplot(223)
    plt.bar(df['Mês'], df['Vendas'])
    plt.xlabel('eixo x')
    plt.ylabel('eixo y')
    plt.title('GRAFICO DE BARRAS')


    
    plt.subplot(224)
    plt.plot(df['Vendas'], df['Mês'])
    plt.xlabel('eixo x')
    plt.ylabel('eixo y')
    plt.title('GRAFICO DE LINHAS')


    plt.show()



gerar_graficos()


# 1. Gráfico de Pizza: Mostre a distribuição de vendas por mês.
# 2. Gráfico de Dispersão: Relacione vendas e lucro.
# 3. Gráfico de Barras: Compare vendas por mês.
# 4. Gráfico de Linha: Mostre a evolução do lucro ao longo dos meses.