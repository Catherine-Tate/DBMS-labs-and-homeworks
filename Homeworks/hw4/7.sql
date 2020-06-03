SELECT master.playerID, hits/atBats as "career_avg" 
FROM (
    SELECT SUM(h) as hits, SUM(ab) as atBats, playerid
    FROM batting
    GROUP BY playerid
) j
INNER JOIN master ON master.playerid = j.playerid
WHERE birthyear >= 1958 AND birthyear <= 1960 AND j.atBats > 300
ORDER BY "career_avg" desc
