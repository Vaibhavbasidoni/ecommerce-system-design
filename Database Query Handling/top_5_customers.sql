-- This query retrieves the top 5 customers who bought the most books in the last year
-- It joins Customers, Orders, and OrderDetails tables to get the necessary information
-- The WHERE clause filters orders to only those within the last year
-- GROUP BY is used to aggregate book quantities for each customer
-- ORDER BY and LIMIT ensure we get only the top 5 customers by purchase quantity
SELECT 
    c.customer_id, 
    c.name, 
    SUM(od.quantity) as total_books_purchased  -- Count total books bought
FROM 
    Customers c
    JOIN Orders o ON c.customer_id = o.customer_id  -- Connect customers to orders
    JOIN OrderDetails od ON o.order_id = od.order_id  -- Connect orders to details
WHERE 
    o.order_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)  -- Only last year's orders
GROUP BY 
    c.customer_id, c.name  -- Combine results for each customer
ORDER BY 
    total_books_purchased DESC  -- Highest buyers first
LIMIT 5;  -- Show only top 5
