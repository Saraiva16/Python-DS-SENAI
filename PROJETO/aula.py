import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelBinarizer


# Previsão

# Análise estatística:
# Calcular medidas de tendência central
# Gerar descrição estatística dos dados
# Identificar e mostrar insights interessantes
# Modelo de machine learning (opcional para alunos avançados):
# Prever desempenho de atletas ou resultados de jogos
# Mostrar importância das características no modelo

# Funcionalidades:
# Prever chances de vitória com base em estatísticas históricas

df = pd.read_csv('player_data.csv')

df = df.dropna()



root = tk.Tk()
root.state('zoomed')
frame_grafico = tk.Frame(root)
frame_grafico.pack(pady=10, fill='both')

frame_controle = tk.Frame(root)
frame_controle.pack(pady=10)

frame_resultado = tk.Frame(root)
frame_resultado.pack(pady=10)

def limpar_frame():
    for dado in frame_grafico.winfo_children():
        dado.destroy()


def mostrar_dispersao_posicao_peso():
    limpar_frame()
    posicao = df['position'].astype(str)
    peso = df['weight']
    
    fig, ax = plt.subplots(figsize=(8,5))
    ax.scatter(peso, posicao)
    ax.set_title('POSIÇÃO X PESO')
    ax.set_xlabel('Peso (lbs)')
    ax.set_ylabel('Posição')

    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def mostrar_dispersao_posicao_altura():
    limpar_frame()
    df['height'].replace('-', '.')
    altura = df['height'].astype(str)
    posicao = df['position'].astype(str)
    
    fig, ax = plt.subplots(figsize=(8,5))
    ax.scatter(altura, posicao)
    ax.set_title('POSIÇÃO X ALTURA')
    ax.set_xlabel('Altura (ft.)')
    ax.set_ylabel('Posição')

    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def comecaram_carreira():
    limpar_frame()
    fig, ax = plt.subplots(figsize=(8,8))

    incio_carreira = df.groupby('year_start').size().sort_values()
    

    anos_selecionados = pd.concat([incio_carreira.tail(10)])

    anos_selecionados.plot(kind='bar', ax=ax, color='skyblue', edgecolor='black')
    ax.set_title('QUANTIDADE DE JOGADORES QUE COMEÇARAM SUAS CARREIRAS POR ANO')
    ax.set_xlabel('Ano de início')
    ax.set_ylabel('Quantidade de jogadores')
    plt.xticks(rotation=45)

    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def encerraram_carreira():
    limpar_frame()
    fig, ax = plt.subplots(figsize=(8,8))

    final_carreira = df.groupby('year_end').size().sort_values()
    

    anos_selecionados = pd.concat([final_carreira.tail(10)])

    anos_selecionados.plot(kind='bar', ax=ax, color='skyblue', edgecolor='black')
    ax.set_title('QUANTIDADE DE JOGADORES QUE ENCERRARAM SUAS CARREIRAS POR ANO')
    ax.set_xlabel('Ano de início')
    ax.set_ylabel('Quantidade de jogadores')
    plt.xticks(rotation=45)

    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def universidades_gerando_lendas():
    limpar_frame()
    fig, ax = plt.subplots(figsize=(8,8))

    formacao = df.groupby('college').size()

    top_universidades = pd.concat([formacao.tail(10)])

    top_universidades.plot(kind='pie', ax=ax, color=['red', 'blue', 'green'])
    ax.set_title('UNIVERSIDADES QUE FORMARAM ASTROS') 

    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def posicao_mais_e_menos_jogadas():
    limpar_frame()
    fig, ax = plt.subplots(figsize=(8,6))
    posicao_mais = df.groupby('position').size().sort_values()
    posicao_mais.plot(kind='bar', ax=ax, color='skyblue', edgecolor='black')
    
    ax.set_title('POSIÇÕES MAIS JOGADAS') 
    ax.set_xlabel('Posição')
    ax.set_ylabel('Quantidade de jogadores')
    plt.xticks(rotation=45)

    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)




# def mostrar_dispersao():
#     limpar_frame()
#     fig, ax = plt.subplots(figsize=(8, 5))
    
#     ax.scatter(df['Height'], df['Points'], alpha=0.6, color='blue')
    
#     ax.set_title('Relação entre Altura e Pontos por Jogo')
#     ax.set_xlabel('Altura (cm)')
#     ax.set_ylabel('Pontos por Jogo')    
    
#     z = np.polyfit(df['Height'], df['Points'], 1)
#     p = np.poly1d(z)
#     ax.plot(df['Height'], p(df['Height']), "r--")
    
#     canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
#     canvas.draw()
#     canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
    


btn_posicao_por_peso = ttk.Button(frame_controle, text='POSIÇÃOxPESO', command=mostrar_dispersao_posicao_peso)
btn_posicao_por_peso.grid(row=0, column=0, padx=5, pady=5)

btn_posicao_por_altura = ttk.Button(frame_controle, text='POSIÇÃOxALTURA', command=mostrar_dispersao_posicao_altura)
btn_posicao_por_altura.grid(row=0, column=1, padx=5, pady=5)

btn_comecaram_carreira = ttk.Button(frame_controle, text='INÍCIO DE CARREIRA', command=comecaram_carreira)
btn_comecaram_carreira.grid(row=0, column=2, padx=5, pady=5)

btn_encerraram_carreira = ttk.Button(frame_controle, text='FINAL DA CARREIRA', command=encerraram_carreira)
btn_encerraram_carreira.grid(row=0, column=3, padx=5, pady=5)

btn_universidades = ttk.Button(frame_controle, text='UNIVERSIDADES x ASTROS', command=universidades_gerando_lendas)
btn_universidades.grid(row=0, column=4, padx=5, pady=5)

btn_posicao_mais_e_menos_jogadas = ttk.Button(frame_controle, text='POSIÇÕES MAIS E MENOS JOGADAS', command=posicao_mais_e_menos_jogadas)
btn_posicao_mais_e_menos_jogadas.grid(row=0, column=5, padx=5, pady=5)




root.mainloop()