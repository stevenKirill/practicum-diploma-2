SELECT courier.login, COUNT(orders.id) AS "deliveryCount"
FROM "Couriers" AS courier
LEFT JOIN "Orders" AS orders ON courier.id = orders."courierId"
WHERE orders."inDelivery" = true
GROUP BY courier.login;

SELECT track,
CASE
WHEN finished = true THEN 2
WHEN cancelled = true THEN -1
WHEN "inDelivery" = true THEN 1
ELSE 0 END AS status
FROM "Orders";