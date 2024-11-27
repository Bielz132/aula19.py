import sqlite3

conexao = sqlite3.connect('meu_banco_de_dados.db')

cursor = conexao.cursor()
cursor.execute('''
               Create table if not exists pessoas  (
               id INTENGER PRIMARY KEY
               AUTOINCREMENT NOT NULL,
               nome TEXT NOT NULL,
               idade INTENGER NOT NULL,
               cidade TEXT NOT NULL
               )
               ''')
nome = input('Digite um nome: ')
idade = int(input('Digite sua idade: '))
cidade = input('Cidade: ')
cursor.execute('''
               INSERT INTO pessoas (nome, idade, cidade
               VALUES (?, ?, ?)
               ''', (nome, idade, cidade))
conexao.comit()
cursor.execute('SELECT * FROM pessoas')
pessoas = cursor.fetchall()
for pessoa in pessoas:
    print(f'''ID: {pessoa[0]}, Nome: {pessoa[1]}, Idade: {pessoa[2]}, Cidade: {pessoa[3]}''')
conexao.close()