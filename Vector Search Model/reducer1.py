#!/usr/bin/env python3
import sys
import ast

def emit_vector(article_id, vector):
    vector_str = ', '.join([f"{word_id}:{score}" for word_id, score in vector.items()])
    print(f"{article_id}\t{vector_str}")

current_article_id = None
current_vector = {}

for line in sys.stdin:
    article_id, tf_idf_list_str = line.strip().split('\t', 1)
    tf_idf_list = ast.literal_eval(tf_idf_list_str)
    
    # If we're still on the same article, update the vector; else, emit the current vector and start a new one
    if article_id == current_article_id or current_article_id is None:
        for word_id, score in tf_idf_list:
            current_vector[word_id] = score
    else:
        emit_vector(current_article_id, current_vector)
        current_vector = {word_id: score for word_id, score in tf_idf_list}
    
    current_article_id = article_id

# Emit the last vector
if current_article_id is not None:
    emit_vector(current_article_id, current_vector)
