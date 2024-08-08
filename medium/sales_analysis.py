# example output
# {
#     "total_sales": {
#         "A": 30,
#         "B": 15,
#         "C": 15
#     },
#     "top_selling_product": "A"
# }

from typing import List, Dict
from pprint import pprint


def analyze_sales_data(sales_records: List[Dict]) -> Dict:
    output = {
        "total_sales": {},
        "top_selling_product": None,
    }
    for entry in sales_records:
        product_name = entry["product"]
        output["total_sales"][product_name] = output["total_sales"].get(product_name, 0) + entry["price"] * entry["quantity"]
    max_sales = max(output["total_sales"].values())
    for key, val in output["total_sales"].items():
        if max_sales == val:
            output["top_selling_product"] = key
    return output


if __name__ == '__main__':
    sales = [
        {"product": "A", "price": 10, "quantity": 2, "date": "2023-01-01"},
        {"product": "B", "price": 15, "quantity": 1, "date": "2023-01-01"},
        {"product": "A", "price": 10, "quantity": 1, "date": "2023-01-02"},
        {"product": "C", "price": 5, "quantity": 3, "date": "2023-01-02"}
    ]
    output = analyze_sales_data(sales)
    pprint(output)