SELECT teams.yearid AS year, SUM(salary) as salary
FROM salaries
INNER JOIN teams 
ON teams.teamid = salaries.teamid AND teams.yearid = salaries.yearid
WHERE teams.WSWin = 'Y'
GROUP BY teams.yearid
order by salary desc
