-- Total revenue by product

SELECT product_name, SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product_name
ORDER BY total_revenue DESC;

--Daily total sales

SELECT sale_date, SUM(quantity * price) as daily_sales
FROM sales
GROUP BY sale_date
ORDER BY sale_date;

-- Example CTE with filter

WITH revenue AS (
	SELECT product_name, SUM(quantity * price) as total_revenue
	FROM sales
	GROUP BY product_name
)
SELECT *
FROM revenue
WHERE total_revenue > 200;
