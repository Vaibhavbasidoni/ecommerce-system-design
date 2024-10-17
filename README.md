# E-Commerce System Design

This project presents a basic design and implementation for an e-commerce system, including a class diagram and code for the main components.

## Project Structure
project_root/
│
├── README.md
├── class_diagram.md
│
└── src/
├── models/
│ ├── user.py
│ ├── product.py
│ ├── order.py
│ └── payment.py
│
├── ecommerce_system.py
└── test_ecommerce_system.py


## Class Diagram

The class diagram outlining the relationships between User, Product, Order, and Payment is as follows:
classDiagram
    User "1" -- "*" Order
    Order "*" -- "*" Product
    Order "1" -- "1" Payment
    class User {
        +int id
        +string name
        +string email
        +List<Order> orders
        +create_order()
        +view_orders()
        +manage_order()
    }
    class Product {
        +int id
        +string name
        +float price
        +get_details()
    }
    class Order {
        +int id
        +User user
        +List<Product> products
        +float total_amount
        +string status
        +add_product()
        +remove_product()
        +update_status()
        +get_order_details()
    }
    class Payment {
        +int id
        +Order order
        +float amount
        +string payment_method
        +string status
        +process_payment()
        +get_payment_status()
    }

    
## Components

The system consists of the following main components:

1. User: Represents a customer who can create and manage orders.
2. Product: Represents items available for purchase.
3. Order: Represents a collection of products ordered by a user.
4. Payment: Represents the payment for an order.
5. ECommerceSystem: The main system that coordinates interactions between other components.

## How to Run

To run the test script and see the system in action:

1. Ensure you have Python 3.x installed on your system.
2. Navigate to the project root directory in your terminal or command prompt.
3. Run the following command:

   ```
   python src/test_ecommerce_system.py
   ```

This will execute the test script, demonstrating the basic functionality of the e-commerce system.

## Assumptions

1. A user can have multiple orders.
2. An order can contain multiple products.
3. Each order is associated with one payment.
4. The system does not include user authentication or authorization.
5. Inventory management is not implemented in this basic design.
6. The system does not interact with a database; all data is managed in-memory.

## Future Enhancements

To expand this basic e-commerce system, consider implementing the following:

1. Database integration for persistent data storage.
2. User authentication and authorization.
3. Inventory management system.
4. Order tracking and status updates.
5. Product categories and search functionality.
6. Shopping cart feature.
7. Integration with external payment gateways.

