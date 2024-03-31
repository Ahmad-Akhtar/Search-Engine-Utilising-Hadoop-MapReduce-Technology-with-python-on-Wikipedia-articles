#!/usr/bin/env python3
import sys

# Mapper processes each line, anticipating "word_id count"
for line in sys.stdin:
    # Split the line into word_id and count based on whitespace
    line_parts = line.strip().split()
    if len(line_parts) == 2:
        word_id, count = line_parts
        # Emit the word_id and count
        print(f"{word_id}\t{count}")
