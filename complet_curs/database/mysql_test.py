import mysql.connector

conn = mysql.connector.connect(user='admin', password='admin',host='localhost',database="peoples")
cursor = conn.cursor()
sql = "CREATE TABLE people (people_id int(11) NOT NULL AUTO_INCREMENT, name VARCHAR(20), email VARCHAR(20), PRIMARY KEY (people_id))"
cursor.execute(sql)
cursor.close()
conn.close()