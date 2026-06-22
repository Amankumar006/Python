# program 6
# pip install transformers torch

from transformers import pipeline

sa = pipeline("sentiment-analysis")
reviews = [
    "the delivery was fast, i liked it",
    "product quality was not good ",
    "the product broke in two days",
    "the experience was average",
]

print("sentiment analysis result:\n")
for text, res in zip(reviews, sa(reviews)):
    print("input sentence: ", text)
    print(f"Predicted Sentiment: {res['label']}")
    print(f"Confidence Score: {res['score']:.4f}")
    print()
