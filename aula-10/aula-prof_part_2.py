import matplotlib.pyplot as plt
import pandas  as pd
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def gerar_():
    dados = pd.read_csv('dados.csv')
    DF = pd.DataFrame(dados)
    des = DF.describe()
    texto.config(text=des)
    
    lucro = dados['lucro']
    mes = dados['mes']


    fig, grafico = plt.subplots()
    grafico.plot(mes,lucro,marker = 'o',linestyle='-')
    


    canvas = FigureCanvasTkAgg(fig, master=janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True) 
  
janela = tk.Tk()



btn = tk.Button(janela, text = 'Clique aqui', command=gerar_)
btn.pack(pady=20)



texto =  tk.Label(janela,text='')
texto.pack()



janela.mainloop()