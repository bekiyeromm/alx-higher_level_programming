#!/usr/bin/env bash
-- script that displays the average temperature (Fahrenheit) by city ordered by
-- temperature desending order
SELECT city, AVG(value) AS temp FROM temperatures
GROUP BY city
ORDER BY temp DESC;
