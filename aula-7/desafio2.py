import statistics

def cria_turma(qtd_alunos):
    print(f'\nBoas vindas, hoje iremos calcular as notas da sua turma que têm {qtd_alunos} alunos')
    lista_turma = []
    x = 0
    while x < qtd_alunos:
        nome_aluno = input('\nDigite o nome do aluno: ')
        n1 = float(input(f'Digite a nota do primeiro semetre do aluno {nome_aluno}: '))
        n2 = float(input(f'Digite a nota do segundo semetre do aluno {nome_aluno}: '))
        n3 = float(input(f'Digite a nota do terceiro semetre do aluno {nome_aluno}: '))        
        soma_notas = sum([n1,n2,n3])
        media_aluno = statistics.mean(soma_notas)
        moda_aluno = statistics.mode(soma_notas)
        desvio_aluno = statistics.stdev(soma_notas)
        mediana_aluno = statistics.median(soma_notas)
        print(f'MÉDIA {nome_aluno}: {media_aluno}\n MODA {nome_aluno}: {moda_aluno}\n DESVIO PADRÃO DAS NOTAS ALUNO {nome_aluno}: {desvio_aluno}\n MEDIANA {nome_aluno}: {mediana_aluno}' )
        x += 1 
    print(lista_turma)

cria_turma(2)
    
    