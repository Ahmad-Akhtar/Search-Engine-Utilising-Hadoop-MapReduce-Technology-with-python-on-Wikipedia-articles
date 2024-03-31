Building a Naive Search Engine on Wikimedia Dataset Using Map-Reduce

Steps:

1-Preprocessing the Dataset:  

  Conduct preprocessing on the dataset, focusing on the necessary columns.

2-Indexing:

  2.1-Create a vocabulary by employing the code found in the vocab folder, adhering to the map-reduce paradigm.
  2.2-Utilize the map-reduce Python files in the tf folder to establish Term Frequency (TF) for each word in the articles.
  2.3-Generate Document Frequency (DF) using the map-reduce process outlined in the df folder.
  2.4-Compute the Inverse Document Frequency (IDF) scores for each article using the code available in the score folder, leveraging the output from TF and DF mappers and reducers.

3-Vector Space Model Creation:

  Convert the resulting array into a Vector Space Model (VSM) by employing the code located in the vsm folder.
