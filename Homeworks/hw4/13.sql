SELECT namefirst as first, nameLast as last
FROM master 
INNER JOIN (
    SELECT b1.playerid
    FROM batting as b1
    INNER JOIN batting as b2 on b1.yearid = b2.yearid 
        AND b1.playerid = b2.playerid
    WHERE b1.ab < b2.ab 
        AND b1.h > b2.h
        AND b1.stint < b2.stint
        AND b2.stint = 2
) peeps on master.playerid = peeps.playerid
ORDER BY master.weight desc

