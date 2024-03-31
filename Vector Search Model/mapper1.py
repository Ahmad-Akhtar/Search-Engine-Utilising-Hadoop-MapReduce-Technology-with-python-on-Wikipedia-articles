#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    article_id, tf_idf_list_str = line.split(':')
    print(f"{article_id}\t{tf_idf_list_str}")
