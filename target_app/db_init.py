import sqlite3, os
DB = os.path.join(os.path.dirname(__file__), 'data.db')
if os.path.exists(DB):
    print("DB already exists:", DB)
else:
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT);")
    users = [('alice',),('bob',),('admin',)]
    cur.executemany("INSERT INTO users(username) VALUES (?)", users)
    conn.commit()
    conn.close()
    print("DB created with sample users")
