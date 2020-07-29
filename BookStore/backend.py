import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER, UNIQUE(isbn))")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def viewAll():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title = "", author = "", year = "", isbn = ""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?" , (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ? ", (title, author, year, isbn, id))
    conn.commit()
    conn.close()

connect()
print(viewAll())
print()
# # insert("My Title", "My Author", 2020, 123456789)
# print(viewAll())
# print()
# print(search(year = 2020))
# insert(title="The Sea", author = "John Smith", year = 1981, isbn = 987654321)
# print(viewAll())
# print()
# delete(id=5)
# print()
# print(viewAll())
# update(
#     id = 3,
#     title = "Hunger Games",
#     author = "Johana",
#     year = 1990,
#     isbn=31857823
# )
# print()
# print(viewAll())