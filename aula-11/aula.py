import tkinter as tk

janela = tk.Tk()
janela.geometry('500x500')

texto = tk.Label(janela, text='Isso é um texto!', bg='lightgreen')
texto.pack()

entry_text = tk.Entry(janela)
entry_text.pack()

btn = tk.Button(janela, text='Clique aqui')
btn.pack()


janela.mainloop()


# Widgets: Botão, input, texto na interface
# Frames: Espaços para guardar infos
# Tree




