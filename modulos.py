import statistics


def media(list):
    media_empresa = statistics.mean(list)  
    print(f'MÉDIA: ',round(media_empresa, 2))

def moda(list):
    lista_moda_empresas = statistics.mode(list)
    print(f'MODA: ',lista_moda_empresas)

def mediana(list):
    lista_mediana_empresas = statistics.median(list)
    print(f'MEDIANA: ',lista_mediana_empresas)

def desvio_padrao(list):
    dp_salario_empresas = statistics.stdev(list)
    print(f'DESVIO PADRÃO: ',round(dp_salario_empresas, 5))

def variancia(list):
    print(f'VARIÂNCIA: ',statistics.variance(list))
    

def amplitude(list):
    ampl = max(list)-min(list)
    print(f'AMPLITUDE: ',ampl)