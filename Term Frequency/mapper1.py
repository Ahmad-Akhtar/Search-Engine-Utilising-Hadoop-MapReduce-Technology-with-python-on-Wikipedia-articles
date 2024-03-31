#!/usr/bin/env python3
import sys
import re

# Load the vocabulary into a dictionary
term_to_id = {}
with open("/home/ahmad/Downloads/BigDataAss2/vocab.txt", "r") as f:
    for line in f:
        term_id, term = line.strip().split("\t")
        term_to_id[term] = term_id

for line in sys.stdin:
    article_id, section_text = line.strip().split(',', 1)
    words = re.findall(r'\b[a-zA-Z]+\b', section_text.lower())
    for word in words:
        if word in term_to_id:  # Verify if the word is in the vocabulary
            print(f"{article_id}\t{term_to_id[word]}\t1")
