--
-- INNER JOIN AND ALIASING
SELECT * 
FROM customers AS c
INNER JOIN orders AS o 
	ON c.customer_id = o.customer_id;

-- LEFT JOIN (left table is preserved) find customers that didnt order anything where it will show null for the order id
SELECT 
	c.customer_id,
	c.full_name,
	o.order_id
FROM customers AS c
LEFT JOIN orders AS o
	ON c.customer_id = o.customer_id;
	
-- AGGREGATIONS = COUNT(), SUM(), AVG(), MIN(), MAX()
--SUM()
SELECT sum(total_amount) 
FROM orders;

--COUNT()
SELECT count(order_id)
FROM orders;

--AVERAGE()
SELECT avg(total_amount)
FROM orders;

--MIN()
SELECT min(total_amount)
FROM orders;

--MAX()
SELECT max(total_amount)
FROM orders;


-- GROUP BY
SELECT 
	c.full_name,
	sum(o.total_amount) AS total_spent
	count(o.order_id) AS total_orders
FROM customers AS c
	INNER JOIN orders AS o
	ON c.customer_id = o.customer_id
GROUP BY c.full_name; 


-- ORDER BY = ASC(default) / DESC Calculate total spend per customer. Show Customer Name, 
--Total Spend (SUM(total_amount)), and Total Orders Count (COUNT(order_id)). 
--Order by Total Spend descending.

SELECT 
	c.full_name,
	sum(o.total_amount) AS total_amount,
	count(o.order_id) AS total_orders
FROM customers AS c 
INNER JOIN orders AS o
ON c.customer_id = o.customer_id
	GROUP BY c.full_name
	ORDER BY total_amount DESC;


--LIMIT = only want the top 3 customers
SELECT
    c.full_name,
    SUM(o.total_amount) AS total_spend
FROM customers AS c
INNER JOIN orders AS o
    ON c.customer_id = o.customer_id
GROUP BY c.full_name
ORDER BY total_spend DESC
LIMIT 3;


--WHERE VS HAVING
--where = before aggregation
--having = after aggregation
SELECT
    c.full_name,
    SUM(o.total_amount) AS total_spend,
    count(o.order_id) AS total_orders
FROM customers AS c
INNER JOIN orders AS o
    ON c.customer_id = o.customer_id
GROUP BY c.full_name
HAVING sum(o.total_amount) > 200
ORDER BY total_spend DESC;

-- GROUP BY = Count the total number of orders and average total amount for each order status
SELECT 
	status,
	count(o.order_id) AS total_orders,
	avg(o.total_amount) AS Average_Status
FROM orders AS o
GROUP BY status;


