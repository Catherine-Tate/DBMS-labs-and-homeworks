SELECT j.yearid as years
FROM (
    SELECT managers.yearid, managers.teamid, n.mostWins
    FROM (
        SELECT yearid, MAX(w) as mostWins
        FROM managers
        WHERE yearid >= 1975
        GROUP BY yearid
        ) n 
    INNER JOIN managers ON managers.yearid = n.yearid AND n.mostWins = managers.w 
    ) j
INNER JOIN teams ON teams.yearid = j.yearid AND teams.teamid = j.teamid AND  teams.divwin = 'Y'
ORDER BY j.yearid desc
