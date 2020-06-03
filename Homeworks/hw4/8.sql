SELECT DISTINCT ON (salaries.yearid) salaries.yearid as year, allStars.asp/regulars.rp as Ratio
FROM (
    SELECT salaries.yearid, 
        AVG(salary) as "asp"
    FROM salaries
    INNER JOIN allStarFull ON salaries.playerid = allstarfull.playerid
    AND allstarfull.yearid = salaries.yearid
    GROUP BY salaries.yearid
) allStars INNER JOIN salaries ON salaries.yearid = allstars.yearid 
INNER JOIN (
    select salaries.yearid,
        AVG(salary) as "rp"
    FROM salaries
    LEFT OUTER JOIN allstarfull on salaries.playerid = allstarfull.playerid
    AND allstarfull.yearid = salaries.yearid
    GROUP BY salaries.yearid
) regulars ON regulars.yearid = allstars.yearid
