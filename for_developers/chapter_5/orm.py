from sqlalchemy import *

db = create_engine("sqlite:///progs.db")
#Torna acessível os metadados
metadata = MetaData(db)
#Ecoa o que o SQLAlchemy está fazend
metadata.bind.echo = True
#Tabela Prog
prog_table = Table(
    "progs",metadata,
    Column("prog_id",Integer,primary_key = True),
    Column("name",String(80))
)
#Cria a tabela
prog_table.create()

#Carrega a definição da tabela
prog_table = Table("progs",metadata,autoload = True)
#Insere dados
insert = prog_table.insert()
insert.execute(
    {"name":"Yes"},
    {"name":"Genesis"},
    {"name":"Pink Floyd"},
    {"name":"King Crimson"},

#Seleciona
select = prog_table.select()
result = select.execute()
for row in result.fetchall():
    print(row)