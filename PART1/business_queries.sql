-- TASK 1.3 - BUSINESS QUERY IMPLEMENTATION

--QUERY 1 - CUSTOMER PURCHASE HISTORY

SELECT
  CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
  c.email,
  COUNT(DISTINCT o.order_id) AS total_orders,
  SUM(o.total_amount) AS total_spent
FROM customers c
JOIN orders o
  ON c.customer_id = o.customer_id
GROUP BY
  c.customer_id,
  c.first_name,
  c.last_name,
  c.email
HAVING
  COUNT(DISTINCT o.order_id) >= 2
  AND SUM(o.total_amount) > 5000
ORDER BY total_spent DESC;


--QUERY 2 - PRODUCT SALES ANALYSIS

SELECT
  p.category,
  COUNT(DISTINCT p.product_id) AS num_products,
  SUM(oi.quantity) AS total_quantity_sold,
  SUM(oi.subtotal) AS total_revenue
FROM products p
JOIN order_items oi
  ON p.product_id = oi.product_id
GROUP BY p.category
HAVING SUM(oi.subtotal) > 10000
ORDER BY total_revenue DESC;


--QUERY 3 - MONTHLY SALES TREND

SELECT
  MONTHNAME(o.order_date) AS month_name,
  COUNT(DISTINCT o.order_id) AS total_orders,
  SUM(o.total_amount) AS monthly_revenue,
  SUM(SUM(o.total_amount)) OVER (
    ORDER BY MONTH(o.order_date)
  ) AS cumulative_revenue
FROM orders o
WHERE YEAR(o.order_date) = 2024
GROUP BY
  MONTH(o.order_date),
  MONTHNAME(o.order_date)
ORDER BY MONTH(o.order_date);

