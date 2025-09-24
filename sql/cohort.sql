WITH first_orders AS (
  SELECT customer_id, MIN(order_date) AS first_order_date
  FROM orders
  GROUP BY customer_id
),
orders_with_cohort AS (
  SELECT
    o.customer_id,
    o.order_date,
    strftime('%Y-%m', o.order_date) AS order_month,
    strftime('%Y-%m', f.first_order_date) AS cohort_month
  FROM orders o
  JOIN first_orders f ON o.customer_id = f.customer_id
)
SELECT cohort_month, order_month, COUNT(DISTINCT customer_id) as users
FROM orders_with_cohort
GROUP BY cohort_month, order_month
ORDER BY cohort_month, order_month;
