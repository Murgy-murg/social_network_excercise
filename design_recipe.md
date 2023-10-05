# User stories
As a social network user,
So I can have my information registered,
I'd like to have a user account with my email address.

As a social network user,
So I can have my information registered,
I'd like to have a user account with my username.

As a social network user,
So I can write on my timeline,
I'd like to create posts associated with my user account.

As a social network user,
So I can write on my timeline,
I'd like each of my posts to have a title and a content.

As a social network user,
So I can know who reads my posts,
I'd like each of my posts to have a number of views.

Nouns: 
user account, email address, username, posts, title, content, number of views

# Record ------- Properties
User account     email address, username
Posts            title, content, number of views


# Column types
Table: User accounts
id: SERIAL
email address: text
username: text

Table: Posts
id: SERIAL
title: text
content: text
number of views: int

Does user account contain many posts ? YES !
Does posts contain many user accounts ? NO !

Therefore foreign ID is within posts table