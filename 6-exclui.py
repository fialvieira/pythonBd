import sqlite3

# 1 - Conectando no BD
conexao = sqlite3.connect("titulo.db")
cursor = conexao.cursor()

# 2 - Excluindo dados
id = (1, 2)
cursor.execute(
    """
    DELETE FROM filmes
    WHERE id IN (?, ?)
    """, id
)
conexao.commit()
conexao.close()

print('Dados excluídos com sucesso!')