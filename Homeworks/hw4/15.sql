SELECT DISTINCT ON(first, last, city) nameFirst AS first, nameLast AS last, birthcity AS city
FROM master
INNER JOIN batting ON batting.playerid = master.playerid
INNER JOIN teams ON batting.teamid = teams.teamid
WHERE birthState = 'NY' AND franchid = 'NYY'
ORDER BY last
