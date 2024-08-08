from typing import List, Dict, Tuple
from pprint import pprint


def categorize_score(scores: List[int]) -> Tuple[List, List, List]:
    positive, neutral, negative = [], [], []
    for idx, score in enumerate(scores):
        if score >= 4:
            positive.append(idx)
        elif score == 3:
            neutral.append(idx)
        else:
            negative.append(idx)
    return positive, neutral, negative


def calculate_score(scores: List[str]) -> float:
    total, count = 0, 0
    for score in scores:
        total += int(score)
        count += 1
    return round(total / count, 2)


def process_feedback(feedback: List[str]) -> Dict:
    output = {
        "average_score": None,
        "feedback_summary": {
            "positive": [],
            "neutral": [],
            "negative": [],
        }
    }
    delimiter = ", "
    feedback = [entry for entry in feedback if delimiter in entry]
    scores = [int(entry.split(", ")[1]) for entry in feedback]
    average_score = calculate_score(scores)
    output["average_score"] = average_score
    positive, neutral, negative = categorize_score(scores)
    feedback_summary = output["feedback_summary"]
    for i in range(len(feedback)):
        if i in positive:
            feedback_summary["positive"].append(feedback[i])
        elif i in neutral:
            feedback_summary["neutral"].append(feedback[i])
        else:
            feedback_summary["negative"].append(feedback[i])
    return output


if __name__ == '__main__':
    feedback = [
        "Great service, 5",
        "Terrible experience, 1",
        "Okay, 3",
        "Not satisfied",
        "Excellent, 4"
    ]
    output = process_feedback(feedback)
    pprint(output)