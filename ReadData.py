import sqlite3
import psycopg2

def create_table():
    conn = sqlite3.connect("myStudents.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER, name TEXT,  email  TEXT)")
    conn.commit()
    conn.close()


def insert(id, name, email):
    conn = sqlite3.connect("myStudents.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO students VALUES(?,?,?)", (id, name, email))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("myStudents.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("myStudents.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, name, email):
    conn = sqlite3.connect("myStudents.db")
    cur = conn.cursor()
    cur.execute("UPDATE students SET name=?, email=? WHERE id=id", (name, email))
    conn.commit()
    conn.close()

update(1200, "Joe Flin", "jflin@yahoo.com")
print(view())
