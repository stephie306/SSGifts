import sqlite3

DB_NAME = 'database.db'

conn = sqlite3.connect(DB_NAME)

conn.cursor().execute(
    '''
    CREATE TABLE IF NOT EXISTS Event (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        event_end_date TEXT NOT NULL,
        name TEXT NOT NULL,
        price_window REAL NOT NULL
    )
    '''
)

conn.cursor().execute(
    '''
    CREATE TABLE IF NOT EXISTS User (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        username TEXT NOT NULL,
        age INTEGER CHECK(age >= 18),
        user_mail TEXT NOT NULL,
        event_id INTEGER,
        FOREIGN KEY(event_id) REFERENCES Event(id)
    )
    '''
)