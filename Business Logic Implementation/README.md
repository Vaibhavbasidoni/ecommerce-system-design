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

## Main functions

1. `process_orders()`: Handles orders and updates inventory
2. `restock_items()`: Adds more items to the inventory

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
