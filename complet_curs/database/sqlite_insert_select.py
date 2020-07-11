import sqlite3

conn = sqlite3.connect("peoples")
cursor = conn.cursor()
sql = "CREATE TABLE people (id INTEGER PRIMARY KEY, name VARCHAR(20))"
cursor.execute(sql)

sql = "INSERT into people VALUES (1, 'André')"
cursor.execute(sql)
sql = "INSERT into people VALUES (2, 'João')"
cursor.execute(sql)
sql = "INSERT into people VALUES (3, 'Lucas')"
cursor.execute(sql)
conn.commit()

sql = "SELECT * FROM people"
cursor.execute(sql)
result = cursor.fetchall()
print(result)