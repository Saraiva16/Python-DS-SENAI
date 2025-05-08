from sklearn.linear_model import LinearRegression
import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog
import numpy as np



def carregar():
    file_caminho = filedialog.askopenfilename(filetypes=[('CSV files', '*.csv')])
    if file_caminho:
        global df
        df = pd.read_csv(file_caminho)
        label_status.config(text='CSV CARREGADO COM SUCESSO')

def previsao():
    X = np.array(df.index).reshape(-1,1)
    y = df['Tempo_espera']

    modelo = LinearRegression()
    modelo.fit(X, y)

    previsao_espera = modelo.predict([[len(df)+1]])
    label_previsao.config(text=f'{previsao_espera[0]:.2f} minutos')

def carregar_dispersao():
    fig, ax = plt.subplots(figsize=(6,4))
    ax.scatter(df['Tempo_espera'], df.index, color='red')
    canvas = FigureCanvasTkAgg(fig,master=frame_grafico)
    canvas.get_tk_widget().pack(side='left', padx=10)
    canvas.draw()

def carregar_linhas():
    fig, ax = plt.subplots(figsize=(6,4))
    ax.bar(df['Tempo_espera'], df.index, color='green')
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.get_tk_widget().pack(side='left', padx=10)
    canvas.draw()

def analisar_estatisticas():
    descrever = df['Tempo_espera'].describe()
    media = df['Tempo_espera'].mean()
    mediana = df['Tempo_espera'].median()
    desvio = df['Tempo_espera'].std()
    print(f'Detalhes: {descrever}\nMédia tempo de espera: {media}\nMediana: {mediana}\nDesvio: {desvio}')

# Janelas

root = tk.Tk()

root.geometry('1800x900')
root.title('DASHBOARD DE ATENDIMENTO')

frame_grafico = tk.Frame(root)
frame_grafico.pack(pady=20, side='top', fill='x')


# Botões

btn_linhas = tk.Button(root, text='Linhas', command=carregar_linhas)
btn_linhas.pack(pady=5, side='top')

btn_dispersao = tk.Button(root, text='Dispersão', command=carregar_dispersao)
btn_dispersao.pack(pady=5, side='top')

btn_previsao = tk.Button(root, text='Previsão para ser atendido', command=previsao)
btn_previsao.pack(pady=5, side='top')

btn_carregar = tk.Button(root, text='Carregar dados', command=carregar)
btn_carregar.pack(pady=5, side='top')

btn_estatisca = tk.Button(root, text='Análise estatística', command=analisar_estatisticas)
btn_estatisca.pack(pady=5, side='top')


# Labels

label_previsao = tk.Label(root)
label_previsao.pack(pady=5, side='top')

label_status = tk.Label(root, text='Carregue os dados para iniciar')
label_status.pack(pady=5, side='top')



root.mainloop()
