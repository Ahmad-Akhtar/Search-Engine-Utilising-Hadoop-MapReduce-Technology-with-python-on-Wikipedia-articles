#!/usr/bin/env python3
import sys
from collections import defaultdict

current_article_id = None
word_counts = defaultdict(int)
total_words = 0

def print_output(article_id, word_counts, total_words):
    term_freq_list = [(word_id, word_counts[word_id]) for word_id in word_counts]
    print(f"({article_id}:{term_freq_list})")

for line in sys.stdin:
    article_id, word_id, count = line.strip().split('\t')
    count = int(count)
    
    if article_id != current_article_id:
        if current_article_id is not None:
            print_output(current_article_id, word_counts, total_words)
        current_article_id = article_id
        word_counts.clear()
        total_words = 0
    
    word_counts[word_id] += count
    total_words += count

# Ensure the last article is processed
if current_article_id is not None:
    print_output(current_article_id, word_counts, total_words)
