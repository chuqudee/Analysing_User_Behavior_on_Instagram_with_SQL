SELECT tag_name, COUNT(tag_name) AS total
FROM tags
JOIN photo_tags ON tags.id = photo_tags.tag_id
GROUP BY tags.id
ORDER BY total DESC
LIMIT 5;
