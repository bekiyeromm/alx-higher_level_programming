#!/usr/bin/env bash
-- displays the 3 max temperature of each state (ordered by State name).
SELECT state, MAX(value) AS temp_max FROM temperatures
GROUP BY state
ORDER BY state
LIMIT 3;