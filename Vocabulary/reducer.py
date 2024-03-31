#!/usr/bin/env python3
import sys

current_word_id = 0
current_word = None

for line in sys.stdin:
    word = line.strip()
    if word != current_word:
        print(f"{current_word_id}\t{word}")
        current_word = word
        current_word_id += 1
