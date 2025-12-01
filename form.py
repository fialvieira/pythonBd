import streamlit as st
import dados

st.title("Filmes")

# Conectar ao banco de dados
conn = dados.conectar_bd()

# Formulário html
nome = st.text_input("Digite o nome do filme:")
ano = st.number_input("Digite o ano do filme:", min_value=2010, max_value=2025)
nota = st.slider("Nota do filme:", min_value=0.0, max_value=10.0, step=0.5)

# Botão para incluir filme
if st.button("Adicionar Filme"):
    dados.inserir_dados(conn, nome, ano, nota)
    st.success("Filme adicionado com sucesso!")

# Listar filmes
filmes = dados.listar_dados(conn)
st.header("Lista de Filmes")
st.table(filmes)
