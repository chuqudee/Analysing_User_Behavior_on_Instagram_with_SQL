/*We're running a new contest to see who can get the most likes on a single photo.
WHO WON??!!*/

SELECT users.username,photos.id,photos.image_url,COUNT(*) AS Total_Likes
FROM likes
JOIN photos ON photos.id = likes.photo_id
JOIN users ON users.id = likes.user_id
GROUP BY photos.id
ORDER BY Total_Likes DESC
LIMIT 1;
