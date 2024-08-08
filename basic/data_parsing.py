# Example output
# [
#     {"name": "Alice", "id": "001", "age": 30, "department": "Engineering"},
#     {"name": "Bob", "id": "002", "age": 25, "department": "Marketing"},
#     {"name": "Charlie", "id": None, "age": 28, "department": "Engineering"},
#     {"name": None, "id": "004", "age": 35, "department": "Marketing"}
# ]
from typing import List, Dict
from pprint import pprint


def parse_employee_records(data: str) -> List[Dict]:
    employee_records = []
    lines = data.split("\n")
    for line in lines:
        name, _id, age, department = line.split(",")

        entry = {
            "name": str(name) if name else None,
            "id": str(_id) if _id else None,
            "age": int(age),
            "department": str(department)
        }
        employee_records.append(entry)
    return employee_records


if __name__ == '__main__':
    data = """Alice,001,30,Engineering
    Bob,002,25,Marketing
    Charlie,,28,Engineering
    ,004,35,Marketing"""
    employee_records = parse_employee_records(data)
    pprint(employee_records)

