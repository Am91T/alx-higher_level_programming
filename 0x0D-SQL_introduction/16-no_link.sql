-- script that eliminate all records
-- without value
SELECT score, name
FROM second_table
WHERE char_length(name) > 0
ORDER BY score DESC;
