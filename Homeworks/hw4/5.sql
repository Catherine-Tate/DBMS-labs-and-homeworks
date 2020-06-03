SELECT 
    franchName as franchise, 
    AVG(CAST(attendance as INT)) as attendance
FROM teams
INNER JOIN teamsfranchises ON teamsFranchises.franchid = teams.franchid
WHERE yearid >= 1997
GROUP BY franchName
ORDER BY franchName
