import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
import tkinter as tk
from tkinter import filedialog


def carregar():
    file = filedialog.askopenfilename()
    df = pd.read_excel(file)
    plt.figure(figsize=(10,6))
    sns.barplot(x='mês',y='vendas', data=df)
    plt.show()


def carregar2():
    file = filedialog.askopenfilename()
    df = pd.read_excel(file)
    plt.figure(figsize=(10,6))
    sns.lineplot(x='mês',y='lucro', data=df)
    plt.show()



def carregar3():
    file = filedialog.askopenfilename()
    df = pd.read_excel(file)
    plt.figure(figsize=(10,6))
    sns.scatterplot(x='vendedor', y ='vendas', data=df)
    plt.show()    




janela = tk.Tk()


btn = tk.Button(janela, text='Vendas X Mês', command=carregar)
btn2 = tk.Button(janela, text='Lucro X Mês', command=carregar2)
btn3 = tk.Button(janela, text='Vendas X Vendedor', command=carregar3)
btn.pack()
btn2.pack()
btn3.pack()


janela.mainloop()    


