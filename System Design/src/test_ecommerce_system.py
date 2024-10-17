from ecommerce_system import ECommerceSystem

def test_ecommerce_system():
    print("Starting E-Commerce System Test")
    print("-------------------------------")

    # Initialize the e-commerce system
    ecommerce = ECommerceSystem()

    # Test user registration
    print("\nTesting User Registration:")
    alice = ecommerce.register_user("Alice", "alice@example.com")
    bob = ecommerce.register_user("Bob", "bob@example.com")
    print(f"Registered users: Alice (ID: {alice.id}), Bob (ID: {bob.id})")

    # Test product addition
    print("\nTesting Product Addition:")
    laptop = ecommerce.add_product("Laptop", 999.99)
    phone = ecommerce.add_product("Smartphone", 499.99)
    headphones = ecommerce.add_product("Wireless Headphones", 149.99)
    print(f"Added products: {laptop.name}, {phone.name}, {headphones.name}")

    # Test order creation
    print("\nTesting Order Creation:")
    alice_order = ecommerce.create_order(alice.id)
    bob_order = ecommerce.create_order(bob.id)
    print(f"Created orders: Alice (Order ID: {alice_order.id}), Bob (Order ID: {bob_order.id})")

    # Test adding products to orders
    print("\nTesting Adding Products to Orders:")
    ecommerce.add_product_to_order(alice_order.id, laptop.id)
    ecommerce.add_product_to_order(alice_order.id, headphones.id)
    ecommerce.add_product_to_order(bob_order.id, phone.id)
    print(f"Added products to orders: Alice (Order ID: {alice_order.id}), Bob (Order ID: {bob_order.id})")

    # Test order details
    print("\nTesting Order Details:")
    print("Alice's order:")
    print(f"  Order ID: {alice_order.id}")
    print(f"  User: {alice_order.user.name}")
    print("  Products:")
    for product in alice_order.products:
        print(f"    - {product.name}: ${product.price}")
    print(f"  Total amount: ${alice_order.total_amount}")
    print(f"  Status: {alice_order.status}")

    print("\nBob's order:")
    print(f"  Order ID: {bob_order.id}")
    print(f"  User: {bob_order.user.name}")
    print("  Products:")
    for product in bob_order.products:
        print(f"    - {product.name}: ${product.price}")
    print(f"  Total amount: ${bob_order.total_amount}")
    print(f"  Status: {bob_order.status}")

    # Test payment processing
    print("\nTesting Payment Processing:")
    alice_payment_success = ecommerce.process_payment(alice_order.id, "credit_card")
    bob_payment_success = ecommerce.process_payment(bob_order.id, "paypal")
    print(f"Alice's payment successful: {alice_payment_success}")
    print(f"Bob's payment successful: {bob_payment_success}")

    # Test order status update
    print("\nTesting Order Status Update:")
    ecommerce.update_order_status(alice_order.id, "shipped")
    print("Updated Alice's order status to 'shipped'")
    print(f"Alice's updated order status: {alice_order.status}")

    # Test viewing user orders
    print("\nTesting Viewing User Orders:")
    alice_orders = ecommerce.get_user_orders(alice.id)
    bob_orders = ecommerce.get_user_orders(bob.id)
    print(f"Alice's orders: {len(alice_orders)}")
    print(f"Bob's orders: {len(bob_orders)}")

    # Test error handling
    print("\nTesting Error Handling:")
    try:
        ecommerce.get_user_orders(999)  # Non-existent user ID
    except ValueError as e:
        print(f"Expected error caught: {e}")

    try:
        ecommerce.add_product_to_order(999, laptop.id)  # Non-existent order ID
    except ValueError as e:
        print(f"Expected error caught: {e}")

    try:
        alice_order.update_status("invalid_status")  # Invalid status
    except ValueError as e:
        print(f"Expected error caught: {e}")

    print("\nE-Commerce System Test Completed")

if __name__ == "__main__":
    test_ecommerce_system()
