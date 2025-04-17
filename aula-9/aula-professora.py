import pandas as pd



csv = 'kidney_disease_dataset.csv'
dados = pd.read_csv(csv)
df = pd.DataFrame(dados)


# mediada de tendencia central básica 
idades = df['Age of the patient'].describe()
# head 5 primeiras linhas
# linhas  = df.head()



# valores vazios 



# substuição de valores



# 5 ultimas linhas 
# print(df.tail())



# estrutura tecnicamente 


# print(df.info())



# linhas por rotulos


# print(df.iloc[-2])




# filtrar


filtro = df[ df['Age of the patient'] > 30].describe()
print(filtro)



# add uma nova coluna


df['teste'] = df['Age of the patient']


print(df)










# Download latest version


# dicio = {
#     'livros':['a','b','c'],
#     'xicaras':['azul','vermelha','verde'],
#     'tenis':['nike','mizunu','all star']
# }



# df = pd.Series(dicio)
# DADOS = df['livros'][0]
# print(DADOS)