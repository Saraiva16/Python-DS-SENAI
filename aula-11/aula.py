import matplotlib.pyplot as plt
import pandas as pd

# IMPORTAÇÃO DE DADOS
dados = pd.read_csv('dados.csv')


# EXPLORAÇÃO
df = pd.DataFrame(dados)
print(df)

print(df.head())
print(df.tail())
print(df.describe())
print(df.info())

# LIMPEZA E TRATAMENTO DOS DADOS

df = df.rename(columns={
               '2urvived': 'Sobreviventes',
               'Pclass': 'Classes',
               'Sex': 'Sexo',
               'Age': 'Idade',
               'Fare': 'Tarifa',
               }
                )

# Remover colunas desnecessárias
df = df.loc[:, ~df.columns.str.contains('zero')]
print(df)

# Análise básica:
taxa_sobrevivencia = df['Sobreviventes'].mean()
print(f'Taxa de sobrevivência: {taxa_sobrevivencia:.2%}')


# GroupBy: Associação entre as colunas

sobreviventes_por_sexo = df.groupby('Sobreviventes')['Sexo'].mean()
print(sobreviventes_por_sexo)

sobreviventes_por_classe = df.groupby('Sobreviventes')['Classes'].mean()
print(sobreviventes_por_classe)


# VISUALIZAÇÃO DOS DADOS

# barra
plt.figure(figsize=(15, 4))
plt.subplot(1, 3, 1)
df.groupby('Sexo')['Sobreviventes'].mean().plot(kind='bar')
plt.title('Sobreviventes por Sexo')

# linha
plt.subplot(1, 3, 2)
df.groupby('Classes')['Sobreviventes'].mean().plot(kind='line')
plt.title('Sobreviventes por Classe')

# histograma
plt.subplot(1, 3, 3)
plt.hist(df['Idade'].dropna(), bins=20)

plt.tight_layout()
plt.show()

