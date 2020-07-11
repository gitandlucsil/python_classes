import sqlite3

conn = sqlite3.connect("peoples")
cursor = conn.cursor()

datas = [(4, "Rodrigo"), (5, "Maria")]

sql = "INSERT INTO people VALUES (?, ?)"
for register in datas:
    cursor.execute(sql, register)
conn.commit()

sql = "SELECT * FROM people"
cursor.execute(sql)
result = cursor.fetchall()
print(result)

sql = "DELETE FROM people WHERE id = 3"
cursor.execute(sql)
conn.commit()

sql = "SELECT * FROM people"
cursor.execute(sql)
result = cursor.fetchall()
print(result)
