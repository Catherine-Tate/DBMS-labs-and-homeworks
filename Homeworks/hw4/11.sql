SELECT DISTINCT ON (park) park --, seriesPost.yearid, round, teamidwinner 
FROM teams
INNER JOIN seriesPost ON teams.teamid = seriesPost.teamidwinner
WHERE park NOT LIKE '%Field%' 
AND seriesPost.round LIKE '%DS%'
AND park NOT LIKE '%Park%' 
AND park NOT LIKE '%Stadium%'
and seriesPost.yearid = teams.yearid
