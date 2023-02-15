-- lists all cities of californya in the database hbtn_0d_usa.
-- results are ordered by ascending cities.id.
SELECT id, name
  FROM cities
 WHERE state_id IN
       (SELECT id
	  FROM states
	 WHERE name = "California")
 ORDER BY id;
