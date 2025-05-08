from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Carregar dataset:
iris = load_iris()
x = iris.data # CARACTERÍSTICAS
y = iris.target # RÓTULOS

# Dividir os dados:
# 70% treino / 30% teste
x_teste, x_treino, y_teste, y_treino = train_test_split(x, y, test_size=0.3, random_state=42)


# Criar modelo
model = DecisionTreeClassifier()
model.fit(x_teste, y_teste)

# Fazer previsão
y_pred = model.predict(x_teste)
print(y_pred)

# Acurácia - qualidade aprendizado
acuracia = accuracy_score(y_teste, y_pred)
print('Acurácia do modelo', acuracia)