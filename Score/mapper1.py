#!/usr/bin/env python3
import sys
import re
import ast

for line in sys.stdin:
    line = line.strip()
    # The input is expected to be TF data in the format: (article_id:[('word_id', count), ...])
    if line.startswith("("):
        # Match the expected TF data format
        match = re.match(r"\((\d+):\s*\[(.*)\]\)", line)
        if match:
            article_id, word_list_str = match.groups()
            # Ensure the string is in a proper list format for evaluation
            word_list_str = "[" + word_list_str + "]"
            try:
                # Safely convert the string representation to a list of tuples
                word_list = ast.literal_eval(word_list_str)
                for word_id, count in word_list:
                    # Output without TF indicator: word_id, article_id, and count
                    print(f"{article_id}\t{word_id}\t{count}")
            except SyntaxError as e:
                # Handle any errors during string evaluation
                print(f"Error evaluating line: {line} | Error: {e}", file=sys.stderr)
        else:
            # Handle lines that do not match the expected format
            print(f"Error parsing line: {line}", file=sys.stderr)
