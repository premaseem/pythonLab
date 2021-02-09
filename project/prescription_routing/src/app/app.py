from typing import List

class InventoryItem:
    def __init__(self, drug, cost):
        self.drug = drug
        self.cost = cost

class OrderItem:
    def __init__(self, drug, quantity):
        self.drug = drug
        self.quantity = quantity
        self.cost = 0

class Pharmacy:
    def __init__(self, name):
        self.name = name
        self.inventory:List[InventoryItem] = []

    def add_inventory(self, inventory_item:InventoryItem):
        self.inventory.append(inventory_item)

    def estimate_order_item_cost(self, order_item: OrderItem) -> float:
        # find drug in inventory
        for available_drug in self.inventory:
            if order_item.drug in available_drug.drug:
                return order_item.drug * available_drug.cost
        return None






class Order:
    pass

class Assignment:
    pass



class Router:
    pass

