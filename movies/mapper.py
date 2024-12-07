#!/usr/bin/env python3

import sys
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
for line in sys.stdin:
    if line.startswith("movie_title"):
        continue
    columns = line.strip().split(',')
    if len(columns) >= 8:
        movie_title = columns[0]
        review_content = columns[7]
        sentiment = sia.polarity_scores(review_content)
        print(f'{movie_title},{sentiment["compound"]}')
