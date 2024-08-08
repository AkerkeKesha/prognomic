# Questions
# can we safely assume all entries are valid: no KeyError, correct departments, etc

from typing import List, Dict
from collections import defaultdict
from pprint import pprint


def group_by_department(employee_records: List) -> Dict[str, List]:
    departments = defaultdict(list)
    for entry in employee_records:
        key = entry["department"]
        departments[key].append(entry)
    return departments


if __name__ == '__main__':
    employees = [
        {"name": "Alice", "id": "001", "age": 30, "department": "Engineering"},
        {"name": "Bob", "id": "002", "age": 25, "department": "Marketing"},
        {"name": "Charlie", "id": "003", "age": 28, "department": "Engineering"},
        {"name": "David", "id": "004", "age": 35, "department": "Marketing"}
    ]
    by_department = group_by_department(employees)
    pprint(by_department)



# Example output
# {
#     "Engineering": [
#         {"name": "Alice", "id": "001", "age": 30, "department": "Engineering"},
#         {"name": "Charlie", "id": "003", "age": 28, "department": "Engineering"}
#     ],
#     "Marketing": [
#         {"name": "Bob", "id": "002", "age": 25, "department": "Marketing"},
#         {"name": "David", "id": "004", "age": 35, "department": "Marketing"}
#     ]
# }
