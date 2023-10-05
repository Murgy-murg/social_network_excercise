DROP TABLE IF EXISTS user_accounts cascade;
DROP SEQUENCE IF EXISTS user_accounts_id_seq;
CREATE SEQUENCE IF NOT EXISTS user_accounts_id_seq;
CREATE TABLE user_accounts(
    id SERIAL PRIMARY KEY,
    email text,
    username text
);

DROP TABLE IF EXISTS posts cascade;
DROP SEQUENCE IF EXISTS posts_id_seq;
CREATE SEQUENCE IF NOT EXISTS post_id_seq;
CREATE TABLE posts(
    id SERIAL PRIMARY KEY,
    title text,
    content text,
    views int,
    user_account_id int,
    constraint fk_user_account foreign key(user_account_id) references user_accounts(id) on delete cascade
);

INSERT INTO user_accounts (email, username) VALUES ('sammurgatroyd30@gmail.com', 'murgy_murg');
INSERT INTO user_accounts (email, username) VALUES ('oliviamundy@gmail.com', 'mundymooma');

INSERT INTO posts (title, content, views, user_account_id) VALUES ('I am awesome', 'the content of this post is that I am awesome', 1, 1);
INSERT INTO posts (title, content, views, user_account_id) VALUES ('I am not awesome', 'the content of this post is that I am not awesome', 2, 2);
