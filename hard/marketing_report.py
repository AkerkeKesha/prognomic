"""
sample_input = [
    {
        "campaign_id": "CA001",
        "channel": "Social Media",
        "date": "2023-01-01",
        "impressions": 10000,
        "clicks": 500,
        "conversions": 50,
        "spend": 1000.00
    },
]
Edge Cases -
1. Null/non-existent keys: campaign_id, channel, date, etc
2. Empty strings: campaign_id, channel, date, numerics
3. Type mismatch: e.g. "1000" string instead of int
4. Outliers: e.g. 1 impressions, 2 clicks CTR > 1.0
5. Negative values, e.g. -10 spend
6. Non-date value for date
7. Division by zero: spend, impressions, clicks, conversions

Required Output Format:
{
    "total_campaigns": int,
    "total_impressions": int,
    "total_clicks": int,
    "total_conversions": int,
    "total_spend": float,
    "average_ctr": float,
    "average_cvr": float,
    "average_cpa": float,

    "top_performing_channel": str,

    "campaign_performance": [
        {
            "campaign_id": str,
            "channel": str,
            "roi": float
        },
        ...
    ]
}

CTR = clicks / impressions
CVR = conversions / clicks
CPA = spend / conversions
ROI = (conversions * 100 - spend ) / spend


"""
from typing import List, Dict
from collections import defaultdict
from pprint import pprint


def _is_valid(campaign: Dict) -> bool:
    return True


def process_marketing_data(campaigns: List[Dict]) -> Dict:
    report = {
        "total_campaigns": 0,
        "total_impressions": 0,
        "total_clicks": 0,
        "total_conversions": 0,
        "total_spend": 0.0,
        "average_ctr": 0.0,
        "average_cvr": 0.0,
        "average_cpa": 0.0,
        "top_performing_channel": "",
        "campaign_performance": [],
    }
    campaigns = [campaign for campaign in campaigns if _is_valid(campaign)]

    for campaign in campaigns:
        report["total_campaigns"] += 1
        report["total_impressions"] += campaign["impressions"]
        report["total_clicks"] += campaign["clicks"]
        report["total_conversions"] += campaign["conversions"]
        report["total_spend"] += campaign["spend"]

        report["average_ctr"] = round(report["total_clicks"] / report["total_impressions"], 2) if report["total_impressions"] else 0.0
        report["average_cvr"] = round(report["total_conversions"] / report["total_clicks"], 2) if report["total_clicks"] else 0.0
        report["average_cpa"] = round(report["total_spend"] / report["total_conversions"], 2) if report["total_conversions"] else 0.0

        campaign_roi = round((campaign["conversions"] * 100 - campaign["spend"]) / campaign["spend"], 2) if campaign["spend"] else 0.0
        campaign_dict = {
            "campaign_id": campaign["campaign_id"],
            "channel": campaign["channel"],
            "roi": campaign_roi,
        }
        report["campaign_performance"].append(campaign_dict)

    report["campaign_performance"].sort(key=lambda x: x["roi"], reverse=True)
    top_channel = report["campaign_performance"][0]["channel"]
    report["top_performing_channel"] = top_channel
    return report


if __name__ == '__main__':
    sample_input = [
        {
            "campaign_id": "CA002",
            "channel": "Organic search",
            "date": "2023-01-01",
            "impressions": 1000,
            "clicks": 200,
            "conversions": 20,
            "spend": 2000.00
        },
        {
            "campaign_id": "CA001",
            "channel": "Social Media",
            "date": "2023-01-01",
            "impressions": 10000,
            "clicks": 500,
            "conversions": 50,
            "spend": 1000.00
        },
        {
            "campaign_id": "CA003",
            "channel": "Google Ads",
            "date": "2023-01-02",
            "impressions": 0,
            "clicks": 0,
            "conversions": 0,
            "spend": 0.0
        },
    ]

    result = process_marketing_data(sample_input)
    pprint(result)
