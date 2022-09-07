-- a script that lists records with the same score
SELECT score, COUNT(*) AS num
FROM second_table
GROUP BY score
OREDER BY num DESC;
