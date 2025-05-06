import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

conexao = sqlite3.connect('aula.db')
cursor = conexao.cursor()

cursor.execute('''
            CREATE TABLE IF NOT EXISTS alunos(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               idade INTEGER NOT NULL,
               curso TEXT NOT NULL
               )
               ''')

dados = [
    ('Mateus', 24, 'Ciência de Dados'),
    ('Lucas', 22, 'Engenharia de Software'),
    ('Ana', 23, 'Banco de Dados'),
    ('Maria', 25, 'Inteligência Artificial'),
    ('João', 21, 'Ciência da Computação'),
    ('Pedro', 26, 'Desenvolvimento Web'),
    ('Julia', 22, 'Segurança da Informação'),
    ('Fernanda', 24, 'Engenharia de Dados'),
    ('Roberto', 23, 'Sistemas de Informação'),
    ('Camila', 25, 'Desenvolvimento de Jogos')
]

cursor.executemany('INSERT INTO alunos (nome, idade, curso) VALUES (?, ?, ?)', dados)

conexao.commit()

cursor.execute('SELECT * FROM alunos')

alunos = cursor.fetchall()

for aluno in alunos:
    print(aluno)

conexao.close()

figure = plt.figure(figsize=(10, 5))
plt.title('Distribuição de Idades dos Alunos')
plt.xlabel('Idade')
plt.ylabel('Frequência')
df = pd.DataFrame(alunos, columns=['id', 'nome', 'idade', 'curso'])
df['idade'].value_counts().sort_index().plot(kind='bar')
plt.show()


