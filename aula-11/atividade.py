# 1. Acesse: https://www.kaggle.com/
# 2. Faça sua conta 
# 3. Extraia um data frame 
# 4. Extraia as 5 primeiras linhas
# 5. Mostre um gráfico de pizza
# 6. Relacione dados
# 7. Trate o Data Frame

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


dados = pd.read_csv('dados_atividade.csv')

df = pd.DataFrame(dados)
print(df)

print(df.head())

df = df.rename(columns={
    'age': 'Idade',
    'gender': 'Sexo',
    'study_hours_per_day': 'Horas estudadas por dia',
    'social_media_hours': 'Horas em redes sociais'
})

contagem_sexo = df['Sexo'].value_counts()
plt.figure(figsize=(10, 5))
plt.pie(contagem_sexo, labels=contagem_sexo.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribuição por Sexo')
plt.show()
