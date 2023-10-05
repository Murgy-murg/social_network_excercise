from lib.posts import Posts
from lib.post_repository import PostRepository

def test_all_method(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = PostRepository(db_connection)
    result = repository.all()
    assert result == [
        Posts(1, 'I am awesome', 'the content of this post is that I am awesome', 1, 1),
        Posts(2, 'I am not awesome', 'the content of this post is that I am not awesome', 2, 2)
    ]

def test_find_method(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = PostRepository(db_connection)
    result = repository.find(2)
    assert result == Posts(2, 'I am not awesome', 'the content of this post is that I am not awesome', 2, 2)
    


def test_create_method(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = PostRepository(db_connection)
    repository.create(Posts(3, 'Gandalf is pretty awesome', 'Gandalf did lots of cool things and this is content about it', 0, 1))
    result = repository.all()
    assert result == [
        Posts(1, 'I am awesome', 'the content of this post is that I am awesome', 1, 1),
        Posts(2, 'I am not awesome', 'the content of this post is that I am not awesome', 2, 2),
        Posts(3, 'Gandalf is pretty awesome', 'Gandalf did lots of cool things and this is content about it', 0, 1)
    ]

def test_delete_method(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = PostRepository(db_connection)
    repository.delete(1)
    result = repository.all()
    assert result == [
        Posts(2, 'I am not awesome', 'the content of this post is that I am not awesome', 2, 2)
    ]