select * from posts;

select * from comments;

select comments.*, posts.title, posts.content, users.name, users.age
from comments
left outer join posts on comments.re_reply_author = posts.post_author
left outer join users on comments.re_reply_author = users.id;