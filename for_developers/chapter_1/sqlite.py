import sqlite3
import io
conexao = sqlite3.connect(":memory:")
cur = conexao.cursor()
contador = 1

def cria_tabela():
    sql = "CREATE TABLE contatos(id INTEGER, nome VARCHAR,fone VARCHAR)"
    cur.execute(sql)
    print("Criada tabela contatos!")

def insere_dados():
    global contador
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    sql = "INSERT INTO contatos VALUES (?,?,?)"
    dados = [contador,nome,telefone]
    cur.execute(sql,dados)
    conexao.commit()
    contador = contador + 1
    print("Inserido dado na tabela contatos!")

def remove_dados():
    id = int(input("Digite o id do contato: "))
    sql = "DELETE FROM contatos WHERE id = ?"
    cur.execute(sql,(id,))
    conexao.commit()
    print("Removido dado na tabela contatos!")

def recuperar_dados():
    sql = "SELECT * FROM contatos"
    cur.execute(sql)
    for linha in cur.fetchall():
        print(linha)

def recuperar_dado_unico():
    id = int(input("Digite o id do contato: "))
    sql = "SELECT * FROM contatos WHERE id = ?"
    cur.execute(sql,(id,))
    print(cur.fetchone())

def atualizar_dados():
    id = int(input("Digite o id do contato: "))
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    sql = "UPDATE contatos SET nome = ?, fone = ? WHERE id = ?"
    dados = [nome,telefone,id]
    cur.execute(sql,dados)
    conexao.commit()
    print("Atualizado dado na tabela contatos!")

def alterando_tabela():
    sql = "ALTER TABLE contatos ADD COLUMN endereco VARCHAR"
    cur.execute(sql)
    conexao.commit()
    print("Alterada tabela contatos!")

def lendo_banco():
    # obtendo informações da tabela
    cur.execute("PRAGMA table_info({})".format("contatos"))
    colunas = [tupla[1] for tupla in cur.fetchall()]
    for coluna in colunas:
        print(coluna)
    print("Lendo tabela contatos!")
    # listando as tabelas do bd
    sql = "SELECT name FROM sqlite_master WHERE type = 'table' ORDER BY name"
    cur.execute(sql)
    print("Tabelas:")
    for tabela in cur.fetchall():
        print(tabela)
    # obtendo o schema da tabela
    sql = "SELECT sql FROM sqlite_master WHERE type = 'table' AND name = 'contatos'"
    cur.execute(sql)
    print("Schema:")
    for schema in cur.fetchall():
        print(schema)


cria_tabela()
#insere_dados()
#insere_dados()
#insere_dados()
#recuperar_dados()
#remove_dados()
#recuperar_dados()
#recuperar_dado_unico()
#atualizar_dados()
#recuperar_dados()
alterando_tabela()
lendo_banco()
conexao.close()