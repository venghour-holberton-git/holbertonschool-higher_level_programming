-- Lists all genres and the number of shows linked to each genre
-- Only genres with at least one linked show are included
-- Results are sorted in descending order by number of shows

SELECT
    tv_genres.name AS genre,
    COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres
    ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id, tv_genres.name
ORDER BY number_of_shows DESC;
