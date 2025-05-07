# Estudo de Caso: Hospital X Análise de Dados de Agendamentos e Pacientes

Um hospital deseja melhorar a gestão de seus pacientes e agendamentos.
Para isso, eles precisam de uma ferramenta para visualizar dados de agendamentos, pacientes, tempos de espera e para prever a demanda de consultas futuras.
A tarefa do aluno é criar um dashboard com o uso de Python, Tkinter, Pandas, Numpy, Matplotlib e Scikit-learn para análise de dados.

CRIE UM CSV: COM AS SEGUINTES COLUNAS:
Paciente,Especialidade,Data,Tempo_espera,Médico

Situação Problema: O hospital tem um banco de dados com informações sobre pacientes, especialidades médicas, tempos de espera e médicos responsáveis. O desafio é construir um ***dashboard*** interativo que permita aos gestores do hospital realizar as seguintes atividades:

Visualizar gráficos para análise de agendamentos e tempos de espera.
Exibir gráficos de dispersão, linha e barras para explorar as variáveis.
Calcular e exibir as medidas de tendência central: média, moda e mediana.
Usar o Scikit-learn para prever o tempo de espera com base no histórico de agendamentos.

Gráfico de Dispersão: Para analisar a relação entre a quantidade de consultas e os tempos de espera.

Gráfico de Linha: Para mostrar a evolução dos agendamentos ao longo do tempo.
Gráfico de Barras: Para exibir a distribuição de agendamentos por especialidade.
Análise de Tendência Central: Calcular e exibir a média, moda e mediana dos tempos de espera.
Predição com Scikit-learn: Usar um modelo simples de regressão para prever o tempo de espera baseado no número de pacientes agendados.

## **Funcionalidades do Sistema:**

Básicas:
CRIE UM CSV: COM AS SEGUINTES COLUNAS:
Paciente,Especialidade,Data,Tempo_espera,Médico

1 Botão para Exibir Gráficos:

- Exibe o gráfico geral de dados.

2 Botão para Exibir Gráfico com Matplotlib:

- Exibe gráficos usando a biblioteca Matplotlib:
    - Gráfico de Dispersão
    - Gráfico de Linhas
    - Gráfico de Barras

3 Botão para Análise de Tendência Central:

- Exibe os principais indicadores estatísticos:
    - Média
    - Moda
    - Mediana

4 Botão para Predição Básica com Scikit-Learn:

- Exibe a predição básica usando a biblioteca Scikit-Learn.
