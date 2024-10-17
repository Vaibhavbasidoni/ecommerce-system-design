from typing import List, Dict, Tuple

def process_orders(products: Dict[str, int], orders: List[Tuple[str, int]], threshold: int = 10) -> List[str]:
    alerts = []
    
    for product, quantity in orders:
        if product not in products:
            raise ValueError(f"Product '{product}' not found in inventory.")
        
        if products[product] < quantity:
            raise ValueError(f"Insufficient stock for product '{product}'. Available: {products[product]}, Ordered: {quantity}")
        
        products[product] -= quantity
        
        if products[product] < threshold:
            alerts.append(f"Alert: Restock needed for '{product}'. Current stock: {products[product]}")
    
    return alerts

def restock_items(products: Dict[str, int], restock_list: List[Tuple[str, int]]) -> None:
    for product, quantity in restock_list:
        if product not in products:
            raise ValueError(f"Product '{product}' not found in inventory.")
        
        if quantity <= 0:
            raise ValueError(f"Invalid restock quantity for '{product}'. Must be greater than 0.")
        
        products[product] += quantity

# Example usage:
if __name__ == "__main__":
    inventory = {"apple": 50, "banana": 30, "orange": 25}
    orders = [("apple", 20), ("banana", 15), ("orange", 20)]
    
    try:
        restock_alerts = process_orders(inventory, orders)
        print("Updated inventory after orders:", inventory)
        for alert in restock_alerts:
            print(alert)
        
        restock_list = [("apple", 30), ("orange", 15)]
        restock_items(inventory, restock_list)
        print("Updated inventory after restocking:", inventory)
    except ValueError as e:
        print(f"Error: {e}")
