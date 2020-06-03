SELECT sals.yearid as year, avg(teamSal) as Salary
FROM (
    SELECT salaries.yearid, salaries.teamid, SUM(salary) as teamSal
    FROM salaries
    GROUP BY salaries.yearid, salaries.teamid
) sals
GROUP BY sals.yearid
ORDER BY sals.yearid
