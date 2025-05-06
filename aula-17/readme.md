# DATA BASE

Documentação sqlite3: https://docs.python.org/pt-br/3.9/library/sqlite3.html

Bancos de dados:
1. Relacional;
2. Não-relacional

## Relacional
SQL
Lembra uma tabela Excel:
Linhas e colunas; cada valor tem uma célula


## Não-Relacional
NoSQL
Se parece com um arquivo JSON, onde temos chave e valor. Também parecido com um dicionário em Python

# SQLITE3
- Importar sqlite3
- > *import sqlite3*
- Criar conexão
- > *conexao = sqlite3.connect('meu_bd.db')*
- Criar um cursor
- > *cursor = conexao.cursor()*
- Inserir dados
- Fechar conexão 
