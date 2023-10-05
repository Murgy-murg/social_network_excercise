from lib.user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM user_accounts')
        users = []
        for row in rows:
            item = User(row['id'], row['email'], row['username'])
            users.append(item)
        return users

    def find(self, user_id):
        rows = self._connection.execute('SELECT * FROM user_accounts WHERE id = %s', [user_id])
        row = rows[0]
        return User(row['id'], row['email'], row['username'])
    
    def create(self, user):
        self._connection.execute('INSERT INTO user_accounts (email, username) VALUES (%s, %s)',
                                [user.email, user.username])
        return None
    
    def delete(self, id):
        self._connection.execute('DELETE FROM user_accounts WHERE id = %s',
                                [id])
        return None
        