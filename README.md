SQL запросы

Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). 

запрос:

SELECT courier.login, COUNT(orders.id) AS "deliveryCount" 
FROM "Couriers" AS courier 
LEFT JOIN "Orders" AS orders ON courier.id = orders."courierId" 
WHERE orders."inDelivery" = true 
GROUP BY courier.login;

Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно. Для этого: выведи все трекеры заказов и их статусы. Статусы определяются по следующему правилу: Если поле finished == true, то вывести статус 2. Если поле canсelled == true, то вывести статус -1. Если поле inDelivery == true, то вывести статус 1. Для остальных случаев вывести 0.

запрос:

SELECT track, 
CASE 
WHEN finished = true THEN 2 
WHEN cancelled = true THEN -1 
WHEN "inDelivery" = true THEN 1 
ELSE 0 END AS status 
FROM "Orders";