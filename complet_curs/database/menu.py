import mysql.connector
import sys

def conectDatabase():
    DATABASE = "peoples"
    USER = "admin"
    PWD = "admin"
    HOST = "localhost"
    try:
        conn = mysql.connector.connect(user=USER,password=PWD,host=HOST,db=DATABASE)
        print("Succesfully conected to database!")
    except mysql.connector.Error as err:
        print("Failed to connect in the database!")
        print(err)
        menu()
    return conn

def register(connection):
    print("Write the people's data: \n")
    nome = input("Name:" )
    email = input("Email:" )
    cursor = connection.cursor()
    sql = "INSERT INTO people(name, email) VALUES('"+nome+"','"+email+"')"
    #print(sql)
    try:
        cursor.execute(sql)
        connection.commit()
        print("People succesfully registered!")
    except mysql.connector.Error as err:
        print("Failed to insert data!")
        print(err)
    menu()

def change(connection):
    id = input("Write the people's id to update: \n")
    name = input("Write the new name: \n")
    cursor = connection.cursor()
    sql = "UPDATE people SET name='"+name+"' WHERE people_id="+id
    try:
        cursor.execute(sql)
        connection.commit()
        print("People succesfully updated!!")
    except mysql.connector.Error as err:
        print("Failed to update data!")
        print(err)
    menu()

def erase(connection):
    print("Write the people's id to delete: \n")
    id = input("Id:" )
    cursor = connection.cursor()
    sql = "DELETE FROM people WHERE people_id="+id
    #print(sql)
    try:
        cursor.execute(sql)
        connection.commit()
        print("People succesfully deleted!!")
    except mysql.connector.Error as err:
        print("Failed to delete data!")
        print(err)
    menu()

def list_all(connection):
    cursor = connection.cursor()
    sql = "SELECT * FROM people"
    try:
        cursor.execute(sql)
        datas = cursor.fetchall()
        print("All people registered: \n")
        print("--ID--|--NAME--|--EMAIL--|")
        for data in datas:
            id = data[0]
            name = data[1]
            email = data[2]
            print("  %s      %s   %s" % (id, name, email))
    except mysql.connector.Error as err:
        print("Failed to select data!")
        print(err)
    menu()

def search(connection):
    name = input("Write the people's name to search for: \n")
    cursor = connection.cursor()
    sql = "SELECT * FROM people WHERE name like '%"+name+"%'"
    try:
        cursor.execute(sql)
        datas = cursor.fetchall()
        print("All people registered: \n")
        print("--ID--|--NAME--|--EMAIL--|")
        for data in datas:
            id = data[0]
            name = data[1]
            email = data[2]
            print("  %s      %s   %s" % (id, name, email))
    except mysql.connector.Error as err:
        print("Failed to select data!")
        print(err)
    menu()

def menu():
    chooseOption = int(input("Choose an option:\n1 - To register\n2 - To update\n3 - To Delete\n4 - Search\n5 - List all\n6 - Exit\n"))
    conn = None
    try:
        conn = conectDatabase()
    except:
        if chooseOption < 1 or chooseOption > 6:
            print("Invalid option!")
            menu()
    if chooseOption == 1:
        register(conn)
    if chooseOption == 2:
        change(conn)
    if chooseOption == 3:
        erase(conn)
    if chooseOption == 4:
        search(conn)
    if chooseOption == 5:
        list_all(conn)
    if chooseOption == 6:
        conn.close()
        sys.exit()


menu()