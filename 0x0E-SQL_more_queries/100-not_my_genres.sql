-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexte
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
SELECT g.`name`
  FROM `tv_genres` AS g
  WHERE g.name NOT IN
	(SELECT g.`name` 
		FROM `tv_genres` AS g
		INNER JOIN `tv_show_genres` AS sg
		ON sg.`genre_id`= g.`id`

		INNER JOIN `tv_shows` AS s
		ON s.`id` = sg.`show_id`
		WHERE s.`title` = "Dexter")
  ORDER BY g.`name`;
