from lib.posts import Posts
def test_constructs():
    posts = Posts(1, 'test title', 'test content', 0, 3)
    assert posts.id == 1
    assert posts.title == 'test title'
    assert posts.content == 'test content'
    assert posts.views == 0
    assert posts.user_account_id == 3

def test_equality():
    posts1 = Posts(1, 'test title', 'test content', 0, 3)
    posts2 = Posts(1, 'test title', 'test content', 0, 3)
    assert posts1 == posts2

def test_format_nicely():
    post = Posts(1, 'test title', 'test content', 0, 3)
    assert str(post) == 'Posts(1, test title, test content, 0, 3)'