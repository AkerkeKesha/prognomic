from typing import List, Dict
from pprint import pprint


def filter_employees_by_age(employees: List[Dict], age_threshold:int) -> List[Dict]:
    return [entry for entry in employees if entry["age"] >= age_threshold]


if __name__ == '__main__':
    employees = [
        {"name": "Alice", "id": "001", "age": 30, "department": "Engineering"},
        {"name": "Bob", "id": "002", "age": 25, "department": "Marketing"},
        {"name": "Charlie", "id": "003", "age": 28, "department": "Engineering"},
        {"name": "David", "id": "004", "age": 35, "department": "Marketing"}
    ]
    age_threshold = 28
    filtered = filter_employees_by_age(employees, age_threshold)
    pprint(filtered)