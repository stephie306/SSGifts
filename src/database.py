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
        user_first_name TEXT NOT NULL,
        user_last_name TEXT NOT NULL,
        age INTEGER CHECK(age >= 18),
        user_mail TEXT NOT NULL,
        password TEXT NOT NULL,
        event_id INTEGER,
        FOREIGN KEY(event_id) REFERENCES Event(id)
    )
    '''
)

class DB:
    def __enter__(self):
        self.connection = sqlite3.connect(DB_NAME)
        return self.connection.cursor()

    def __exit__(self, type, value, traceback):
        self.connection.commit()