SELECT name
FROM (
    SELECT count(teamidLoser) as losses, teamidLoser as teamid
    FROM seriespost
    WHERE round LIKE 'NLCS'
    OR round LIKE 'ALCS'
    GROUP BY teamidLoser
) j
INNER JOIN teams ON teams.teamid = j.teamID
AND losses > 2
GROUP BY teams.name
