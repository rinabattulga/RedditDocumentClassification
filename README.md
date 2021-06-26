# RedditDocumentClassification
Used Reddit corpora to compare document two linear systems: Support Vector Machine and Naive Bayes, and two Neural Networks: Deep Averaging Network (DAN) and Bi-directional LSTM (BiLSTM)

Used Classification algorithm code from online sources.
https://towardsdatascience.com/text-classification-with-nlp-tf-idf-vs-word2vec-vs-bert-41ff868d1794 

Cleaned web-scraped Reddit data with datacleaning.py file. 

Merged different category data values with merge_col.py and merge_diff_file.py files.

Used confusionmatrix.py to create a confusion matrix to calculate Accuracy, Error rate, Precision, Recall, and F1-score for each algorithm. 
