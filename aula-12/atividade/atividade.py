import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
import tkinter as tk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



def carregar():
    file = filedialog.askopenfilename()
    df = pd.read_excel(file)
    plt.figure(figsize=(10,6))
    sns.lineplot(x='Meses',y='Vendas', data=df)
    plt.show()
    dados = pd.DataFrame(df)
    descricao = dados.describe()
    label_describe.config(text=descricao)


janela = tk.Tk()
janela.title('Vendas X Mês')
janela.geometry('500x500')

btn = tk.Button(janela, text='Vendas X Mês', command=carregar)
btn.pack()

label_describe = tk.Label(janela, text='')
label_describe.pack()

janela.mainloop()