import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(""" 
        CREATE TABLE IF NOT EXISTS book (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            year INTEGER,
            isbn INTEGER
        )
    """)
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title = "", author = "", year = "", isbn = ""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM book WHERE title = ? OR author = ?  OR 
        year = ? OR isbn = ?
    """, (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id = ?",(id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("""
        UPDATE book SET title = ?,
                        author = ?,
                        year = ?,
                        isbn = ?
        WHERE id = ?
    """, (title, author, year, isbn, id))
    conn.commit()
    conn.close()

connect()
#insert("Book 2", "Jesus", 2030, 14434324)
#print(view())
#print()
#update (1, "libro 1", "alan", 2010, 9999999)
#delete(3)
#print(view())
#print(search(author = "Alan"))
