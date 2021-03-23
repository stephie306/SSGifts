import hashlib

from database import DB


class User:
    def __init__(self, id, username, password, age, email):
        self.id = id
        self.username = username
        self.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        self.age = age
        self.email = email

    def create(self):
        with DB() as db:
            values = (self.username, self.age, self.email, self.password)
            db.execute('''
                INSERT INTO Users(username, age, user_mail, password) VALUES(?, ?, ?, ?)
                ''', values)

            return self

    def delete(self):
        with DB() as db:
            db.execute('''
                DELETE FROM Users WHERE user_id = ?
                ''', self.id)

    @staticmethod
    def find_by_username(username):
        with DB() as db:
            values = db.execute('''
                SELECT * FROM Users WHERE username = ?
            ''', (username,)).fetchone()
            if values:
                return User(*values)
            return None

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def verify_password(self, new_password):
        return self.password == User.hash_password(new_password)