#!/usr/bin/env python3
import sys
import re

for line in sys.stdin:
    # Assuming CSV format: ARTICLE_ID,TITLE,SECTION_TITLE,SECTION_TEXT
    # Extract SECTION_TEXT
    section_text = line.strip().split(',')[-1]
    # Tokenize and normalize the text
    words = re.findall(r'\b[a-zA-Z]+\b', section_text.lower())
    for word in words:
        print(word)
