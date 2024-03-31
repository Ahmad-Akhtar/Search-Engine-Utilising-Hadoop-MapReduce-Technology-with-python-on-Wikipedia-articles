query = "anarchism anarchy philosophy aa"
tokens = query.lower().split()  # Simple tokenization, can be adjusted as necessary.

# Load the vocabulary to map terms to IDs
vocab = {}
with open("/home/ahmad/Downloads/BigDataAss2/vocab.txt", "r") as f:
    for line in f:
        term_id, term = line.strip().split("\t")
        vocab[term] = term_id

# Count occurrences of each token to determine term frequencies
token_counts = {}
for token in tokens:
    if token in vocab:  # Consider only tokens present in the vocabulary
        term_id = vocab[token]
        if term_id not in token_counts:
            token_counts[term_id] = 0
        token_counts[term_id] += 1

# Prepare the token counts for further processing, such as MapReduce, by writing to a file
with open("query.txt", "w") as f:
    for term_id, count in token_counts.items():
        f.write(f"{term_id}\t{count}\n")  # Write each term ID with its corresponding count
