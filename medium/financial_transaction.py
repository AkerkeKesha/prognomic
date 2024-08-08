from typing import List, Dict
from pprint import pprint


def analyze_transactions(transactions: List[Dict]) -> Dict:
    report = {
        "total_by_currency": {},
        "highest_transaction": {}
    }
    by_currency = report["total_by_currency"]
    amounts = []
    for entry in transactions:
        currency = entry["currency"]
        if entry["amount"] == "invalid":
            amount = 0
        else:
            amount = entry.get("amount", 0)
        by_currency[currency] = by_currency.get(currency, 0) + amount
        amounts.append(amount)
    max_amount = max(amounts)
    for entry in transactions:
        if entry["amount"] == max_amount:
            max_val_transaction = {
                "transaction_id": entry["transaction_id"],
                "amount": int(entry["amount"]),
                "currency": entry["currency"]
            }
    report["highest_transaction"] = max_val_transaction
    return report


if __name__ == '__main__':
    transactions = [
        {"transaction_id": "T1", "amount": 100, "currency": "USD", "date": "2023-01-01"},
        {"transaction_id": "T2", "amount": 200, "currency": "EUR", "date": "2023-01-02"},
        {"transaction_id": "T3", "amount": 150, "currency": "USD", "date": "2023-01-03"},
        {"transaction_id": "T4", "amount": "invalid", "currency": "USD", "date": "2023-01-04"},
        {"transaction_id": "T5", "amount": 300, "currency": "EUR"}
    ]
    output = analyze_transactions(transactions)
    pprint(output)