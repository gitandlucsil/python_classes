from ZODB import FileStorage, DB
import transaction

# Definindo o armazenamento do banco
storage = FileStorage.FileStorage("people.fs")
db = DB(storage)
#Conectando
conn = db.open()
#Referência para a raiz da árvore
root = conn.root()
#Um registro persistente
root["singer"] = "Kate Bush"
# Efetuando a alteração
transaction.commit()
print(root["singer"])
# Mudando um item
root["singer"] = "Tori Amos"
print(root["singer"]) 
# Abortando...
transaction.abort()
# O item voltou ao que era antes da transação
print(root["singer"])