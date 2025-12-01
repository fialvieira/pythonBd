import sqlite3

# 1 - Conectar no BD
def conectar_bd(banco="titulo.db"):
    conn = sqlite3.connect(banco)
    return conn

# 2 - Inserir dados
def inserir_dados(conn, nome, ano, nota):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO filmes (nome, ano, nota) VALUES (?, ?, ?)", (nome, ano, nota))
    conn.commit()
    conn.close()
    
# 3 - Listagem de dados
def listar_dados(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM filmes")
    dados = cursor.fetchall()
    conn.close()
    return dados