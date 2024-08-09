'''
Input:
comments =
[
    "Great product. Loved all",
    "Did not like it.",
    "seems fine to me",

]

Output:
{
    "total_comments": int,
    "average_word_count": float,
    "sentiment_distribution": {
        "positive": float,
        "neutral": float,
        "negative": float
    },
    "top_keywords": [str, str, str, str, str],
    "longest_comment": str,
    "shortest_comment": str
}

positive = ["good", "great", "excellent", "love", "best"]
negative = ["bad", "poor", "terrible", "worst", "hate"]

Clarifications:
1. average_word_count = total_words / total_comments
2. distibution as percentage: 0.1, 0.9, 0.0 (or 2 decimal, or out of 100) - float decimals?
3. common_english_words = ["the", "a", "an", "in", "on", "at", "to", "for", "of", "and", "is", "are", "was", "were"]
4. top_keywords, longest/shortest - lower_case?
5. handle punctuation = !()-[]{};:'"\,<>./?@#$%^&*_~
6. what if comment contains both negative and positive words: how to decide the sentiment?

Edge Cases:
1. Keys are missing in the entry
2. Empty strings/comments
3. division by zero, what if no comments
4. type of comment - str
5. all uppercase/lowercase
6. duplicate words

'''
from typing import List, Dict
from collections import Counter
from pprint import pprint


def remove_punctuation(comment: str) -> str:
    punctuation = "!()-[]{};:',<>./?@#$%^&*_~"
    for char in comment:
        if char in punctuation:
            clean_comment = comment.replace(char, "")
    return clean_comment


def analyze_sentiment(comment: str) -> str:
    positive = set(["good", "great", "excellent", "love", "best"])
    negative = set(["bad", "poor", "terrible", "worst", "hate"])
    words = set(comment.lower().split())
    pos_count = len(words.intersection(positive))
    neg_count = len(words.intersection(negative))
    if pos_count > neg_count:
        return "positive"
    elif neg_count > pos_count:
        return "negative"
    else:
        return "neutral"


def get_top_keywords(words: List[str], n: int = 5) -> List:
    common_words = {"the", "a", "an", "in", "on", "at", "to", "for", "of", "and", "is", "are", "was", "were"}
    word_counts = Counter(word for word in words if word not in common_words)
    return [word for word, _ in word_counts.most_common(n)]


def analyze_customer_feedback(comments: List[str]) -> Dict:
    report = {
        "total_comments": 0,
        "average_word_count": 0.00,
        "sentiment_distribution": {
            "positive": 0.00,
            "neutral": 0.00,
            "negative": 0.00
        },
        "top_keywords": [],
        "longest_comment": "",
        "shortest_comment": ""
    }

    comments = [comment.strip().lower() for comment in comments if comment.strip()]
    if not comments:
        return report
    comments = [remove_punctuation(comment) for comment in comments]
    total_comments = len(comments)
    words =[word for comment in comments for word in comment.split()]
    total_words = len(words)

    report["total_comments"] = total_comments
    report["average_word_count"] = total_words / report["total_comments"]

    report["longest_comment"] = max(comments, key=len)
    report["shortest_comment"] = min(comments, key=len)

    sentiments = [analyze_sentiment(comment) for comment in comments]
    sentiment_counts = Counter(sentiments)

    report["sentiment_distribution"] = {
        sentiment: count / total_comments for sentiment, count in sentiment_counts.items()
    }
    report["top_keywords"] = get_top_keywords(words, n=5)

    return report


if __name__ == '__main__':
    sample_comments = [
        "The product is great! I love how easy it is to use.",
        "Poor customer service. I've been waiting for a response for days.",
        "It's okay, nothing special but gets the job done.",
        "Best purchase I've made this year! Highly recommend to everyone.",
        "Terrible experience. The product broke after two days."
    ]

    result = analyze_customer_feedback(sample_comments)
    pprint(result)

    # total_words = 12+11+9+10+8 = 50
    # top_keywords = [product, days, ive]

