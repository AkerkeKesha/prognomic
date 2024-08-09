'''
input:

sample_input = [
    {
        "patient_id": "P001",
        "age": 45,
        "fever": 38.5,
        "cough": True,
        "fatigue": True,
        "difficulty_breathing": False,
        "blood_test_result": 11.2,
        "x_ray_result": "abnormal"
    },
    # Add more sample patients here
]

output:
{
    "high_risk_patients": [str],  # list of patient_ids
    "total_patients": int,
    "high_risk_percentage": float,
    "average_age": float,
    "most_common_symptom": str,
    "blood_test_summary": {
        "min": float,
        "max": float,
        "average": float
    },
    "x_ray_summary": {
        "normal": int,
        "abnormal": int,
        "inconclusive": int
    }
}

Notes:
- most_common_symptom in [fatigue, cough, difficulty_breathing]
- round decimal to 2
- empty patients list, i.e. count(patients) = 0
- If a tie for the most common symptom, return any of the tied symptoms

Edge Cases:
- all keys present in entry
- keys match their described types, e.g. patient_id: str
- age should be between 0 and 120 (inclusive)
- abnormal fever: fever < 0 or fever > 60
- blood_test < 0

'''
from typing import Dict, List
from pprint import pprint
from collections import Counter


def _is_valid(patient) -> bool:
    must_keys = {"patient_id",
        "age",
        "fever",
        "cough",
        "fatigue",
        "difficulty_breathing",
        "blood_test_result",
        "x_ray_result"
    }
    if set(patient.keys()) != must_keys:
        return False
    if patient["age"] < 0:
        return False
    if patient["age"] > 120:
        return False
    if patient["fever"] < 0:
        return False
    if patient["blood_test_result"] < 0:
        return False
    return True


def is_high_risk(patient: Dict) -> bool:
    risk_factors = [
        patient["fever"] > 38.0,
        patient["cough"],
        patient["fatigue"],
        patient["difficulty_breathing"],
        patient["blood_test_result"] > 10.0,
        patient["x_ray_result"] == "abnormal",
    ]
    return sum(risk_factors) >= 3


def analyze_disease_data(patients: List[Dict]) -> Dict:
    report = {
        "high_risk_patients": [],
        "total_patients": 0,
        "high_risk_percentage": 0.0,
        "average_age": 0.0,
        "most_common_symptom": "",
        "blood_test_summary": {},
        "x_ray_summary": {
            "normal": 0,
            "abnormal": 0,
            "inconclusive": 0
        }

    }
    patients = [patient for patient in patients if _is_valid(patient)]
    if not patients:
        return report
    total_patients, sum_age, high_risks = 0, 0, 0
    blood_test, x_rays, symptoms = [], [], []

    for patient in patients:
        total_patients += 1
        sum_age += patient["age"]
        blood_test.append(patient["blood_test_result"])
        x_rays.append(patient["x_ray_result"])

        for symptom in ["cough", "fatigue", "difficulty_breathing"]:
            if patient[symptom]:
                symptoms.append(symptom)

        if is_high_risk(patient):
            report["high_risk_patients"].append(patient["patient_id"])
            high_risks += 1

    report["high_risk_percentage"] = high_risks / total_patients
    report["total_patients"] = total_patients
    report["average_age"] = sum_age / total_patients

    report["blood_test_summary"] = {
        "min": min(blood_test),
        "max": max(blood_test),
        "average": sum(blood_test) / len(blood_test)
    }
    x_ray_counts = Counter(x_rays)
    report["x_ray_summary"] = {
        key: count for key, count in x_ray_counts.items()
    }
    symptom, _ = Counter(symptoms).most_common(1)[0]  # [(key, val)]
    report["most_common_symptom"] = symptom
    return report


if __name__ == '__main__':
    sample_input = [
        {
            "patient_id": "P001",
            "age": 45,
            "fever": 38.5,
            "cough": True,
            "fatigue": True,
            "difficulty_breathing": False,
            "blood_test_result": 11.2,
            "x_ray_result": "abnormal"
        },
        {
            "patient_id": "P002",
            "age": 40,
            "fever": 30.5,
            "cough": True,
            "fatigue": False,
            "difficulty_breathing": False,
            "blood_test_result": 11.2,
            "x_ray_result": "normal"
        },
        {},
        {
            "patient_id": "P002",
            "age": -40,
            "fever": 30.5,
            "cough": True,
            "fatigue": False,
            "difficulty_breathing": False,
            "blood_test_result": 11.2,
            "x_ray_result": "normal"
        },

    ]

    result = analyze_disease_data(sample_input)
    pprint(result)