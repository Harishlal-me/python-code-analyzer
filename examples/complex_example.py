"""
Module for handling customer orders
"""
import json
import logging
from datetime import datetime
from typing import List, Dict

logger = logging.getLogger(__name__)

class Order:
    """Represents a customer order"""
    
    def __init__(self, order_id: str, customer_id: str):
        self.order_id = order_id
        self.customer_id = customer_id
        self.items = []
        self.created_at = datetime.now()
    
    def add_item(self, item_id: str, quantity: int, price: float):
        """Add an item to the order"""
        self.items.append({
            'item_id': item_id,
            'quantity': quantity,
            'price': price
        })
        logger.info(f"Added item {item_id} to order {self.order_id}")
    
    def calculate_total(self) -> float:
        """Calculate total order value"""
        total = sum(item['quantity'] * item['price'] for item in self.items)
        return round(total, 2)
    
    def to_dict(self) -> Dict:
        """Convert order to dictionary"""
        return {
            'order_id': self.order_id,
            'customer_id': self.customer_id,
            'items': self.items,
            'total': self.calculate_total(),
            'created_at': self.created_at.isoformat()
        }


class OrderManager:
    """Manages multiple orders"""
    
    def __init__(self):
        self.orders = {}
    
    def create_order(self, customer_id: str) -> Order:
        """Create a new order"""
        order_id = f"ORD-{len(self.orders) + 1:04d}"
        order = Order(order_id, customer_id)
        self.orders[order_id] = order
        return order
    
    def get_order(self, order_id: str) -> Order:
        """Retrieve an order by ID"""
        return self.orders.get(order_id)
    
    def get_customer_orders(self, customer_id: str) -> List[Order]:
        """Get all orders for a customer"""
        return [order for order in self.orders.values() 
                if order.customer_id == customer_id]


def validate_order_data(data: Dict) -> bool:
    """Validate order data structure"""
    required_fields = ['order_id', 'customer_id', 'items']
    return all(field in data for field in required_fields)


def export_orders_to_json(orders: List[Order], filename: str):
    """Export orders to JSON file"""
    with open(filename, 'w') as f:
        json.dump([order.to_dict() for order in orders], f, indent=2)