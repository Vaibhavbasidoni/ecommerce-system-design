from ecommerce_system import ECommerceSystem

def main():
    # Initialize the e-commerce system
    ecommerce = ECommerceSystem()

    # Register users
    alice = ecommerce.register_user("Alice", "alice@example.com")
    bob = ecommerce.register_user("Bob", "bob@example.com")

    # Add products
    laptop = ecommerce.add_product("Laptop", 999.99)
    phone = ecommerce.add_product("Smartphone", 499.99)
    headphones = ecommerce.add_product("Wireless Headphones", 149.99)

    # Create orders
    alice_order = ecommerce.create_order(alice.id)
    bob_order = ecommerce.create_order(bob.id)

    # Add products to orders
    ecommerce.add_product_to_order(alice_order.id, laptop.id)
    ecommerce.add_product_to_order(alice_order.id, headphones.id)
    ecommerce.add_product_to_order(bob_order.id, phone.id)

    # Process payments
    alice_payment_success = ecommerce.process_payment(alice_order.id, "credit_card")
    bob_payment_success = ecommerce.process_payment(bob_order.id, "paypal")

    # Print order details
    print("Alice's order:", alice_order.get_order_details())
    print("Bob's order:", bob_order.get_order_details())

    # Update order status
    ecommerce.update_order_status(alice_order.id, "shipped")

    # Print updated order details
    print("Alice's updated order:", alice_order.get_order_details())

    # View user orders
    alice_orders = ecommerce.get_user_orders(alice.id)
    print(f"Alice's orders: {len(alice_orders)}")

if __name__ == "__main__":
    main()
