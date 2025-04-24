import matplotlib.pyplot as plt
import pandas as pd

# leitura do arquivo csv

dados  = pd.read_csv('train_and_test2.csv')


# Exploração 

# print(dados.head())
# print(dados.info())
# print(dados.describe())

# limpeza e tratamento dos dados

# df =  pd.DataFrame(dados)
# print(df)

# renomenado 
dados = dados.rename(columns={
    '2urvived':'Sobreviventes',
    'Pclass':'Classes',
    'Sex':'Sexo',
    'Age':'Idade',
    'Fare':'Tarifa'
}
)

# remover colunas desnecessárias

dados = dados.loc[:, ~dados.columns.str.contains('zero')]

# print(f'{round(dados.head(),2)}')
# print(round(dados.info(),2))
# print(round(dados['Idade'].describe(),2))
# print(dados['Classes'].describe())

# # analise básica: 

# taxa_sobrevivencia = dados['Sobreviventes'].mean()
# print('Média de sobreviventes Titanic', taxa_sobrevivencia)


# groupby associação entre as colunas 


sobreviventes_por_sexo = dados.groupby('Classes')['Tarifa'].std()
print(sobreviventes_por_sexo)

sobreviventes_por_classe = dados.groupby('Classes')['Sobreviventes'].mean()
print('Por classe:', sobreviventes_por_classe)

# visualização dos dados

plt.figure(figsize=(15,4))


# line
plt.subplot(1,3,1)
dados.groupby('Sexo')['Sobreviventes'].mean().plot(kind='bar', color='red')
plt.title('SOBREVIVENTES POR SEXO')

# bar
plt.subplot(1,3,2)
dados.groupby('Classes')['Sobreviventes'].mean().plot(kind='bar')
plt.title('SOBREVIVENTES POR CLASSE')

# hist

# df = pd.DataFrame(dados)

plt.subplot(1,3,3)
plt.hist(dados['Idade'].dropna(), bins=20)


plt.tight_layout()
plt.show()





