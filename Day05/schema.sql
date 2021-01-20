create table users (
  id int not null primary key auto_increment,
  name varchar(20) not null,
  age tinyint default 0
);

insert into users (name, age) value
('john', 20),
('abc', 30),
('steve', 15);

create table posts (
  id int not null primary key auto_increment,
  title varchar(50) not null,
  post_author int(20) not null,
  content text,
  constraint post_author_key foreign key (post_author) references users (id)
);

insert into posts (title, post_author, content) value
('hello', 2, 'nice to meet you');

create table comments (
  id int not null primary key auto_increment,
  reply_author int(20),
  reply text,
  re_reply_author int(20),
  re_reply text,
  constraint reply_author_key foreign key (reply_author) references users (id),
  constraint re_reply_author_key foreign key (re_reply_author) references users (id)
);

insert into comments (reply_author, reply, re_reply_author, re_reply) value
(1, 'Hi!!', 2, 'Thx!');