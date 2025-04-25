import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
import tkinter as tk
from tkinter import filedialog




def carregar2():
    file = filedialog.askopenfilename()
    df = pd.read_excel(file)
    plt.figure(figsize=(10,6))
    sns.lineplot(x='meses',y='vendas', data=df)
    plt.show()


    


def carregar_des():
    file = filedialog.askopenfilename()
    df = pd.read_excel(file)
    dados = pd.DataFrame(df)
    descricao = dados.describe()
    label_describe.config(text = descricao)    



janela = tk.Tk()
janela.geometry('500x500')


btn = tk.Button(janela, text='clique', command=carregar2)
btn.pack()


btn2 = tk.Button(janela, text='clique', command=carregar_des)
btn2.pack()


label_describe = tk.Label(janela, text= '', bg='yellow', font='arial')
label_describe.pack()



janela.mainloop()    




