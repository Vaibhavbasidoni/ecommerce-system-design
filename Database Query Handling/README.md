
# Bookstore Database Queries

This project contains SQL queries for analyzing data from an online bookstore database.

## Queries

1. `top_5_customers.sql`:
   Retrieves the top 5 customers who have purchased the most books (by total quantity) over the last year.

2. `author_revenue.sql`:
   Calculates the total revenue generated from book sales by each author.

3. `popular_books.sql`:
   Retrieves all books that have been ordered more than 10 times, along with the total quantity ordered for each book.

These queries are designed to work with a bookstore database containing customer, book, order, and order detail information.

## Database Schema

The queries work with the following tables:
- Customers (customer_id, name, email)
- Books (book_id, title, author, price)
- Orders (order_id, customer_id, order_date)
- OrderDetails (order_id, book_id, quantity)



