SELECT COUNT(DISTINCT(users.id)) AS total_number_of_users_with_posts
FROM users
JOIN photos ON users.id = photos.user_id;

