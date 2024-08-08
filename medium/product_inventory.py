from typing import List, Dict
from pprint import pprint


def manage_inventory(inventory: List[Dict]) -> Dict:
    report = {
        "restock_needed": [],
        "inventory_value": {}
    }
    inventory_summary = report["inventory_value"]
    for entry in inventory:
        product_id = entry["product_id"]
        quantity = entry.get("quantity", 0)
        inventory_summary[product_id] = inventory_summary.get(product_id, 0) + entry["price"] * quantity
    restock = report["restock_needed"]
    cleaned_inventory = [entry for entry in inventory if "quantity" in entry]
    for entry in cleaned_inventory:
        product_id = entry["product_id"]
        quantity = entry["quantity"]
        if quantity < 5:
            restock.append(product_id)
    return report


if __name__ == '__main__':
    inventory = [
        {"product_id": "A", "product_name": "Product A", "quantity": 3, "price": 10},
        {"product_id": "B", "product_name": "Product B", "quantity": 6, "price": 15},
        {"product_id": "C", "product_name": "Product C", "quantity": 2, "price": 5},
        {"product_id": "D", "price": 20}
    ]
    output = manage_inventory(inventory)
    pprint(output)