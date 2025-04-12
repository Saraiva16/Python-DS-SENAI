# ***Você é um profissional em transição de carreira e está avaliando novas oportunidades de emprego.***

# ***Utilize estatísticas como média, moda, mediana e desvio padrão para analisar as faixas salariais oferecidas por diferentes empresas e tomar uma decisão embasada.***

# ***Explique sua escolha com base nos dados analisados***

# ***Verifique isso através dos salários:***

import statistics

empresa1 = [2500, 2800, 3000, 9500, 12000]

empresa2 = [5000, 5200, 5300, 5400, 5500]

empresa3 = [1000, 2000, 8000, 15000, 20000]

empresa4 = [3500, 4000, 4200, 4300, 6000]

empresa5 = [1200, 1500, 1800, 2500, 10000]

empresas = [empresa1, empresa2, empresa3, empresa4, empresa5]

def media(list):
    lista_media_empresas = []
    for empresa in list:        
        media_empresa = statistics.mean(empresa)        
        lista_media_empresas.append(media_empresa)
    print(lista_media_empresas)

def moda(list):
    lista_empresas = []
    for empresa in list:
        for salario in empresa:
            lista_empresas.append(salario)
    lista_moda_empresas = statistics.mode(lista_empresas)
    print(lista_moda_empresas)

def mediana(list):
    lista_empresas = []
    for empresa in list:
        for salario in empresa:
            lista_empresas.append(salario)
    lista_mediana_empresas = statistics.median(lista_empresas)
    print(lista_mediana_empresas)

def desvio_padrao(list):
    lista_empresas = []
    for empresa in list:
        for salario in empresa:
            lista_empresas.append(salario)
    dp_salario_empresas = statistics.stdev(lista_empresas)
    print(round(dp_salario_empresas, 5))


media(empresas)

moda(empresas)

mediana(empresas)

desvio_padrao(empresas)

def escolha_empresa():
    empresa_Escolhida = input('Digite a empresa que você deseja trabalhar: ')
    justificativa = input('Justifique sua escolha: ')
    print(f'A empresa escolhida foi {empresa_Escolhida} pelo seguinte motivo: {justificativa}.')

escolha_empresa()