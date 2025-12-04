import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

with open("queries.sql", "r", encoding="utf-8") as f:
    sql_commands = f.read()

cursor.executescript(sql_commands)

conn.commit()
conn.close()

print("school.db успешно создан")
