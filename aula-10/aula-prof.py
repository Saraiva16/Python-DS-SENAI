import statistics
import matplotlib.pyplot as plt 



def moda1(lista):
    moda = statistics.mode(lista)
    print('Moda: ', moda)



def mediana1(lista):
    mediana = statistics.median(lista)
    print('Mediana: ', mediana)



def varianca1(lista):
    varianca = statistics.variance(lista)
    print('Variança: ', varianca)


def desvio1(lista):
    desvio = statistics.stdev(lista)
    print(f'Desvio padrão:  {desvio:.2f}')



def media1(lista):
    media = statistics.mean(lista)
    print('Media: ', media)
 
cargos  =  ['Cargo 1', 'cargo 2', 'cargo 3', 'cargo 4', 'cargo 5'] 
empresa1 = [1000,6000,1200,8000,1400]
empresa1.sort()
empresa2 = [5000,4000,3000,2000,7000]
empresa2.sort()
empresa3 = [1200,1300,8000,3000,15000]
empresa3.sort()
empresa4 = [1400,1750,2000,4500,5900]
empresa4.sort()


def handle(lista, salarios):


    print('EMPRESA', salarios)
    print('----------------------------')
    
    media1(lista)
    mediana1(lista)
    moda1(lista)
    varianca1(lista)
    desvio1(lista)



handle(empresa1, empresa1)  
handle(empresa2, empresa2)   
handle(empresa3, empresa3) 
handle(empresa4, empresa4)



def grafico_plot():
    plt.figure(figsize=(6,4))
    plt.plot(cargos,empresa1)
    
    plt.figure(figsize=(6,4))
    plt.pie(empresa1, labels=cargos)


    plt.figure(figsize=(6,4))
    plt.bar(cargos,empresa1)
    
    plt.figure(figsize=(6,4))
    plt.scatter(empresa1, cargos)



    plt.show()


grafico_plot()



# def grafico_bar():




# grafico_bar()



# def grafico_pie():


  


# grafico_pie()



# def grafico_scatter():


    


# grafico_scatter()


