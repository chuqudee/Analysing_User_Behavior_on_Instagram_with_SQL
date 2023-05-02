SELECT username,comment_text
FROM users
LEFT JOIN comments ON users.id = comments.user_id
GROUP BY users.id
HAVING comment_text IS NULL;

