SELECT name_full as school_name, count(distinct collegeplaying.playerid)
FROM Schools
INNER JOIN collegeplaying on schools.schoolid = collegeplaying.schoolid
INNER JOIN allstarfull on collegeplaying.playerid = allstarfull.playerid
GROUP BY name_full
ORDER BY count desc, school_name asc
LIMIT 10
