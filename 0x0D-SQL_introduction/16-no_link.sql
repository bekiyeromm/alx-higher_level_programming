##!/usr/bin/env bash
-- lists all records of the table second_table of the database
-- Don’t list rows without a name value
-- Results should display the score and the name
-- Records should be listed by descending score
SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC
