import sqlite3


connection = sqlite3.connect("vault_98/Databases/vault_98.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM Users")
for u in cursor.fetchall():
    print(u)

cursor.execute("SELECT * FROM Journal")
for u in cursor.fetchall():
    print(u)

connection.close()
