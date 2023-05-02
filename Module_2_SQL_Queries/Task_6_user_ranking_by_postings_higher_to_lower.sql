SELECT users.username,COUNT(photos.image_url)
FROM users
JOIN photos ON users.id = photos.user_id
GROUP BY users.id
ORDER BY 2 DESC;

