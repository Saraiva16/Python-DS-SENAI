import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1 - Carregamento dos dados

df = pd.read_csv('student_habits_performance.csv')

print(df.head())
print(df.info())
print(df.describe())

# df = pd.DataFrame(df)

# 2 Exploração inicial 
# 3 Limpeza e tratamento de df

df = df.rename(columns = {
  'age':'Idade',
  'netflix_hours':'horas_netflix',
  'social_media_hours':'Horas_midias',
  'sleep_hours':'horas_sono' ,
  'gender':'genero',
  'study_hours_per_day':'horas_estudo_por_dia',
  'part_time_job':'trabalha_estuda'

})

print(df['genero'])
# df = df.loc[:,~df.columns.str.contains('')  ]


#  4 análise

# relacionar horas de netiflix com horas age
media_idade = df['Idade'].mean()
print('media de idade:', media_idade)



netflix_x_idade = df.groupby(df['Idade'])['horas_netflix'].mean()

print(netflix_x_idade)

# relacionar horas de redes com hora de sono

redes_sono = df.groupby(df['horas_sono'])['Horas_midias'].mean()
print(redes_sono)

print(df.describe())

# 5 Visualizações com Matplotlib


plt.figure(figsize=(15,4))

plt.subplot(1,3,1)
redes_sono = df.groupby(df['Horas_midias'].head())['horas_sono'].mean().plot(kind='bar')
plt.xlabel('midia social x horas de sono')
plt.ylabel('Horas de sono')

plt.subplot(1,3,2)

netflix_x_idade = df.groupby(df['Idade'])['horas_netflix'].mean().plot(kind='line')
plt.xlabel('idade por uso da netflix')
plt.ylabel('Horas netflix')

plt.subplot(1,3,3)
horasEstudos_horas_redes = df.groupby(df['trabalha_estuda'])['Horas_midias'].mean().plot(kind='pie', autopct = '%1.1f%%')
plt.xlabel('Horas de estudo')
plt.ylabel('genero')


plt.tight_layout()
plt.show()