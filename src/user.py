import hashlib

from database import DB


class User:
    def __init__(self, id, first_name, last_name, password, age, email):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        self.age = age
        self.email = email

    def create(self):
        with DB() as db:
            values = (self.first_name, self.last_name, self.age, self.email, self.password)
            db.execute('''
                INSERT INTO Users(user_first_name, user_last_name, age, user_mail, password) VALUES(?, ?, ?, ?, ?)
                ''', values)

            return self

    def delete(self):
        with DB() as db:
            db.execute('''
                DELETE FROM Users WHERE user_id = ?
                ''', self.id)

    @staticmethod
    def find_by_firstname(first_name):
        with DB() as db:
            values = db.execute('''
                SELECT * FROM Users WHERE username = ?
            ''', (first_name,)).fetchone()
            if values:
                return User(*values)
            return None

    @staticmethod
    def find_by_lastname(last_name):
        with DB() as db:
            values = db.execute('''
                SELECT * FROM Users WHERE username = ?
            ''', (last_name,)).fetchone()
            if values:
                return User(*values)
            return None

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def verify_password(self, new_password):
        return self.password == User.hash_password(new_password)