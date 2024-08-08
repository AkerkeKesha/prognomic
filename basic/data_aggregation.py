from typing import List, Dict
from collections import defaultdict
from pprint import pprint


def average_age_by_department(employees: List[Dict]) -> Dict[str, float]:
    department = defaultdict(list)
    for entry in employees:
        key = entry["department"]
        department[key].append(entry["age"])
    return {key: sum(val) / len(val) for key, val in department.items()}


if __name__ == '__main__':
    employees = [
        {"name": "Alice", "id": "001", "age": 30, "department": "Engineering"},
        {"name": "Bob", "id": "002", "age": 25, "department": "Marketing"},
        {"name": "Charlie", "id": "003", "age": 28, "department": "Engineering"},
        {"name": "David", "id": "004", "age": 35, "department": "Marketing"}
    ]
    department_data = average_age_by_department(employees)
    pprint(department_data)