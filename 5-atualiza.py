import sqlite3

# 1 - Conectando no BD
conexao = sqlite3.connect("titulo.db")
cursor = conexao.cursor()

# 2 - Atualizando dados
id = 1
novo_nome = 'Super Mario Bros'
cursor.execute(
    """
    UPDATE filmes
    SET nome = ?
    WHERE id = ?
    """, (novo_nome, id)
)
conexao.commit()
conexao.close()

print('Dados atualizados com sucesso!')