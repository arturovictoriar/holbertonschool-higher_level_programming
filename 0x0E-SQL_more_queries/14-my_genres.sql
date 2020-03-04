-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
-- Holberton School
SELECT tv_genres.name
FROM tv_shows, tv_show_genres INNER JOIN tv_genres 
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_show_genres.show_id = (SELECT id FROM tv_shows WHERE title = "Dexter") 
GROUP BY tv_genres.name 
ORDER BY tv_genres.name ASC;
