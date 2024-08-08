from typing import List, Dict
from pprint import pprint


def track_attendance(attendance: List[Dict]) -> Dict:
    output = {
        "total_days_present": {},
        "perfect_attendance": set()
    }
    presence = output["total_days_present"]
    attendance = [entry for entry in attendance if "status" in entry]
    for entry in attendance:
        employee_id = entry["employee_id"]
        if entry["status"] == "present":
            presence[employee_id] = presence.get(employee_id, 0) + 1
        elif entry["status"] == "absent":
            presence[employee_id] = presence.get(employee_id, 0)
    employee_ids = [entry["employee_id"] for entry in attendance]
    counter = {}
    for employee_id in employee_ids:
        counter[employee_id] = counter.get(employee_id, 0) + 1
    for employee_id in employee_ids:
        if counter[employee_id] == presence[employee_id]:
            output["perfect_attendance"].add(employee_id)
    return output


if __name__ == '__main__':
    attendance = [
        {"employee_id": "001", "date": "2023-01-01", "status": "present"},
        {"employee_id": "002", "date": "2023-01-01", "status": "absent"},
        {"employee_id": "001", "date": "2023-01-02", "status": "present"},
        {"employee_id": "002", "date": "2023-01-02"},
        {"employee_id": "001", "date": "2023-01-03", "status": "present"}
    ]
    output = track_attendance(attendance)
    pprint(output)
