import pandas as pd

df_geral = pd.read_csv('arquivo.csv')

# 1 - CRIANDO DATAFRAMES
# data = {'coluna1': [1,2,3], 'coluna2': [4,5,6]}
# df = pd.DataFrame(data)
# print(df)

# data2 = {'a': [1,2,3], 'b': [1,2,3]}
# df2 = pd.DataFrame(data2)
# print(df2)


# 2 - LISTA DE LISTAS
# data_listas = [[1,4], [2,5], [3,6]]
# df_listas = pd.DataFrame(data_listas)
# print(df_listas)


# 3 - LENDO E ESCREVENDO ARQUIVOS
# 3.1 - CSV:

# 3.1.1 - Lendo:
# df_ler_arquivos = pd.read_csv('arquivo.csv')


# print(df_ler_arquivos)

# 3.1.2 - Escrevendo:
# df_geral.to_csv('saida.csv', index=False)
# print(df_to_csv)


# 4 - VISUALIZANDO DADOS
# 4.1 - Primeiras linhas:
# df_geral.head()

# 4.2 - Últimas linhas:
# df_geral.tail()

# 4.3 - Resumo:
# df_geral.info()

# 4.4 - Estatísticas descritivas:
# df_geral.describe()



# 5 - SELECIONANDO DADOS
# 5.1 - Selecionando colunas:
# df_geral['quantidade']

# 5.2 - Selecionando linhas por rótulo
# df_geral.loc[0]

# 5.3 - Selecionando linhas por índice
# df_geral.iloc[0]



# 6 - FILTRANDO DADOS
# filtro = df_geral[df_geral['quantidade'] > 2]



# 7 - OPERAÇÕES COM COLUNAS
# 7.1 - Criando uma nova coluna:
# df_geral['nova_coluna'] = df_geral['quantidade']


