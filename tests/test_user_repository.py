from lib.user_repository import UserRepository
from lib.user import User


def test_get_all_method(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = UserRepository(db_connection)

    users = repository.all()

    assert users == [
        User(1, 'sammurgatroyd30@gmail.com', 'murgy_murg'),
        User(2, 'oliviamundy@gmail.com', 'mundymooma')
    ]

def test_get_find_method(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = UserRepository(db_connection)

    users = repository.find(2)

    assert users == User(2, 'oliviamundy@gmail.com', 'mundymooma')

def test_create_method(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = UserRepository(db_connection)
    repository.create(User(3, 'test_mail.com', 'test_username'))
    result = repository.all() 
    assert result == [
        User(1, 'sammurgatroyd30@gmail.com', 'murgy_murg'),
        User(2, 'oliviamundy@gmail.com', 'mundymooma'),
        User(3, 'test_mail.com', 'test_username')
    ]
        
def test_delete_method(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repository = UserRepository(db_connection)
    repository.delete(1)
    result = repository.all() 
    assert result == [
        User(2, 'oliviamundy@gmail.com', 'mundymooma'),]
        