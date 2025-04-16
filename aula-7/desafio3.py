import modulos

pessoas = {
    "Ana": 28,
    "Bruno": 34,
    "Carlos": 25,
    "Daniela": 30,
    "Eduardo": 40,
    "Fernanda": 27,
    "Gustavo": 22,
    "Helena": 29,
    "Igor": 33,
    "Juliana": 31,
    "Karla": 26,
    "Lucas": 35,
    "Mariana": 24,
    "Nicolas": 38,
    "Olívia": 32,
    "Paulo": 36,
    "Quezia": 21,
    "Rafael": 39,
    "Sofia": 23,
    "Tiago": 37,
    "Ursula": 28,
    "Vinícius": 30,
    "Wesley": 34,
    "Xênia": 27,
    "Yara": 26,
    "Zeca": 29,
    "Beatriz": 33,
    "Caio": 25,
    "Débora": 31,
    "Enzo": 22
}

lista_valores = []

for pessoa, valor in pessoas.items():
    lista_valores.append(valor)
print(lista_valores)

media = modulos.media(lista_valores)
mediana = modulos.mediana(lista_valores)
moda = modulos.moda(lista_valores)
variancia = modulos.variancia(lista_valores)
desvio_padrao = modulos.desvio_padrao(lista_valores)
amplitude = modulos.amplitude(lista_valores)
