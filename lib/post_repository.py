from lib.posts import Posts

class PostRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM posts')
        posts = []
        for row in rows:
            item = Posts(row['id'], row['title'], row['content'], row['views'], row['user_account_id'])
            posts.append(item)
        return posts
    def find(self, id):
        rows = self._connection.execute('SELECT * FROM posts WHERE id = %s',[id])
        row = rows[0]
        return Posts(row['id'], row['title'], row['content'], row['views'], row['user_account_id'])
    def create(self, new_post):
        self._connection.execute('INSERT INTO posts(title, content, views, user_account_id) VALUES (%s, %s, %s, %s)', [new_post.title, new_post.content, new_post.views, new_post.user_account_id])
        return None
    def delete(self, user_id):
        self._connection.execute('DELETE FROM posts WHERE id = %s', [user_id])
        return None