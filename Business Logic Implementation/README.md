# Simple Inventory Management System

This project helps manage inventory for a warehouse. It can process orders, update stock levels, and restock items when needed.

## What it does

1. Processes orders and updates inventory
2. Alerts when items are running low
3. Restocks items

## How to use it

1. Make sure you have Python installed on your computer.
2. Save the `inventory_management.py` file on your computer.
3. Open a command prompt or terminal.
4. Go to the folder where you saved the file.
5. Type this command and press Enter:
   ```
   python inventory_management.py
   ```
## Functions

### `process_orders(products, orders, threshold=10)`

Processes a list of orders and updates the inventory accordingly.

- Parameters:
  - `products`: A dictionary of products and their current stock levels.
  - `orders`: A list of tuples, each containing a product name and order quantity.
  - `threshold`: The stock level below which a restock alert is generated (default: 10).
- Returns: A list of restock alerts.

### `restock_items(products, restock_list)`

Restocks items in the inventory.

- Parameters:
  - `products`: A dictionary of products and their current stock levels.
  - `restock_list`: A list of tuples, each containing a product name and restock quantity.


## How it works

- Uses dictionaries to store product information for quick access
- Checks for errors like ordering more items than available
- Alerts you when an item is running low

## Things to know

- Products are stored with their names and quantities
- You can't order more items than what's in stock
- The system assumes all numbers (stock, orders) are whole numbers

## Possible future updates

- Add a database to save information permanently
- Create a user-friendly interface
- Add features like automatic reordering

This system provides a simple way to manage inventory, process orders, and keep track of stock levels.
