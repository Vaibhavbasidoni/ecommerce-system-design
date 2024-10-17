-- This query finds books that have been ordered more than 10 times
-- It joins the Books and OrderDetails tables to get book information and order quantities
-- GROUP BY is used to aggregate order quantities for each book
-- The HAVING clause filters for books with more than 10 total orders
-- Results are ordered by total quantity to show most popular books first
-- Note: The threshold of 10 can be adjusted based on the dataset size and requirements
SELECT 
    b.book_id, 
    b.title, 
    b.author, 
    SUM(od.quantity) as total_quantity_ordered  -- Count total books ordered
FROM 
    Books b
    JOIN OrderDetails od ON b.book_id = od.book_id  -- Connect books to orders
GROUP BY 
    b.book_id, b.title, b.author  -- Combine results for each book
HAVING 
    SUM(od.quantity) > 10  -- Only books ordered more than 10 times
ORDER BY 
    total_quantity_ordered DESC;  -- Most popular books first
