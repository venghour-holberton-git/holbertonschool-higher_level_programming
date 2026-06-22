-- List records with a score greater than or equal to 10
-- Display score and name
-- Order by score from highest to lowest

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
