SELECT master.namefirst as first, master.namelast as last, n.appearances
FROM (
    SELECT COUNT(allStarFull.playerid) as appearances,
        halloffame.playerid
    FROM allStarFull
    INNER JOIN hallofFame ON allstarfull.playerid = halloffame.playerid
    AND halloffame.yearid = 2000 
    GROUP BY halloffame.playerid
) n JOIN master ON n.playerid = master.playerid
ORDER BY appearances desc, last asc
LIMIT 8
