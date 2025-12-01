from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///banco.db", echo=True)
Base = declarative_base()

class Filme(Base):
    __tablename__ = "filmes"
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    nota = Column(Float, nullable=False)

Base.metadata.create_all(engine)

# Inserir dados
def adiciona_filme(nome, ano, nota):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = Filme(nome=nome, ano=ano, nota=nota)
    session.add(filme)
    session.commit()
    session.close()

# adiciona_filme("Inception", 2010, 8.8)
# adiciona_filme("Interstellar", 2014, 8.6)

def atualiza_filme(id, nome=None, ano=None, nota=None):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = session.query(Filme).filter(Filme.id == id).first()
    if filme:
        if nome is not None:
            filme.nome = nome
        if ano is not None:
            filme.ano = ano
        if nota is not None:
            filme.nota = nota
        session.commit()
    session.close()

# atualiza_filme(1, nome="Mario", ano=2024, nota=8.9)

def exclui_filme(id):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = session.query(Filme).filter(Filme.id == id).first()
    if filme:
        session.delete(filme)
        session.commit()
    session.close()

# exclui_filme(1)