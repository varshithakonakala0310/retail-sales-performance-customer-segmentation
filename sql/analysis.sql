-- Retail Sales & Segmentation — SQL
-- Tables: retail_orders_synthetic, customer_rfm_segments

-- Monthly revenue trend
SELECT strftime('%Y-%m', order_date) AS month, ROUND(SUM(revenue),2) AS revenue, COUNT(*) AS orders
FROM retail_orders_synthetic GROUP BY 1 ORDER BY 1;

-- Top 20 customers by spend
SELECT customer_id, COUNT(*) AS orders, ROUND(SUM(revenue),2) AS total_spend
FROM retail_orders_synthetic GROUP BY customer_id ORDER BY total_spend DESC LIMIT 20;

-- Segment summary
SELECT segment, COUNT(*) AS customers, ROUND(AVG(monetary),2) AS avg_monetary, ROUND(AVG(frequency),2) AS avg_frequency
FROM customer_rfm_segments GROUP BY segment ORDER BY avg_monetary DESC;

-- Average order value by month
SELECT strftime('%Y-%m', order_date) AS month, ROUND(AVG(revenue),2) AS avg_order_value
FROM retail_orders_synthetic GROUP BY 1 ORDER BY 1;
