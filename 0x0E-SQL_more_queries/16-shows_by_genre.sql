-- a script that lists all shows, and all genres linked to that show, from the database
-- If a show doesn’t have a genre, display NULL in the genre column
-- Results must be sorted in ascending order by the show title and genre name
SELECT t.`title`, g.`name` 
	FROM `tv_shows` AS t 
		LEFT JOIN `tv_show_genres` AS s 
		ON s.`show_id`= t.`id` 
		
		LEFT JOIN `tv_genres` AS g 
		ON g.id = s.`genre_id`
ORDER BY t.title,g.name;
