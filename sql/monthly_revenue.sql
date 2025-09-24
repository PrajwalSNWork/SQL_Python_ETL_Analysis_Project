SELECT
  strftime('%Y-%m', order_date) AS month,
  SUM(total_amount) AS revenue,
  COUNT(DISTINCT customer_id) AS active_customers,
  COUNT() AS num_orders
FROM orders
GROUP BY month
ORDER BY month;
