import sqlite3


connection = sqlite3.connect("Databases/vault_98.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM Users")
for u in cursor.fetchall():
    print(u)
print('----------     ---')
cursor.execute("SELECT * FROM Games")
for u in cursor.fetchall():
    print(u)
print('----------     ---')
cursor.execute("SELECT * FROM Scores")
for u in cursor.fetchall():
    print(u)

connection.close()
