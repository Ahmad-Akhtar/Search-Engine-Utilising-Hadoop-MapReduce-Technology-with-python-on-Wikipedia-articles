#!/usr/bin/env python3
import sys
from collections import defaultdict

# Keep track of the current word and a set of articles it has occurred in
current_word_id = None
articles = set()

for line in sys.stdin:
    word_id, article_id = line.strip().split('\t')
    
    # If it's the same word, add the article to the set
    if word_id == current_word_id:
        articles.add(article_id)
    else:
        # If it's a new word, but not the first one encountered
        if current_word_id is not None:
            # Output the word and the count of unique articles it appeared in
            print(f"{current_word_id}\t{len(articles)}")
        
        # Reset for the new word
        current_word_id = word_id
        articles = {article_id}

# Output the last word if there is one
if current_word_id is not None:
    print(f"{current_word_id}\t{len(articles)}")
