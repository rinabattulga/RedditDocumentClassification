# Introduction
Used Reddit corpora to compare two linear systems: Support Vector Machine and Naive Bayes, and two Neural Networks: Deep Averaging Network (DAN) and Bi-directional LSTM (BiLSTM). 

TF-IDF word vectorization and Naive Bayes classification were used as the base system to analyze the accuracy, precision, recall, and F1-scores generated from the confusion matrices of the algorithms. 

BiLSTM and DAN outperformed Naive Bayes by over 10% on F1-score and recall, while SVM performed slightly lower than our base. 

## Python files
Cleaned Reddit data from Kaggle with datacleaning.py file. 

Merged different category data values with merge_col.py and merge_diff_file.py files.

Used confusionmatrix.py to create a confusion matrix to calculate Accuracy, Error rate, Precision, Recall, and F1-score for each algorithm. 

## Data

### Data Preparation

Obtained 9 different categories of Reddit data: cryptocurrency, showerthoughts, coronavirus, suicideanddepression, cyberpunk, jokes, texas, wallstreetbets, and recipes.

Used datasets from:

www.kaggle.com/gpreda/reddit-wallstreetsbets-posts
www.kaggle.com/cuddlefish/reddit-rjokes
https://www.kaggle.com/nickreinerink/reddit-rcryptocurrency 
https://www.kaggle.com/nikhileswarkomati/suicide-watch 
https://www.kaggle.com/jaedebug/rtexas-reddit-posts 
https://www.kaggle.com/maxspunnring/reddit-rdankmemes-top-1000-memes 
https://www.kaggle.com/xhlulu/covid19-vaccine-news-reddit-discussions 
https://www.kaggle.com/matheusdalbuquerque/rcyberpunkgame-posts?select=Posts.csv 
https://www.kaggle.com/vishxl/showerthoughts 
https://www.kaggle.com/viktorarsovski/randroiddev-data-20152019

Randomly partitioned dataset into trainging (80%), validation (10%), and test (10%). 

Important to note that the dataset is skewed with some categories having way more datapoints. 

![alt text](https://github.com/rinabattulga/RedditDocumentClassification/blob/main/SkewedDist.png)
