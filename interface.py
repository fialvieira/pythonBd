import tkinter as tk
import orm
from tkinter import messagebox


# Adicionar filme
def adicionar_filme():
    nome = entry_nome.get()
    ano = entry_ano.get()
    nota = entry_nota.get()

    if not nome or not ano or not nota:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return

    try:
        ano = int(ano)
        nota = float(nota)
    except ValueError:
        messagebox.showerror(
            "Erro", "Ano deve ser um número inteiro e Nota deve ser um número decimal."
        )
        return

    orm.adiciona_filme(nome=nome, ano=ano, nota=nota)
    messagebox.showinfo("Sucesso", "Filme adicionado com sucesso!")


# Atualizar filme
def atualizar_filme():
    id = entry_id.get()
    nome = entry_nome.get()
    ano = entry_ano.get()
    nota = entry_nota.get()

    if not id or not nome or not ano or not nota:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return

    try:
        id = int(id)
        ano = int(ano)
        nota = float(nota)
    except ValueError:
        messagebox.showerror(
            "Erro",
            "ID e Ano devem ser números inteiros e Nota deve ser um número decimal.",
        )
        return

    orm.atualiza_filme(id=id, nome=nome, ano=ano, nota=nota)
    messagebox.showinfo("Sucesso", "Filme atualizado com sucesso!")


# Excluir filme
def excluir_filme():
    id = entry_id.get()

    if not id:
        messagebox.showerror("Erro", "ID deve ser preenchido.")
        return

    try:
        id = int(id)
    except ValueError:
        messagebox.showerror("Erro", "ID deve ser um número inteiro.")
        return

    orm.exclui_filme(id=id)
    messagebox.showinfo("Sucesso", "Filme excluído com sucesso!")


# Interface gráfica
root = tk.Tk()
root.title("Gerenciador de Filmes")

# Rótulos de campos de entrada
label_id = tk.Label(root, text="ID:")
label_id.grid(row=0, column=0)

label_nome = tk.Label(root, text="Nome:")
label_nome.grid(row=1, column=0)

label_ano = tk.Label(root, text="Ano:")
label_ano.grid(row=2, column=0)

label_nota = tk.Label(root, text="Nota:")
label_nota.grid(row=3, column=0)

# Campos de entrada
entry_id = tk.Entry(root, width=50)
entry_id.grid(row=0, column=1, padx=10, pady=5)

entry_nome = tk.Entry(root, width=50)
entry_nome.grid(row=1, column=1, padx=10, pady=5)

entry_ano = tk.Entry(root, width=50)
entry_ano.grid(row=2, column=1, padx=10, pady=5)

entry_nota = tk.Entry(root, width=50)
entry_nota.grid(row=3, column=1, padx=10, pady=5)

# Botões
button_adicionar = tk.Button(root, text="Adicionar Filme", command=adicionar_filme)
button_adicionar.grid(row=4, column=0, columnspan=2, pady=5)

button_atualizar = tk.Button(root, text="Atualizar Filme", command=atualizar_filme)
button_atualizar.grid(row=5, column=0, columnspan=2, pady=5)

button_excluir = tk.Button(root, text="Excluir Filme", command=excluir_filme)
button_excluir.grid(row=6, column=0, columnspan=2, pady=5)

root.mainloop()
