SELECT ANY_VALUE(U.name) as 'name', COALESCE(SUM(Rides.distance), 0) as 'travelled_distance'
FROM Rides
         RIGHT JOIN Users U on Rides.user_id = U.id
GROUP BY U.id
ORDER BY 2 DESC, 1 ASC;