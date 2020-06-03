SELECT DISTINCT ON(awardid) a1.awardid
FROM awardsplayers AS a1
INNER JOIN awardsplayers AS a2 ON a1.awardid = a2.awardid
AND a1.yearid+1 = a2.yearid
INNER JOIN awardsplayers AS a3 ON a1.awardid = a3.awardid
AND a2.yearid+1 = a3.yearid
WHERE a1.yearid >= 1950 AND a1.yearid <= 1959
AND a1.playerid=a2.playerid AND a2.playerid = a3.playerid
