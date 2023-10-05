from lib.user import User

def test_contstructs():
    user = User(1, 'test email', 'test username')
    assert user.id == 1
    assert user.email == 'test email'
    assert user.username == 'test username'

def test_users_are_equal():
    user1 = User(1, 'test email', 'test username')
    user2 = User(1, 'test email', 'test username')
    assert user1 == user2

def test_formats_nicely():
    user = User(1, 'test email', 'test username')
    assert str(user) == "User(1, test email, test username)"
