# Search Engine Utilising Hadoop MapReduce Technology with python on Wikipedia articles
This repository has files used for developing a Naive Search Engine Utilising Apache Hadoop MapReduce Technology on a dataset in comma-separated values (CSV) format containing around 5 million Wikipedia articles provided by Wikimedia.

# Collaborators :
The group members for this assignment are :
- Ahmad Akhtar 21I-1655
- Inam ul Haq 22I-1906
- Abdurrehman 22I-1963


# Data Set 
You can download data set from this link 
"https://drive.google.com/file/d/1lGVGqzF5CNWaoV-zoz8_mlThvHwMgcsP/view"

# Dependencies: 
Important Libraries required for the preprocessing of this data and to create a sample data are listed below :

- import pandas as pd
- import nltk
- import string
- import time
- from tqdm import tqdm
- import numpy as np
- import os
- import tempfile
- import nltk
- from nltk.corpus import stopwords
- from nltk.tokenize import word_tokenize


# Pre Processing data:
First , I load the dataset and select Relevent Columns. Then I convert the text to lowercase, tokenizes it, and removes stopwords, punctuation, and special characters while ensuring to eliminate any empty strings. Then, it divides the dataset into manageable chunks, processing each chunk separately and saving them temporarily. Afterward, it merges all the processed chunks into a single dataset. The process is optimized for memory and time efficiency, with the total preprocessing time tracked and printed at the end. Lastly, it cleans up the temporary files created during the process. 
This systematic approach is crucial for handling extensive datasets effectively, which is essential for generating reports. 

# Create Sample Dataset:
The code reads and processes a CSV file containing textual data, identifying duplicates, concatenating text by groups, and exporting the results, optimizing the data for report generation.

# Indexing:

1. Create a vocabulary by employing the code found in the vocab folder, adhering to the map-reduce paradigm.
2. Utilize the map-reduce Python files in the tf folder to establish Term Frequency (TF) for each word in the articles.
3. Generate Document Frequency (DF) using the map-reduce process outlined in the df folder.
4. Compute the Inverse Document Frequency (IDF) scores for each article using the code available in the score folder, leveraging the output from TF and DF mappers and reducers.

# Vector Space Model Creation:
Convert the resulting array into a Vector Space Model (VSM) by employing the code located in the vsm folder.

# Running on Hadoop:
To run the MapReduce jobs on Hadoop, follow these steps:

1. Ensure you have Hadoop installed and configured properly on your system.
2. Ensure you have python3 installed in you system.
3. Upload your input data to the Hadoop Distributed File System (HDFS).
4. Compile your MapReduce code into a JAR file.
5. Use the Hadoop command line interface to submit your MapReduce job, specifying the input and output paths, and the JAR file containing your code.


