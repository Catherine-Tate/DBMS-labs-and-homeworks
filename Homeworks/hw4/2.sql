SELECT COUNT(master.playerid)
FROM master
INNER JOIN batting ON master.playerid = batting.playerid
WHERE height < 72
AND 
yearid = 1995
AND 
h/ab::float > .300
AND 
ab >  50
