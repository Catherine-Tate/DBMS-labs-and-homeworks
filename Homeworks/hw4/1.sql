--SELECT COUNT(playerid)
--SELECT playerid, saves, yearid
--FROM (
    SELECT DISTINCT ON (playerid) SUM(sv) as saves, playerid, yearid
    FROM pitching
    WHERE yearid >= 1975
    GROUP BY playerid
    ) j 
WHERE j.saves > 40
--order by playerid desc
