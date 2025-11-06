import sqlite3

# 1 - Conectando no BD
conexao = sqlite3.connect("titulo.db")
cursor = conexao.cursor()

# 2 - Lendo dados da tabela
cursor.execute("SELECT * FROM filmes")
filmes = cursor.fetchall()
for filme in filmes:
    print(f"ID: {filme[0]}, Nome: {filme[1]}, Ano: {filme[2]}, Nota: {filme[3]}")

conexao.close()