-- a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows
-- Results must be sorted in ascending order by the show title
SELECT s.`title`
  FROM `tv_shows` AS s
  WHERE s.`title` NOT IN
	(SELECT s.`title`
		FROM `tv_shows` AS s
		INNER JOIN `tv_show_genres` AS sg
		ON sg.`show_id`= s.`id`

		INNER JOIN `tv_genres` AS g
		ON g.`id` = sg.`genre_id`
		WHERE g.`name` = "Comedy")
  ORDER BY s.`title`;
