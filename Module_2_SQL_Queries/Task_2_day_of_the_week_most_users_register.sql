SELECT DAYNAME(created_at) AS day_of_week, COUNT(*) AS num 
FROM users 
GROUP BY day_of_week 
ORDER BY num DESC LIMIT 1;
