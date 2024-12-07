#!/usr/bin/env python3

import sys
current_movie = None
total_sentiment = 0.0
num_reviews = 0
for line in sys.stdin:
    movie, sentiment = line.strip().split(',')

    if current_movie != movie:
        if current_movie is not None:
            average_sentiment = total_sentiment / num_reviews
            print(f'{current_movie},{average_sentiment:.2f}')
        current_movie = movie
        total_sentiment = 0.0
        num_reviews = 0

    sentiment_score = float(sentiment)
    total_sentiment += sentiment_score
    num_reviews += 1

if current_movie is not None:
    average_sentiment = total_sentiment / num_reviews
    print(f'{current_movie},{average_sentiment:.2f}')
