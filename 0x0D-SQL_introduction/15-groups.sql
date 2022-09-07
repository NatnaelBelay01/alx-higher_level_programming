-- a script that lists records with the same score
SELECT score, COUNT(*) AS num
FROM second_table
GROUP BY score
ORDER BY num DESC;
