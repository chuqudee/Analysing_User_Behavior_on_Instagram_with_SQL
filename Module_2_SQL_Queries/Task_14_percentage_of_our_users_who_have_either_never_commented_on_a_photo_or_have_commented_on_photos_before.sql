SELECT tableA.total_A AS 'Number Of Users who never commented',
		(tableA.total_A/(SELECT COUNT(*) FROM users))*100 AS '%',
		tableB.total_B AS 'Number of Users who commented on photos',
		(tableB.total_B/(SELECT COUNT(*) FROM users))*100 AS '%'
FROM
	(
		SELECT COUNT(*) AS total_A FROM
			(SELECT username,comment_text
				FROM users
				LEFT JOIN comments ON users.id = comments.user_id
				GROUP BY users.id
				HAVING comment_text IS NULL) AS total_number_of_users_without_comments
	) AS tableA
	JOIN
	(
		SELECT COUNT(*) AS total_B FROM
			(SELECT username,comment_text
				FROM users
				LEFT JOIN comments ON users.id = comments.user_id
				GROUP BY users.id
				HAVING comment_text IS NOT NULL) AS total_number_users_with_comments
	)AS tableB
