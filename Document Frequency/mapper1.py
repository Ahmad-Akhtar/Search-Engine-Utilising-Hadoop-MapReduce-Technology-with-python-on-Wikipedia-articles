#!/usr/bin/env python3
import sys
import re
import ast

for line in sys.stdin:
    # Pattern: (article_id:,[('word_id', count), ...])
    # Isolate article_id and the list part
    article_id, word_list_str = re.match(r"\((\d+):\[(.*)\]\)", line.strip()).groups()
    
    # Convert list part from string to a list of tuples
    word_list = ast.literal_eval(f"[{word_list_str}]")
    
    # Process each word_id in word_list
    for word_id, _ in word_list:
        # Output word_id and article_id, excluding count for DF calculation
        print(f"{word_id}\t{article_id}")
