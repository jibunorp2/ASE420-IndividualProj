import sqlite3
from datetime import datetime

conn = sqlite3.connect('main.db')
conn.execute('''DROP TABLE todo;''')
conn.execute('''CREATE TABLE IF NOT EXISTS todo(
    id INTEGER PRIMARY KEY,
    task TEXT NOT NULL,
    timed DATETIME NOT NULL,
    tag TEXT NOT NULL);''')

def view():
    query = "SELECT * FROM todo;"
    return conn.execute(query)

def insertdata(task, timed, tag):
    query = "INSERT INTO todo(task, timed, tag) VALUES(?, ?, ?);"
    conn.execute(query, (task, timed, tag))
    conn.commit()

def deletebytag(tagid):
    query = "DELETE FROM todo WHERE id = ?;"
    conn.execute(query, (tagid,))
    conn.commit()

def updatedata(tagid, newtask):
    query = "UPDATE todo SET task = ? WHERE tag = ?;"
    conn.execute(query, (newtask, tagid))
    conn.commit()