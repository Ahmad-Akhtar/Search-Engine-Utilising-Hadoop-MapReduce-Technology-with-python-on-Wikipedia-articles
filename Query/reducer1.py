#!/usr/bin/env python3
import sys
import math

# Load document frequency (DF) values. In a real scenario, this might come from distributed cache or external storage
df_values = {}
total_documents = 817111  # Total number of documents in the corpus
with open("/home/ahmad/Downloads/BigDataAss2/df.txt", "r") as f:
    for line in f:
        term_id, df_count = line.strip().split("\t")
        df_values[term_id] = int(df_count)

# Function to calculate Inverse Document Frequency (IDF)
def calculate_idf(total_docs, df):
    return math.log((total_docs / df), 10) if df else 0

# Calculate TF-IDF for each term in the query
query_vector = {}
squared_sum = 0
for line in sys.stdin:
    term_id, tf = line.strip().split("\t")
    tf = int(tf)
    if term_id in df_values:
        idf = calculate_idf(total_documents, df_values[term_id])
        tf_idf = tf * idf
        query_vector[term_id] = tf_idf
        squared_sum += tf_idf ** 2  # For normalization

# Normalize the query vector
normalization_factor = math.sqrt(squared_sum)
for term_id in query_vector:
    query_vector[term_id] /= normalization_factor

# Emit the normalized TF-IDF scores for the query vector
for term_id, normalized_tf_idf in query_vector.items():
    print(f"{term_id}\t{normalized_tf_idf}")
