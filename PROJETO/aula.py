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

# Interface gráfica deve conter:
# Gráfico de barras comparando estatísticas
# Gráfico de dispersão relacionando variáveis
# Gráfico de pizza mostrando distribuições
# Botões para alternar entre visualizações
# Previsão

# Análise estatística:
# Calcular medidas de tendência central
# Gerar descrição estatística dos dados
# Identificar e mostrar insights interessantes
# Modelo de machine learning (opcional para alunos avançados):
# Prever desempenho de atletas ou resultados de jogos
# Mostrar importância das características no modelo

# Funcionalidades:
# Comparar médias de pontos por jogador por time
# Analisar relação entre altura e desempenho
# Distribuição de jogadores por posição
# Prever chances de vitória com base em estatísticas históricas

df = pd.read_csv('player_data.csv')

root = tk.Tk()
root.geometry('400x600')
frame_grafico = tk.Frame(root)
frame_grafico.pack(pady=10, fill='both')

frame_controle = tk.Frame(root)
frame_controle.pack(pady=10)

frame_resultado = tk.Frame(root)
frame_resultado.pack(pady=10)

def limpar_frame():
    for dado in frame_grafico.winfo_children():
        dado.destroy


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
    fig, ax = plt.subplots(figsize=(8,5))

    incio_por_posicao = df.groupby('year_start')['position']
    incio_por_posicao.plot(kind='bar', color='red')
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
    
    


btn_posicao_por_peso = ttk.Button(frame_controle, text='POSIÇÃOxPESO - DISPERÇÃO', command=mostrar_dispersao_posicao_peso)
btn_posicao_por_peso.grid(row=0, column=0, padx=5, pady=5)

btn_posicao_por_altura = ttk.Button(frame_controle, text='POSIÇÃOxALTURA - DISPERÇÃO', command=mostrar_dispersao_posicao_altura)
btn_posicao_por_altura.grid(row=1, column=0, padx=5, pady=5)

btn_comecaram_carreira = ttk.Button(frame_controle, text='INÍCIO DE CARREIRA', command=comecaram_carreira)
btn_comecaram_carreira.grid(row=2, column=0, padx=5, pady=5)










root.mainloop()