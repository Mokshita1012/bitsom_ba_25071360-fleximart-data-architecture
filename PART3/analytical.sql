--QUERY 1

USE fleximart_dw;

SELECT
    d.year,
    d.quarter,
    d.month_name,
    SUM(f.total_amount) AS total_sales,
    SUM(f.quantity_sold) AS total_quantity
FROM fact_sales f
JOIN dim_date d
	 ON f.date_key = d.date_key
WHERE d.year = 2024
GROUP BY 
     d.year,
     d.quarter,
     d.month,
     d.month_name
ORDER BY 
     d.year,
     d.quarter,
     d.month;


--QUERY 2

SELECT
    p.product_name,
    p.category,
    SUM(f.quantity_sold) AS units_sold,
    SUM(f.total_amount) AS revenue,
    ROUND(
        SUM(f.total_amount) * 100 /
        (SELECT SUM(total_amount) FROM fact_sales),
        2
	) AS revenue_percentage
FROM fact_sales f
JOIN dim_product p
    ON f.product_key = p.product_key
GROUP BY 
     p.product_name,
     p.category
ORDER BY
     revenue DESC
LIMIT 10;



--QUERY 3

USE fleximart_dw;

SELECT
    CASE
        WHEN cs.total_spent > 50000 THEN 'High Value'
        WHEN cs.total_spent BETWEEN 20000 AND 50000 THEN 'Medium Value'
        ELSE 'Low Value'
END AS customer_segment,
COUNT(*) AS customer_count,
SUM(cs.total_spent) AS total_revenue,
ROUND(SUM(cs.total_spent) / COUNT(*), 2) AS avg_revenue_per_customer
FROM (
     SELECT 
          c.customer_key,
          SUM(f.total_amount) AS total_spent
	 FROM fact_sales f
     JOIN dim_customer c
		ON f.customer_key = c.customer_key
	GROUP BY c.customer_key
) AS cs
GROUP BY customer_segment;
