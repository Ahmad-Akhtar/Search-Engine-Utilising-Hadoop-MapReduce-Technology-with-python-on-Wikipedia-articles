#!/usr/bin/env python3
import sys

# Mapper emits the document ID and its vector.
for line in sys.stdin:
    line = line.strip()
    if line:
        # Assuming the document vector format is: "(doc_id) vector"
        doc_id, vector_str = line[1:].split(')\t', 1)  # Remove leading '(' and split on ")\t"
        print(f"{doc_id}\t{vector_str}")
