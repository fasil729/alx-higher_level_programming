-- displaying the records with the same score as labeled with score and number(number of records)
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
